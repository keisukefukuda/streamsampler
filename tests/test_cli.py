import sys
import random
import unittest

from streamsampler import Cli

class StreamSamplerCliTestCase(unittest.TestCase):
    def setUp(self):
        random.seed(0)

    def test_ok(self):
        self.assertTrue(True)

    def test_basic(self):
        for n in range(10):
            cli = Cli(number=n)
            cli.feed("\n".join([str(i) for i in range(1000)]))
            res = [int(x) for x in list(cli)]
            self.assertEqual(len(res), n)

        self.assertEqual(res, sorted(res))

    def test_another_delim(self):
        cli = Cli(number = 10, delim=" ")
        cli.feed(' '.join([str(i) for i in range(1000)]))
        res = [int(x) for x in list(cli)]
        self.assertEqual(len(res), 10)

def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(StreamSamplerCliTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
