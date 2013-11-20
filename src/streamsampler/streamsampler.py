"""
streamsampler.streamsampler 
// http://en.wikipedia.org/wiki/Reservoir_sampling
Reservoir sampling
array R[k];    // result
integer i, j;

// fill the reservoir array
for each i in 1 to k do
    R[i] := S[i]
done;

// replace elements with gradually decreasing probability
for each i in k+1 to length(S) do
    j := random(1, i);   // important: inclusive range
    if j <= k then
        R[j] := S[i]
    fi
done
"""

import random

class StreamSampler(object):
    def __init__(self, k, **kwd):
        self._k = k
        self._i = 0
        self._R = []
        self._S = None
        self._preserve = True

        if 'preserve' in kwd:
            self._preserve = bool(kwd['preserve'])
            del kwd['preserve']

        if len(kwd) != 0:
            raise ArgumentError("Unknown keyword arguments: " + ','.join(kwd.keys()))

    def append(self, elm):
        if self._k > 0:
            i = self._i
            if len(self._R) >= self._k:
                j = random.randint(0, i-1)
                if j < self._k:
                    self._R[j] = (i, elm)
            else:
                self._R.append((i,elm))
            self._i += 1
            self._S = None

    def append_all(self, lst):
        for e in lst:
            self.append(e)
        self._S = None

    def __len__(self):
        return len(self._R)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("list indices must be integers, not " + type(key).__name__)

        if key >= len(self):
            raise IndexError("list index out of range")

        self.__sort()
        return self._S[key]

    def __iter__(self):
        self.__sort()
        for elm in self._S:
            yield elm

    def __sort(self):
        if self._S is None:
            if self._preserve:
                tmp = sorted(self._R, key=lambda d: d[0])
            else:
                tmp = self._R
            self._S = [e[1] for e in tmp]
            

    def total_count(self):
        return self._i
        

