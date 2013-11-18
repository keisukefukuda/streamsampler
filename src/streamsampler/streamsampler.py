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

class StreamSampler(object):
    def __init__(self, k):
        self._k = k
        self._i = 0
        self._R = []

    def append(self, elm):
        if len(self._R) >= self._k:
            i = self._i
            j = random.randint(0, i-1)
            if j < self._k:
                self._R[j] = elm
        else:
            self._R.append(elm)
        self._i += 1

    def __len__(self):
        return len(self._R)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("list indices must be integers, not " + type(key).__name__)

        if key >= len(self):
            raise IndexError("list index out of range")

        return self._R[key]

    def total_count(self):
        return self._i
        

