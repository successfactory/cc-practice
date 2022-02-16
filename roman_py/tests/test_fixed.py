import romanenc
import unittest


class FixedTestCase(unittest.TestCase):
    def test_romanenc_fixed2(self):
        self.assertEqual("II", romanenc.encode(2))

    def test_romanenc_fixed3(self):
        self.assertEqual("III", romanenc.encode(3))

    def test_romanenc_fixed5(self):
        self.assertEqual("V", romanenc.encode(5))

    def test_romanenc_fixed9(self):
        self.assertEqual("IX", romanenc.encode(9))

    def test_romanenc_fixed10(self):
        self.assertEqual("X", romanenc.encode(10))

    def test_romanenc_fixed11(self):
        self.assertEqual("XI", romanenc.encode(11))

    def test_romanenc_fixed15(self):
        self.assertEqual("XV", romanenc.encode(15))

    def test_romanenc_fixed19(self):
        self.assertEqual("XIX", romanenc.encode(19))

    def test_romanenc_fixed22(self):
        self.assertEqual("XXII", romanenc.encode(22))

    def test_romanenc_fixed1001(self):
        self.assertEqual("MI", romanenc.encode(1001))

    def test_romanenc_fixed2008(self):
        self.assertEqual("MMVIII", romanenc.encode(2008))
