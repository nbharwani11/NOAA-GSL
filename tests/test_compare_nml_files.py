import argparse
import f90nml
import os
import importlib  

NOAA_GSL = __import__("NOAA-GSL")
from NOAA_GSL.src.compare_nml_files.py import read_nml
noaa_file_base = os.path.join(os.path.dirname(__file__))


def test_read_nml():
    '''Tests reading content of a file. Confirms the output is as expected.'''
    input_file = os.path.join(noaa_file_base, "fixtures/example.nml")
    result = read_nml.compare_nml_files(input_file)

    outcome=\
    """&salad
  fruit = 'papaya'
  vegetable = 'eggplant'
  how_many = '17'
  dressing = 'ranch'
/
"""
    assert result == outcome 



def test_compare_nml():
    '''
    '''
    pass
