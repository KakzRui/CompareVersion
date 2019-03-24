import unittest
from compare_version import compare


class CompareVersionTest(unittest.TestCase):
    def test_greater(self):
        v1, v2 = 4.5, 3.4
        self.assertEqual(compare(v1, v2), 'version {} is greater than version {}'.format(v1, v2))

    def test_less_than(self):
        v1, v2 = 2.5, 4.4
        self.assertEqual(compare(v1, v2), 'version {} is less than version {}'.format(v1, v2))

    def test_equal(self):
        v1, v2 = 1.0, 1.0
        self.assertEqual(compare(v1, v2), 'version {} is equal to version {}'.format(v1, v2))

    def test_conv_ver_str(self):
        v1, v2 = '1.2', '2.3'
        self.assertEqual(compare(v1, v2), 'version {} is less than version {}'.format(1.2, 2.3))


if __name__ == '__main__':
    unittest.main()
