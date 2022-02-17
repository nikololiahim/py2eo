xdoctests = "\n\nUnpack tuple\n\n    >>> t = (1, 2, 3)\n    >>> a, b, c = t\n    >>> a == 1 and b == 2 and c == 3\n    True\n\nUnpack list\n\n    >>> l = [4, 5, 6]\n    >>> a, b, c = l\n    >>> a == 4 and b == 5 and c == 6\n    True\n\nUnpack implied tuple\n\n    >>> a, b, c = 7, 8, 9\n    >>> a == 7 and b == 8 and c == 9\n    True\n\nUnpack string... fun!\n\n    >>> a, b, c = 'one'\n    >>> a == 'o' and b == 'n' and c == 'e'\n    True\n\nUnpack generic sequence\n\n    >>> class Seq:\n    ...     def __getitem__(self, i):\n    ...         if i >= 0 and i < 3: return i\n    ...         raise IndexError\n    ...\n    >>> a, b, c = Seq()\n    >>> a == 0 and b == 1 and c == 2\n    True\n\nSingle element unpacking, with extra syntax\n\n    >>> st = (99,)\n    >>> sl = [100]\n    >>> a, = st\n    >>> a\n    99\n    >>> b, = sl\n    >>> b\n    100\n\nNow for some failures\n\nUnpacking non-sequence\n\n    >>> a, b, c = 7\n    Traceback (most recent call last):\n      ...\n    TypeError: cannot unpack non-iterable int object\n\nUnpacking tuple of wrong size\n\n    >>> a, b = t\n    Traceback (most recent call last):\n      ...\n    ValueError: too many values to unpack (expected 2)\n\nUnpacking tuple of wrong size\n\n    >>> a, b = l\n    Traceback (most recent call last):\n      ...\n    ValueError: too many values to unpack (expected 2)\n\nUnpacking sequence too short\n\n    >>> a, b, c, d = Seq()\n    Traceback (most recent call last):\n      ...\n    ValueError: not enough values to unpack (expected 4, got 3)\n\nUnpacking sequence too long\n\n    >>> a, b = Seq()\n    Traceback (most recent call last):\n      ...\n    ValueError: too many values to unpack (expected 2)\n\nUnpacking a sequence where the test for too long raises a different kind of\nerror\n\n    >>> class BozoError(Exception):\n    ...     pass\n    ...\n    >>> class BadSeq:\n    ...     def __getitem__(self, i):\n    ...         if i >= 0 and i < 3:\n    ...             return i\n    ...         elif i == 3:\n    ...             raise BozoError\n    ...         else:\n    ...             raise IndexError\n    ...\n\nTrigger code while not expecting an IndexError (unpack sequence too long, wrong\nerror)\n\n    >>> a, b, c, d, e = BadSeq()\n    Traceback (most recent call last):\n      ...\n    test.test_unpack.BozoError\n\nTrigger code while expecting an IndexError (unpack sequence too short, wrong\nerror)\n\n    >>> a, b, c = BadSeq()\n    Traceback (most recent call last):\n      ...\n    test.test_unpack.BozoError\n\nAllow unpacking empty iterables\n\n    >>> () = []\n    >>> [] = ()\n    >>> [] = []\n    >>> () = ()\n\nUnpacking non-iterables should raise TypeError\n\n    >>> () = 42\n    Traceback (most recent call last):\n      ...\n    TypeError: cannot unpack non-iterable int object\n\nUnpacking to an empty iterable should raise ValueError\n\n    >>> () = [42]\n    Traceback (most recent call last):\n      ...\n    ValueError: too many values to unpack (expected 0)\n\n" # 1:0-1:2853
x__test__ = {"doctests" : xdoctests} # 143:0-143:33
def xtest_main(xverbose = False): # 145:0-150:-1
    from xtest import xsupport # 146:21-146:27
    from xtest import xtest_unpack # 147:21-147:31
    e0 = xsupport.xrun_doctest # 148:4-148:22
    lhs0 = xtest_unpack # 148:24-148:34
    lhs1 = xverbose # 148:37-148:43
    e1 = e0(lhs0, lhs1) # 148:4-148:44
e3 = (x__name__ == "__main__") # 150:3-150:24
if (e3): # 150:26-152:-1 
    e2 = xtest_main(xverbose=True) # 151:4-151:26
else: # 150:0-152:-1
    pass # 150:0-152:-1