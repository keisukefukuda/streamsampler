# Example package with a console entry point

import sys, os.path
import random
from optparse import OptionParser
import locale

from streamsampler import StreamSampler

def main():
    parser = OptionParser()
    parser.add_option("-n", action="store", type="int", dest="number", default=1000,
                      help="Take N samples from input data stream", metavar="N")
    parser.add_option("--report", dest="report", action="store_true", default=False,
                      help="Report the number of read/sampled lines to stderr")

    (options, args) = parser.parse_args()

    k = options.number

    ss = StreamSampler(k)

    if len(args) == 0:
        for line in sys.stdin:
            ss.append(line.strip())
    else:
        for fname in args:
            f = open(fname, 'r')
            for line in f:
                ss.append(line.strip())
            f.close()

    for line in ss.get():
        print line

    if options.report:
        locale.setlocale(locale.LC_ALL, "en_US")
        t = ss.total_count()
        sys.stderr.write("%s: %s lines read, %s lines sampled (%.3f%%)\n" %
                         (os.path.basename(sys.argv[0]),
                          locale.format("%d", t, grouping=True),
                          locale.format("%d", len(ss), grouping=True),
                          len(ss)*100./t if t > 0 else 0))
            
    
