from __future__ import print_function, absolute_import

import re
from . import streamsampler as ss

class Cli(object):
    def __init__(self, **kwd):
        if 'number' in kwd:
            try:
                number = int(kwd['number'])
            except ValueError:
                raise ValueError("Argument number must be an integer")

            if number < 0:
                raise ValueError("Argument number must be >0")

            del kwd['number']
        else:
            number = 1000

        if 'delim' in kwd:
            self._delim = kwd['delim']
            del kwd['delim']
            print("OK, we've got delimiter string '%s'" % self._delim)
        else:
            self._delim = None

        if 'preserve' in kwd:
            preserve = bool(kwd['preserve'])
        else:
            preserve = True

        self._stream = ""
        self._ss = ss.StreamSampler(number, preserve=preserve)

    def feed(self, s):
        self._stream += s

        if self._delim is None:
            while True:
                m = re.search(r'\r\n|\r|\n', self._stream)
                if m:
                    self._ss.append(self._stream[0:m.start(0)])
                    self._stream = self._stream[m.end(0):]
                else:
                    break
        else:
            while True:
                ind = self._stream.find(self._delim)
                if ind < 0:
                    break
                else:
                    self._ss.append(self._stream[0:ind])
                    self._stream = self._stream[ind+1:]

    def __iter__(self):
        for elm in self._ss:
            yield elm

    def __len__(self):
        return len(self._ss)

    def show_report(self, out):
        locale.setlocale(locale.LC_ALL, "en_US")
        t = _ss.total_count()
        out.write("%s: %s lines read, %s lines sampled (%.3f%%)\n" %
                  (os.path.basename(sys.argv[0]),
                   locale.format("%d", t, grouping=True),
                   locale.format("%d", len(ss), grouping=True),
                   len(ss)*100./t if t > 0 else 0))
