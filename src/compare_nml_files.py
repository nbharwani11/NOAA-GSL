import f90nml
import argparse

def read_nml(filepath):
    ''' Load a file given the filepath. Return a dict object.'''
    with open(filepath) as nml_file:
        nml = f90nml.read(nml_file)

def write(input_path, output_path):
    ''' Write an object to a file at the output_path provided.'''
    with open(input_path) as nml_file:
        nml = f90nml.write(nml_file)

