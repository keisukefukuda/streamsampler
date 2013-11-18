import streamsampler
import test_streamsampler

def suites():
    import unittest
    import doctest
    suite = unittest.TestSuite()
    #suite.addTests(doctest.DocTestSuite(streamsampler))
    suite.addTests(test_streamsampler.suite())
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
