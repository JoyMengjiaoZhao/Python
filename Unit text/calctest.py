import unittest
import calc

class testcalc(unittest.TestCase):

    def test_add(self):   #have to start with 'test_'
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)

    def test_subtract(self):   #have to start with 'test_'
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-1,1),-2)
        self.assertEqual(calc.subtract(-1,-1),0)

    def test_multiply(self):   #have to start with 'test_'
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-1,1),-1)
        self.assertEqual(calc.multiply(-1,-1),1)

    def test_divide(self):   #have to start with 'test_'
        self.assertEqual(calc.divide(5,2),2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertEqual(calc.divide(-1,-1),1)

        #self.assertRaises(ValueError, calc.divide,10,0) # check the error raise
        with self.assertRaises(ValueError): #context manager (way 2)
            calc.divide(10,0)
if __name__=='__main__':   #allow editor run all the def
    unittest.main()
