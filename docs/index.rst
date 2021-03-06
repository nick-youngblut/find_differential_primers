.. pdp documentation master file, created by
   sphinx-quickstart on Tue Nov  6 13:46:01 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===================================
Welcome to ``pdp``'s documentation!
===================================

-----------------
Build Information
-----------------

.. image:: https://img.shields.io/travis/widdowquinn/find_differential_primers.svg?style=flat-square
   :target: https://travis-ci.org/widdowquinn/find_differential_primers
.. image:: https://img.shields.io/codecov/c/github/widdowquinn/find_differential_primers.svg?style=flat-square
   :target: https://codecov.org/widdowquinn/find_differential_primers
.. image:: https://readthedocs.org/projects/find_differential_primers/badge/?version=latest
   :target: https://find_differential_primers.readthedocs.io/en/latest/?badge=latest
.. image:: https://api.codacy.com/project/badge/Grade/f3e56b2bf118471aabf09514a3e6af75
    :target: https://www.codacy.com/app/widdowquinn/find_differential_primers?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=widdowquinn/pyani&amp;utm_campaign=Badge_Grade

------------------------------
``PyPI`` version and Licensing
------------------------------

.. image:: https://img.shields.io/pypi/v/find_differential_primers.svg?style=flat-square
   :target: https://pypi.python.org/pypi/find_differential_primers
.. image:: https://img.shields.io/pypi/l/find_differential_primers.svg?style=flat-square
   :target: https://pypi.python.org/pypi/find_differential_primers

-----------------
``conda`` version
-----------------

.. image:: https://anaconda.org/bioconda/find_differential_primers/badges/version.svg?style=flat-square
   :target: https://anaconda.org/bioconda/find_differential_primers
.. image:: https://anaconda.org/bioconda/find_differential_primers/badges/latest_release_date.svg?style=flat-square
   :target: https://anaconda.org/bioconda/find_differential_primers
.. image:: https://anaconda.org/bioconda/find_differential_primers/badges/installer/conda.svg?style=flat-square
   :target: https://conda.anaconda.org/bioconda
.. image:: https://anaconda.org/bioconda/find_differential_primers/badges/downloads.svg?style=flat-square
   :target: https://anaconda.org/bioconda/find_differential_primers
.. image:: https://anaconda.org/bioconda/pyani/badges/platforms.svg?style=flat-square
   :target: https://anaconda.org/bioconda/find_differential_primers

If you're feeling impatient, please head over to the :ref:`QuickStart Guide <pdp-quickstart>`

-----------
Description
-----------

``pdp`` is a program and Python package (``diagnostic_primers``) that provides support for design and identification of diagnostic qPCR and metabarcoding primers and marker sequences. It performs automated finding of discriminatory (real-time) PCR or qPCR primers that distinguish among genomes or other biological sequences of interest. It is also useful for the identification of metabarcoding marker sequences that can discriminate within a subset of bacterial genomes.

Where available, ``pdp`` natively takes advantage of multicore systems, and can integrate with `SGE or OGE-compatible`_ job schedulers to manage the computationally-heavy sequence comparisons.

This package can be used with either of two command-line interfaces: ``find_differential_primers``/``find_differential_primers.py``, which maintains backwards compatibility with the old ``find_differential_primers`` package, and ``pdp``, which is a new step-wise interface for scripting and performing specific stages of the design in isolation. The ability to separate out individual stages allows for scripting of branching designs, where alternative design filters and parameters may be used.

.. ATTENTION::
  The ``find_differential_primers``/``find_differential_primers.py`` interface may be deprecated in a future release.

----------------------------------------------
Reporting problems and requesting improvements
----------------------------------------------

If you encounter bugs or errors, or would like to suggest ways in which ``pdp`` can be improved, please raise a new issue at the ``pdp`` `GitHub issues page`_.

If you'd like to fix a bug or make an improvement yourself, contributions are welcomed, and guidelines on how to do this can be found at the :ref:`pdp-contributing` documentation page.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart
   installation
   find_differential_primers
   pdp
   testing
   contributing
   citations


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _GitHub issues page: https://github.com/widdowquinn/find_differential_primers/issues
.. _SGE or OGE-compatible: http://gridscheduler.sourceforge.net/
