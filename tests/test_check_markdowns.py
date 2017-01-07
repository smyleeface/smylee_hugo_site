import unittest


class TestCheckMarkdown(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOmO')

if __name__ == '__main__':
    unittest.main()
