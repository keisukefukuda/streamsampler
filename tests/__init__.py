import streamsampler
import test_cli
import test_streamsampler


def suites():
    import doctest
    import unittest

    suite = unittest.TestSuite()
    # suite.addTests(doctest.DocTestSuite(streamsampler))
    suite.addTests(test_streamsampler.suite())
    suite.addTests(test_cli.suite())
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
