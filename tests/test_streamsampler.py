from streamsampler import StreamSampler
import unittest

class StreamSamplerTestCase(unittest.TestCase):
    def test_ok(self):
        self.assertTrue(True)

def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(StreamSamplerTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
