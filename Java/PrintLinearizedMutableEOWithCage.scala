import Expression.{CallIndex, CollectionCons, Cond, DictCons, Field, Ident, Parameter, StringLiteral}
import PrintEO.{EOVisibility, Text, indent, printExpr}
import PrintLinearizedImmutableEO.rmUnreachableTail
import PrintLinearizedMutableEONoCage.headers

import scala.annotation.tailrec
import scala.collection.immutable.HashMap

object PrintLinearizedMutableEOWithCage {

  val bogusVisibility = new EOVisibility()

  @tailrec
  def isSeqOfFields(x : Expression.T) : Boolean = x match {
    case Field(whose, name, ann) => isSeqOfFields(whose)
    case CallIndex(false, whom, List((_, StringLiteral(_, _))), ann) => isSeqOfFields(whom)
    case Ident(_, _) => true
    case _ => false
  }

  def printFun(newName : String, f : FuncDef) : Text = {
    val (Suite(l0, _), _) = SimplePass.procStatement(SimplePass.unSuite)(Suite(List(f.body), f.body.ann.pos), SimplePass.Names(HashMap()))
    val l = rmUnreachableTail(l0)
    //    println(s"l = \n${PrintPython.printSt(Suite(l), "-->>")}")
    def pe = printExpr(bogusVisibility)(_)
    def isFun(f : Statement) = f match { case f : FuncDef => true case _ => false }
    val funs = l.filter(isFun)
    val funNames = funs.map{ case f : FuncDef => f.name }.toSet
    val argCopies = f.args.map(parm => s"${parm.name}NotCopied' > x${parm.name}")
    val memories = f.accessibleIdents.filter(x => x._2._1 == VarScope.Local && !funNames.contains(x._1)).
      map(x => s"cage > x${x._1}").toList
    val innerFuns = funs.flatMap{case f : FuncDef => (printFun(f.name, f))}

    def others(ns : SimplePass.Names, l : List[Statement]) : (SimplePass.Names, Text) =
      l.foldLeft((ns, List[String]()))((acc, st) => st match {
        case NonLocal(l, _) => acc
        case SimpleObject(name, l, ann) =>
          (acc._1, acc._2 ++ ("write." ::
            indent("x" + name :: "[]" :: indent(
              l.map{ case (name, value) => "cage > x" + name } ++ (
                "seq > @" :: indent(l.map{case (name, value) => s"x$name.write " + pe(value)})
              ))
            )) :+ s"x$name.@")
        case f : FuncDef => (acc._1, acc._2 :+ s"${f.name}.write ${f.name}Fun")
        case Assign(List(lhs, rhs@CallIndex(true, whom, args, ann)), _) if isSeqOfFields(whom) && isSeqOfFields(lhs) =>
//          assert(args.forall{ case (_, Ident(_, _)) => true  case _ => false })
          (ns, List(
            s"tmp.write ${pe(rhs)}",
            "tmp.@",
            s"${pe(lhs)}.write (tmp.xresult)"
          ))
        case Assign(List(lhs, rhs), _) if isSeqOfFields(lhs) =>
          (acc._1, acc._2 :+ s"${pe(lhs)}.write ${pe(rhs)}.@")
        case Assign(List(e), _) => (acc._1, acc._2 :+ pe(e))
        case Return(e, ann) => e match {
          case Some(value) =>
            val (ns1, sts) = others(acc._1, List(Assign(List(Ident("result", ann.pos), value), ann.pos)))
            (ns1, acc._2 ++ sts)
          case None => acc
        }
        case IfSimple(cond, Return(Some(yes), _), Return(Some(no), _), ann) =>
          val (ns1, stsY) = others(acc._1, List(Assign(List(Ident("result", ann.pos), yes), ann.pos)))
          val (ns2, stsN) = others(ns1,    List(Assign(List(Ident("result", ann.pos), no), ann.pos)))
          val ifelse = pe(cond) + ".if" :: indent("seq" :: indent(stsY)) ++ indent("seq" :: indent(stsN))
          (ns2, acc._2 ++ ifelse)
        case Pass(_) => acc
        case Suite(l, _) => others(ns, l)
      })

    val args1 = f.args.map{ case Parameter(argname, kind, None, None, _) if kind != ArgKind.Keyword =>
      argname + "NotCopied" }.mkString(" ")
    s"[$args1] > x${newName}" :: indent(
      "cage > xresult" ::
      "cage > tmp" ::
      argCopies ++ memories ++ innerFuns ++
        ("seq > @" :: indent(
  //          s"stdout \"$newName\\n\"" ::
              f.args.map(parm => s"${parm.name}.<") ++
              others(new SimplePass.Names(), l.filterNot(isFun))._2  :+
                "123"
            )
          )
    )
  }

  def printTest(testName : String, st : Statement) : Text = {
    println(s"doing $testName")
    val theTest@FuncDef(_, _, _, _, _, _, _, _, _, _) =
      SimpleAnalysis.computeAccessibleIdents(FuncDef(testName, List(), None, None, None, st, Decorators(List()),
        HashMap(), false, st.ann.pos))
    headers ++ printFun(theTest.name, theTest)
  }


}