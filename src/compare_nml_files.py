import f90nml
import argparse

def read_nml(filepath):
    '''Load a file given the filepath. Return a dict object.'''
    with open(filepath) as nml_file:
        nml = f90nml.read(nml_file)
        return nml

def write_nml(input_path, output_path):
    '''Write an object to a file at the output_path provided.'''
    with open(input_path) as nml_file:
        nml = f90nml.write(nml_file)
        return nml

def compare_nml(nml_file1, nml_file2):
    '''Takes in two namelist files. Parses each of the namelist files. Compare values of the namelist files. Will return the differences between the two files.'''
    pass
