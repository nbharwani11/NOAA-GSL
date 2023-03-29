import argparse
import f90nml
import os
import pytest

from src import compare_nml_files

noaa_file_base = os.path.join(os.path.dirname(__file__))


def test_read_file(self):
    '''Reads content of a file using file path.'''
    input_file = os.path.join(noaa_file_base, "fixtures/example.nml")

def test_write_file(self):
    '''Writes content of a file using the inout file path and output file path provided'''
    pass

