#!/usr/bin/python3
import argparse
import f90nml

def read_nml(filepath):
    '''Load a file given the filepath. Return a dict object.'''
    with open(filepath) as nml_file:
        nml = f90nml.read(nml_file)
        return nml


def compare_nml(nml_file1, nml_file2):
    '''Takes in two namelist files. Parses each of the namelist files.
     Compare values of the namelist files. Will return the differences between the two files.'''
    
    diff = {}
    print(nml_file1.keys())
    print(nml_file2.keys())
    #print(nml_file1)
    #print(nml_file2)
    print()
    print()

    new_dict = nml_file1.keys() | nml_file2.keys()
    for item in nml_file1.keys() | nml_file2.keys():
        print(item, nml_file1[item], nml_file2[item])
        for val in nml_file1[item]:
            print(val)
    return diff



def main():
    '''Takes input from user of two Fortran namelist files.
    Returns differences between the files.'''
    parser = argparse.ArgumentParser()
    parser.add_argument("nml_filepath1")
    parser.add_argument("nml_filepath2")
    args = parser.parse_args()

    #print(args)
    nml_file1 = read_nml(args.nml_filepath1)
    nml_file2 = read_nml(args.nml_filepath2)

    
    #print(nml_file1)
    #print()
    #print(nml_file2)
    diff = compare_nml(nml_file1, nml_file2)
    return diff



if __name__ == "__main__":
    main()
