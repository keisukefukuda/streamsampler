from __future__ import print_function, absolute_import

import sys, os.path
import random
from optparse import OptionParser
import locale

from . import streamsampler

StreamSampler = streamsampler.StreamSampler

def main():
    parser = OptionParser()
    parser.add_option("-n", action="store", type="int", dest="number", default=1000,
                      help="Take N samples from input data stream", metavar="N")
    parser.add_option("-s", action="store", type="int", dest="seed", default=None,
                      help="Seed value for random variables", metavar="S")
    parser.add_option("--no-preserve", action="store_false", dest="preserve", default=True,
                      help="Preserve the order of data")
    parser.add_option("--report", dest="report", action="store_true", default=False,
                      help="Report the number of read/sampled lines to stderr")

    (options, args) = parser.parse_args()
    kwd = {}

    k = options.number

    if options.seed is not None:
        random.seed(options.seed)

    if options.preserve == False:
        print("Not preserving")
        kwd['preserve'] = False

    ss = StreamSampler(k, **kwd)

    if len(args) == 0:
        for line in sys.stdin:
            ss.append(line.strip())
    else:
        for fname in args:
            f = open(fname, 'r')
            for line in f:
                ss.append(line.strip())
            f.close()

    for line in ss:
        print(line)

    if options.report:
        locale.setlocale(locale.LC_ALL, "en_US")
        t = ss.total_count()
        sys.stderr.write("%s: %s lines read, %s lines sampled (%.3f%%)\n" %
                         (os.path.basename(sys.argv[0]),
                          locale.format("%d", t, grouping=True),
                          locale.format("%d", len(ss), grouping=True),
                          len(ss)*100./t if t > 0 else 0))
            
    
