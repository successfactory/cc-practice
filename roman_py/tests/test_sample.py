import romanenc
import unittest


class SamplesTestCase(unittest.TestCase):
    def test_romanenc_sample1(self):
        self.assertEqual("I", romanenc.encode(1))

    def test_romanenc_sample4(self):
        self.assertEqual("IV", romanenc.encode(4))

    def test_romanenc_sample1000(self):
        self.assertEqual("M", romanenc.encode(1000))

    def test_romanenc_sample1990(self):
        self.assertEqual("MCMXC", romanenc.encode(1990))

    def test_romanenc_sample2020(self):
        self.assertEqual("MMXX", romanenc.encode(2020))
