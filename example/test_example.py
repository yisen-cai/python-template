import unittest

import logging
from logging import config

logging.config.fileConfig(
    'logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# @unittest.skip("skip example")
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        """
        setUp method for each test
        :return:
        """
        logger.info("setUp method invoking...")

    def tearDown(self) -> None:
        """
        tearDown method for each test
        :return:
        """
        logger.info("tearDown method invoking...")

    @unittest.skip("skip test")
    def test_something(self):
        self.assertEqual(True, 1 == 1)

    @unittest.skipIf(1 < 2, "one less than two")
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    @unittest.skipUnless(1 < 2, "one not less than 2")
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

    def test_skip_method(self):
        if 1 < 2:
            self.skipTest("one less than two")
        pass

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("setUp class method invoking...")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("tearDown class method invoking...")

    @unittest.skip("skip error test")
    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


if __name__ == '__main__':
    # python -m unittest test_module1 test_module2 -v
    # python -m unittest test_module.TestClass -v
    # python -m unittest test_module.TestClass.test_method -v
    unittest.main(verbosity=2)
