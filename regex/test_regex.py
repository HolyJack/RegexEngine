import unittest
from regex import *


class MyTestCase(unittest.TestCase):
    def test_simple(self):
        #   Testing basic cases with ^, $ and . metacharacters
        self.assertTrue(regex_string_improved('^app', 'apple'))
        self.assertTrue(regex_string_improved('le$', 'apple'))
        self.assertTrue(regex_string_improved('^a', 'apple'))
        self.assertTrue(regex_string_improved('.$', 'apple'))
        self.assertTrue(regex_string_improved('apple$', 'tasty apple'))
        self.assertTrue(regex_string_improved('^apple', 'apple pie'))
        self.assertTrue(regex_string_improved('^apple$', 'apple'))
        self.assertFalse(regex_string_improved('^apple$', 'tasty apple'))
        self.assertFalse(regex_string_improved('^apple$', 'apple pie'))
        self.assertFalse(regex_string_improved('app$', 'apple'))
        self.assertFalse(regex_string_improved('^le', 'apple'))

    def test_med_part1(self):
        #   Testing '?' metacharacter
        self.assertTrue(regex_string_improved('colou?r', 'color'))
        self.assertTrue(regex_string_improved('colou?r', 'colour'))
        self.assertFalse(regex_string_improved('colou?r', 'colouur'))

    def test_med_part2(self):
        #   Testing '*' metacharacter
        self.assertTrue(regex_string_improved('colou*r', 'color'))
        self.assertTrue(regex_string_improved('colou*r', 'colour'))
        self.assertTrue(regex_string_improved('colou*r', 'colouur'))

    def test_med_part3(self):
        #   Testing '+' metacharacter
        self.assertFalse(regex_string_improved('+', 'cccc'))
        self.assertFalse(regex_string_improved('colou+r', 'color'))
        self.assertTrue(regex_string_improved('colou+r', 'colour'))
        self.assertTrue(regex_string_improved('colou+r', 'colouuur'))

    def test_hard_part1(self):
        #   Testing metacharacters interactions
        self.assertTrue(regex_string_improved('col.*r', 'color'))
        self.assertTrue(regex_string_improved('col.*r', 'colour'))
        self.assertTrue(regex_string_improved('col.*r', 'colr'))
        self.assertTrue(regex_string_improved('col.*r', 'collar'))
        self.assertFalse(regex_string_improved('col.*r$', 'colors'))
        self.assertTrue(regex_string_improved('^col.*r', 'color'))

    def test_hard_part2(self):
        #   Testing metacharacters interactions
        self.assertTrue(regex_string_improved('col.+r', 'color'))
        self.assertTrue(regex_string_improved('col.+r', 'colour'))
        self.assertFalse(regex_string_improved('col.+r', 'colr'))
        self.assertTrue(regex_string_improved('col.+r', 'collar'))
        self.assertFalse(regex_string_improved('col.+r$', 'colors'))
        self.assertTrue(regex_string_improved('^col.+r', 'color'))

    def test_hard_part3(self):
        #   Testing metacharacters interactions
        self.assertTrue(regex_string_improved('col.?r', 'color'))
        self.assertFalse(regex_string_improved('col.?r', 'colour'))
        self.assertTrue(regex_string_improved('col.?r', 'colr'))
        self.assertFalse(regex_string_improved('col.?r', 'collar'))
        self.assertFalse(regex_string_improved('col.?r$', 'colors'))
        self.assertTrue(regex_string_improved('^col.?r', 'color'))

    def test_escape_sequence(self):
        #   Testing escape sequence interactions
        self.assertTrue(regex_string_improved('\\.$', 'end.'))
        self.assertTrue(regex_string_improved('3\\+3', '3+3=6'))
        self.assertTrue(regex_string_improved('\\?', 'Is this working?'))
        self.assertTrue(regex_string_improved('\\\\', '\\'))
        self.assertFalse(regex_string_improved('colou\\?r', 'color'))
        self.assertFalse(regex_string_improved('colou\\?r', 'colour'))

if __name__ == '__main__':
    unittest.main()
