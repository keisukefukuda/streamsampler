import sys
import random
import unittest

from streamsampler import StreamSampler

class StreamSamplerTestCase(unittest.TestCase):
    def setUp(self):
        random.seed(0)

        # Since the implementations of random modules of 2 and 3 are different,
        # we need to prepare two answers.
        self.py3_ans = [818, 784, 2, 929, 503]
        self.py2_ans = [407, 998, 911, 517, 668]

    def test_rand(self):
        ss = StreamSampler(5, preserve=False)
        for i in range(1000): ss.append(i)
        if sys.version_info[0] == 2:
            self.assertEqual(list(ss),  self.py2_ans)
        elif sys.version_info[0] == 3:
            self.assertEqual(list(ss),  self.py3_ans)

    def test_rand_preserved(self):
        ss = StreamSampler(5)
        for i in range(1000): ss.append(i)
        if sys.version_info[0] == 2:
            self.assertEqual(list(ss),  sorted(self.py2_ans))
        elif sys.version_info[0] == 3:
            self.assertEqual(list(ss),  sorted(self.py3_ans))

    def test_small(self):
        ss = StreamSampler(5)
        for i in range(5): ss.append(i)
        self.assertEqual(list(ss), list(range(5)))

    def test_small_2(self):
        ss = StreamSampler(5)
        ss.append_all(range(5))
        self.assertEqual(list(ss), list(range(5)))

    def test_k(self):
        for k in range(100):
            ss = StreamSampler(k)
            for i in range(5 * k):
                ss.append(i)
            self.assertEqual(len(ss), k)

def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(StreamSamplerTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
