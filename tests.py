import unittest
import csFunctions as cs

class TestLeft(unittest.TestCase):
  def test_left(self):
    self.assertEqual(cs.left('abcdef', 0), '', "Should be ''")
    self.assertEqual(cs.left('abcdef', 2), 'ab', "Should be 'ab'")
    self.assertEqual(cs.left('abcdef', 1000), 'abcdef', "Should be 'abcdef'")
    #TODO self.assertEqual(cs.left('abcdef', -1), 'abcdef', "Should be 'abcdef'")

class TestRight(unittest.TestCase):
  def test_right(self):
    self.assertEqual(cs.right('abcdef', 3), 'def')

class TestMid(unittest.TestCase):
  def test_mid(self):
    self.assertEqual(cs.mid('abcdef', 2, 3), 'bcd')

class TestInstring(unittest.TestCase):
  def test_instring(self):
    self.assertEqual(cs.instring('abcdef', 'b'), 2)
    self.assertEqual(cs.instring('abcdef', 'nada'), 0)

if __name__ == "__main__":
  unittest.main()