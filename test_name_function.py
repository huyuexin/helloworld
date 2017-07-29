import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('hu', 'yuexin')
        self.assertEqual(formatted_name, 'Hu Yuexin')
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('hu', 'xin','yue')
        self.assertEqual(formatted_name, 'Hu Yue Xin')

if __name__ == '__main__':
    main()

