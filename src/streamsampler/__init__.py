from __future__ import print_function, absolute_import

import sys, os.path
import random
from optparse import OptionParser
import locale

from . import streamsampler as ss
from . import cli

StreamSampler = ss.StreamSampler
Cli = cli.Cli

def main():
    parser = OptionParser()
    parser.add_option("-n", action="store", type="int", dest="number", default=1000,
                      help="Take N samples from input data stream", metavar="N")
    parser.add_option("-s", action="store", type="int", dest="seed", default=None,
                      help="Seed value for random variables", metavar="S")
    parser.add_option("-d", "--delim", type="string", dest="delim", default=None,
                      help="Delimiter character(s)")
    parser.add_option("--no-preserve", action="store_false", dest="preserve", default=True,
                      help="Preserve the order of data")
    parser.add_option("--report", dest="report", action="store_true", default=False,
                      help="Report the number of read/sampled lines to stderr")

    (options, args) = parser.parse_args()
    kwd = {}

    if options.seed is not None:
        random.seed(options.seed)

    if options.preserve == False:
        print("Not preserving")
        kwd['preserve'] = False

    if options.delim is not None:
        kwd['delim'] = options.delim

    kwd['number'] = options.number
    
    c = Cli(**kwd)

    if len(args) == 0:
        for line in sys.stdin:
            c.feed(line)
    else:
        for fname in args:
            f = open(fname, 'r')
            for ln in f.readlines():
                c.feed(ln)
            f.close()

    for line in c:
        print(line)

    if options.report:
        c.show_report(sys.stderr)
    
if __name__ == "__main__":
    main()

