from romanenc import encode
import unittest


class SamplesTestCase(unittest.TestCase):
    def test_romanenc_sample1(self):
        self.assertEqual("I", encode(1))

    def test_romanenc_sample4(self):
        self.assertEqual("IV", encode(4))

    def test_romanenc_sample1000(self):
        self.assertEqual("M", encode(1000))

    def test_romanenc_sample1990(self):
        self.assertEqual("MCMXC", encode(1990))

    def test_romanenc_sample2020(self):
        self.assertEqual("MMXX", encode(2020))


class FixedTestCase(unittest.TestCase):
    def test_romanenc_fixed2(self):
        self.assertEqual("II", encode(2))

    def test_romanenc_fixed3(self):
        self.assertEqual("III", encode(3))

    def test_romanenc_fixed5(self):
        self.assertEqual("V", encode(5))

    def test_romanenc_fixed9(self):
        self.assertEqual("IX", encode(9))

    def test_romanenc_fixed10(self):
        self.assertEqual("X", encode(10))

    def test_romanenc_fixed11(self):
        self.assertEqual("XI", encode(11))

    def test_romanenc_fixed15(self):
        self.assertEqual("XV", encode(15))

    def test_romanenc_fixed19(self):
        self.assertEqual("XIX", encode(19))

    def test_romanenc_fixed22(self):
        self.assertEqual("XXII", encode(22))

    def test_romanenc_fixed1001(self):
        self.assertEqual("MI", encode(1001))

    def test_romanenc_fixed2008(self):
        self.assertEqual("MMVIII", encode(2008))


class AdvancedTestCase(unittest.TestCase):
    def test_romanenc_adv1004(self):
        self.assertEqual("MIV", encode(1004))

    def test_romanenc_adv1992(self):
        self.assertEqual("MCMXCII", encode(1992))

    def test_romanenc_adv2843(self):
        self.assertEqual("MMDCCCXLIII", encode(2843))

    def test_romanenc_adv345(self):
        self.assertEqual("CCCXLV", encode(345))

    def test_romanenc_adv376(self):
        self.assertEqual("CCCLXXVI", encode(376))

    def test_romanenc_adv189(self):
        self.assertEqual("CLXXXIX", encode(189))


if __name__ == "__main__":
    unittest.main()
