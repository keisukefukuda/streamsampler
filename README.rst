StreamSampler
=============

StreamSampler package allows you to sample a particular number of elements from
a stream of data of which length is very large or unknown.

StreamSampler is provided in both forms of an executable command and library.
It utilizes Reservoir sampling algorithm [`Vitter85`_]

You can take a look at the README.txt of other projects, such as repoze.bfg
(http://bfg.repoze.org/trac/browser/trunk/README.txt) for some ideas.

.. _`Vitter85`: Random Sampling with a Reservoir http://www.cs.umd.edu/~samir/498/vitter.pdf



License
-------
MIT License

See Also
--------
* `sample-cli`_ by Paul Butler is a command line tool providing almost the same feature. StreamSampler is intended to be a library, although it has a command line interface, so that it can be a part of other packages including my future projects.

.. _`sample-cli`: https://pypi.python.org/pypi/sample-cli/
