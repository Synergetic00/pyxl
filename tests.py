import unittest

from excel import *

class TestExcelFunctions(unittest.TestCase):

    def test_BIN2DEC(self):
        self.assertEqual(BIN2DEC(1100100), 100)
        self.assertEqual(BIN2DEC(1111111111), -1)

    # def test_BIN2HEX(self):
    #     self.assertEqual(BIN2HEX(65), 'A')

    # def test_BIN2OCT(self):
    #     self.assertEqual(BIN2OCT(65), 'A')

    def test_CHAR(self):
        self.assertEqual(CHAR(65), 'A')
        self.assertEqual(CHAR(33), '!')

    def test_FISHER(self):
        self.assertAlmostEqual(FISHER(0.75), 0.9729551)

    def test_FISHERINV(self):
        self.assertAlmostEqual(FISHERINV(0.972955), 0.75)

if __name__ == '__main__':
    unittest.main()