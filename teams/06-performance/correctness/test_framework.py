"""The framework must catch broken code.  [STUB]

Checks, for EVERY registered pair:

  * import every correctness/test_*.py so all pairs are registered
  * for each pair: check(pair, device, fast_override=scaled(1.01)) must raise AssertionError
  * a toy pair: correct passes; wrong gradient (x1.01 in backward only) fails; NaN fails; wrong shape fails
  * rel_err(x * 1.01, x) == 0.01
"""


def test_todo():
    raise NotImplementedError("test_framework.py")
