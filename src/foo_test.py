# test.py
import unittest
from mock import patch, MagicMock
from foo import foo
from src import bar


class MyTest(unittest.TestCase):



    @patch("foo.Bar.biz") # not -> @patch("bar.Bar.biz")
    def test_foo_returnMocked(self, mock_biz):

        self.assertFalse(mock_biz.called)
        mock_biz.return_value = 'MOCKED'
        result = foo()

        self.assertEqual("MOCKED",  result)

        self.assertTrue(mock_biz.called)
        self.assertEqual(mock_biz.call_count, 1)
        self.assertIsInstance(mock_biz, MagicMock)

    def test_foo(self):

        self.assertEqual("biz", foo() )
