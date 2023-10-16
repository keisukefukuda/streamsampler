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

from streamsampler.samplers.r_sampler import RSampler


def create_sampler(k: int, algorithm: str = "R", **kwargs={}):
    algorithm = algorithm.lower()

    if algorithm not in ["r"]:
        raise ValueError(f"Unsupported sampling algorithm: {algorithm}")
    
    if algorithm == 'r':
        return RSampler(k, **kwargs)

