import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_addop(self):
        self.assertEqual(calc.addop(10,5),15)
        self.assertEqual(calc.addop(12,-5),7)
        self.assertEqual(calc.addop(-54,5),-49)
        self.assertEqual(calc.addop(-4,-5),-9)
    def test_subop(self):
        self.assertEqual(calc.subop(10,5),5)
        self.assertEqual(calc.subop(12,-5),17)
        self.assertEqual(calc.subop(-54,-5),-49)
        self.assertEqual(calc.subop(-4,-5),1)
    def test_mulop(self):
        self.assertEqual(calc.mulop(10,5),50)
        self.assertEqual(calc.mulop(12,-5),-60)
        self.assertEqual(calc.mulop(-54,-5),270)
        self.assertEqual(calc.mulop(-4,-5),20)
    def test_divop(self):
        self.assertEqual(calc.divop(10,5),2)
        self.assertEqual(calc.divop(12,-5),-2.4)
        self.assertEqual(calc.divop(-54,-5),10.8)
        self.assertEqual(calc.divop(-4,-5),0.8)

if __name__=='__main__':
    unittest.main()
