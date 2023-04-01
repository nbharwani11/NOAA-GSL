import argparse
import f90nml
import os

import src.compare_nml_files as compare_nml
noaa_file_base = os.path.join(os.path.dirname(__file__))


def test_read_nml():
    '''Tests reading content of a file. Confirms the output is as expected.'''
    input_file = os.path.join(noaa_file_base, "fixtures/example.nml")
    result = compare_nml.read_nml(input_file)


    outcome = {
    'salad': {
        'fruit': 'papaya',
        'vegetable': 'eggplant',
        'how_many': 17,
        'dressing': 'ranch'
    }}
    
    assert result == outcome 


def test_compare_nml():
    '''Tests taking in two namelist files. 
    Compares values of the namelist files.
    Returns differences between the two files.
    '''
    input_file1 = os.path.join(noaa_file_base, "fixtures/example.nml")
    input_file2 = os.path.join(noaa_file_base, "fixtures/example2.nml")
    nml_1 = compare_nml.read_nml(input_file1)
    nml_2 = compare_nml.read_nml(input_file2)

    result = compare_nml.compare_nml(nml_1, nml_2)

    outcome = {
    'salad': {
        'dressing': ('ranch', 'caesar'), 
        'vegetable': ('eggplant', 'tomato')
    }}

    assert result == outcome
