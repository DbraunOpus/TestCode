import unittest

from multiwordsearch import char_list

class test(unittest.TestCase):
    def test_list_int(self):

        """
        Testing . . .
        """
        target = __import__("multiwordsearch")

        sum = target.sum

        self.assertEqual(target, sum)

if __name__ == '__main__':
    unittest.main()
