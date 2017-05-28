#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_genomedata.py

Test instantiation, methods and attributions of the GenomeData class

This test suite is intended to be run from the repository root using:

nosetests -v

(c) The James Hutton Institute 2017
Author: Leighton Pritchard

Contact:
leighton.pritchard@hutton.ac.uk

Leighton Pritchard,
Information and Computing Sciences,
James Hutton Institute,
Errol Road,
Invergowrie,
Dundee,
DD6 9LH,
Scotland,
UK

The MIT License

Copyright (c) 2017 The James Hutton Institute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import os
import unittest

from diagnostic_primers.GenomeData import GenomeData

from nose.tools import assert_equal, raises


class TestGenomeData(unittest.TestCase):

    """Class defining tests of the GenomeData object."""

    def setUp(self):
        """Set parameters for tests."""
        self.datadir = os.path.join('tests', 'test_input', 'sequences')
        self.name = "test_name"
        self.groups_list = ['group1', 'group2', 'group3']
        self.groups_str = 'group1,group2,group3'
        self.groups_set = set(self.groups_list)
        self.seqfile = os.path.join(self.datadir,
                                    'GCF_000011605.1.fasta')
        self.stitchfile = os.path.join(self.datadir,
                                       'GCF_000291725.1.fasta')
        self.stitchout = os.path.join(self.datadir,
                                      'genomedata_test_concat.fas')
        self.noambigout = os.path.join(self.datadir,
                                       'genomedata_test_noambig.fas')
        self.features = None
        self.primers = None

    def test_instantiation_grouplist(self):
        """GenomeData object instantiates with list of groups."""
        gd = GenomeData(self.name, self.groups_list, self.seqfile,
                        self.features, self.primers)

    def test_instantiation_groupstr(self):
        """GenomeData object instantiates with string of groups."""
        gd = GenomeData(self.name, self.groups_str, self.seqfile,
                        self.features, self.primers)

    def test_instantiation_groupset(self):
        """GenomeData object instantiates with set of groups."""
        gd = GenomeData(self.name, self.groups_set, self.seqfile,
                        self.features, self.primers)

    def test_stitch(self):
        """GenomeData object stitches multi-sequence input.

        The self.stitchfile path points to an input file with multiple
        sequences. We test if this needs stitching (it should), and if so
        stitch it.
        """
        gd = GenomeData(self.name, self.groups_str, self.stitchfile,
                        self.features, self.primers)
        if gd.needs_stitch:
            gd.stitch()
        # We have to take the input filename from the GenomeData object,
        # as this will have changed if stitched/ambiguities removed.
        with open(gd.seqfile, 'r') as ifh:
            with open(self.stitchout, 'r') as ofh:
                assert_equal(ifh.read(), ofh.read())

    def test_noambig(self):
        """GenomeData object replaces ambiguities in input.

        The self.stitchfile path points to an input file with multiple
        sequences, and ambiguity symbols. We test for ambiguity symbols, and
        replace them.
        """
        gd = GenomeData(self.name, self.groups_str, self.stitchfile,
                        self.features, self.primers)
        if gd.has_ambiguities:
            gd.replace_ambiguities()
        # We have to take the input filename from the GenomeData object,
        # as this will have changed if stitched/ambiguities removed.
        with open(gd.seqfile, 'r') as ifh:
            with open(self.noambigout, 'r') as ofh:
                assert_equal(ifh.read(), ofh.read())

    @raises(ValueError)
    def test_invalid_sequence(self):
        """GenomeData errors with invalid input sequence file."""
        gd = GenomeData(self.name, self.groups_str, "seqfile.notexist",
                        self.features, self.primers)

    @raises(ValueError)
    def test_invalid_features(self):
        """GenomeData errors with invalid feature file."""
        gd = GenomeData(self.name, self.groups_str, self.seqfile,
                        "features.notexist", self.primers)

    @raises(ValueError)
    def test_invalid_primers(self):
        """GenomeData errors with invalid primers file."""
        gd = GenomeData(self.name, self.groups_str, self.seqfile,
                        self.features, "primers.notexist")

    @raises(ValueError)
    def test_invalid_primers_fasta(self):
        """GenomeData errors with invalid primers_fasta file."""
        gd = GenomeData(self.name, self.groups_str, self.seqfile,
                        self.features, self.primers,
                        "primers_fasta.notexist")

    @raises(TypeError)
    def test_invalid_groups(self):
        """GenomeData errors with invalid group type."""
        gd = GenomeData(self.name, 12345, self.seqfile,
                        self.features, self.primers)
