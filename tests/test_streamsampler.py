from streamsampler import StreamSampler
import random
import unittest

class StreamSamplerTestCase(unittest.TestCase):
    def setUp(self):
        random.seed(0)
        
    def test_rand(self):
        ss = StreamSampler(5, preserve=False)
        for i in range(1000): ss.append(i)
        self.assertEqual(list(ss),  [407, 998, 911, 517, 668])

    def test_rand_preserved(self):
        ss = StreamSampler(5)
        for i in range(1000): ss.append(i)
        self.assertEqual(list(ss),  [407, 517, 668, 911, 998])

    def test_small(self):
        ss = StreamSampler(5)
        for i in range(5): ss.append(i)
        self.assertEqual(list(ss), list(range(5)))

    def test_small_2(self):
        ss = StreamSampler(5)
        ss.append_all(range(5))
        self.assertEqual(list(ss), list(range(5)))

def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(StreamSamplerTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
