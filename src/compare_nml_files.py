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

    #print(set(nml_file1.keys()))
    
    for name in nml_file1.keys() | nml_file2.keys():
        group_nml1 = nml_file1.get(name)
        group_nml2 = nml_file2.get(name)

        group_diff = {}
        for key in nml_file1.keys() | nml_file2.keys():
            if group_nml1.get(key) != group_nml2.get(key):
                group_diff[key] = (group_nml1.get(key), group_nml2.get(key))
        if group_diff:
            diff[name] = group_diff
    #diff = {'salad': {'vegetable' = 'eggplant'}, {'dressing' = 'ranch'}}
    return diff


def output_diff(diff):
    '''Outputs the differences between the two Fortran files on the command line.'''
    print("Running script compare_nml_files.py with args:\n", f"{('-' * 80)}\n{('-' * 80)}")
    for name, group_diff in diff.items():
        print(f"Category: {name}")
        for key, (val1, val2) in group_diff.items():
            print(f"Key: {key}\n")
            print(f"Value 1: {val1}\n")
            print(f"Value 2: {val2}\n")

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
    if diff == {}:
        print("No differences found between the two Fortran files.")
    else:
        output_diff(diff)



if __name__ == "__main__":
    main()
