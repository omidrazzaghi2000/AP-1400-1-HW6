import unittest
from datetime import date
from mathap import MathAP
from shape import Rectangle,Circle,Square


# class Test(unittest.TestCase):
    # def test_math_ap_class(self):
    #     m_ap = MathAP()
    #     self.assertEqual(4, m_ap.add(2).add(2,5).subtract(3,2).result())
    #     self.assertEqual(28.15, m_ap.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result())
    #     self.assertEqual(31.95,m_ap.add([1], 3,4).add([3,5,7,8], (4, 4, 2, 6), [2,4.3,1.25]).subtract(2, [2,3], (6, 2, 4.2), [1.1,2.3]).result())
        

    # ## ----------------  Rectangle Test ----------------
    # def test_rectangle_basic(self):
    #     rect = Rectangle(5, 4)
    #     print(rect)
    #     self.assertEqual(20,rect.area())
    #     self.assertEqual(18,rect.perimeter())

    # ## ----------------  Circle Test ----------------
    # def test_rectangle_basic(self):
    #     circ = Circle(5)
    #     print(circ)
    #     self.assertEqual(79,round(circ.area()))
    #     self.assertEqual(31,round(circ.perimeter()))

    # ## ----------------  Square Test ----------------
    # def test_rectangle_basic(self):
    #     sqr = Square(5)
    #     print(sqr)
    #     self.assertEqual(25,sqr.area())
    #     self.assertEqual(20,sqr.perimeter())

    # ## ----------------  Operator power Test ----------------
    # def test_rectangle_basic(self):
    #     sqr = Square(5)**2
    #     print(sqr)
    #     self.assertEqual(625,sqr.area())
    #     self.assertEqual(400,sqr.perimeter())

    # ## ----------------  Compare and Operations Test ----------------
    # def test_rectangle_basic(self):
    #     sqr1 = Square(5)
    #     sqr2 = Square(4)
    #     sqr3 = Square(1)
    #     self.assertEqual(True,sqr1>sqr2)
    #     self.assertEqual(True,sqr1>=sqr2)
    #     self.assertEqual(False,sqr1<sqr2)
    #     self.assertEqual(False,sqr1<=sqr2)
    #     self.assertEqual(True,sqr1 == sqr2+sqr3)
        



if __name__=='__main__':
    unittest.main()