import romanenc
import unittest


class AdvancedTestCase(unittest.TestCase):
    def test_romanenc_adv1004(self):
        self.assertEqual("MIV", romanenc.encode(1004))

    def test_romanenc_adv1992(self):
        self.assertEqual("MCMXCII", romanenc.encode(1992))

    def test_romanenc_adv2843(self):
        self.assertEqual("MMDCCCXLIII", romanenc.encode(2843))

    def test_romanenc_adv345(self):
        self.assertEqual("CCCXLV", romanenc.encode(345))

    def test_romanenc_adv376(self):
        self.assertEqual("CCCLXXVI", romanenc.encode(376))

    def test_romanenc_adv189(self):
        self.assertEqual("CLXXXIX", romanenc.encode(189))
