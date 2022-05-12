package org.polystat.py2eo.transpiler

import org.junit.Assert.fail
import org.polystat.py2eo.transpiler.Main.writeFile
import org.yaml.snakeyaml.Yaml
import org.yaml.snakeyaml.error.YAMLException

import java.io.{File, FileInputStream}
import java.nio.file.{Files, Path}
import java.{lang => jl, util => ju}

trait Commons {
  val testsPrefix: String = System.getProperty("user.dir") + "/src/test/resources/org/polystat/py2eo/transpiler"

  def yaml2python(f: File): String = {
    val map = new Yaml().load[java.util.Map[String, String]](new FileInputStream(f))
    map.get("python")
  }

  def useCageHolder(test: File): Unit = {
    Transpile(test.getName.replace(".yaml", ""), yaml2python(test)) match {
      case None => fail(s"could not transpile ${test.getName}");
      case Some(transpiled) => writeFile(test, "genCageEO", ".eo", transpiled)
    }
  }

  def collect(dir: String, needsFiltering: Boolean = false): ju.Collection[Array[jl.String]] = {
    val testsPrefix = System.getProperty("user.dir") + "/src/test/resources/org/polystat/py2eo/transpiler"

    val res = collection.mutable.ArrayBuffer[String]()
    val simpleTestsFolder = new File(testsPrefix + File.separator + dir + File.separator)
    Files.walk(simpleTestsFolder.toPath).filter((p: Path) => p.toString.endsWith(".yaml")).forEach((p: Path) => {
      val testHolder = new File(p.toString)

      try {
        val map = new Yaml().load[java.util.Map[String, String]](new FileInputStream(testHolder))
        if (needsFiltering) {
          if (map.containsKey("enabled") && map.getOrDefault("enabled", "false").asInstanceOf[Boolean]) {
            res.addOne(p.toString)
          } else {
            println(s"The test ${testHolder.getName} is disabled")
          }
        } else {
          res.addOne(p.toString)
        }
      } catch {
        case e: YAMLException => fail(s"Couldn't parse ${testHolder.getName} file with error ${e.getMessage}")
        case e: ClassCastException => fail(s"Couldn't parse ${testHolder.getName} file with error ${e.getMessage}")
      }
    })


    val list = new ju.ArrayList[Array[jl.String]]()
    res.foreach(n => list.add(Array(n)))
    list
  }
}
