# NOAA-GSL

## **Coding Challenge**

Instructions:
Given the two sample namelist fortran files in this repo, please write a Python based tool that gives a user a command line interface that takes file paths as input and provides a report on the differences between the two files as output. For context, Fortran doesn't care about section/key order, so it's often difficult for users to track down differences in values that two researchers may have prepared independently. 


## **Getting Started with `f90nml` (A Python module for Fortran namelists)**

The latest documentation for `f90nml` can be found at https://f90nml.readthedocs.io/en/latest/

### **Installation**

```
$ pip install f90nml
```

### **Set Up**

Clone the repository

```
$ git clone https://github.com/nbharwani11/NOAA-GSL.git
```


## **Executing the Code**

Once you have cloned the repository and have installed f90nml perform the following operations:

```
$ cd src
```

```
$ python compare_nml_files.py insert_filepath_nml_1 insert_filepath_nml_2

or

$ ./compare_nml_files.py insert_filepath_nml_1 insert_filepath_nml_2
```

## **Running pytest**

I mainly followed the tutorial listed [here](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)

Following their guidelines perform the operations below:

```
$ mkdir pytest_project
$ cd pytest_project
$ python3 -m venv pytest-env
$ source pytest-env/bin/activate
$ pip install pytest
```

Now execute the pytest command ```$ pytest``` to run the tests

- Be sure to follow the styling guidelines in the link provided 
(i.e. Pytest expects our tests to be located in files whose names begin with test_ or end with _test.py)


## **Sources**

Below are my sources that I used to complete the coding challenge

- https://github.com/marshallward/f90nml
- https://f90nml.readthedocs.io/en/latest/
- https://sites.google.com/colorado.edu/fall-2022-software-developer/home
- https://realpython.com/pytest-python-testing/
- https://www.tutorialsteacher.com/python/os-module#:~:text=The%20OS%20module%20in%20Python,with%20the%20underlying%20operating%20system.
- https://docs.python.org/3/library/argparse.html#:~:text=The%20argparse%20module%20makes%20it,generates%20help%20and%20usage%20messages.
- https://www.knowledgehut.com/blog/programming/self-variabe-python-examples
- https://vim.rtorr.com/
- https://realpython.com/command-line-interfaces-python-argparse/
- https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser
- https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument
- https://docs.python.org/3/library/argparse.html?highlight=argparse#argparse.ArgumentParser.parse_args
- https://favtutor.com/blogs/empty-dictionary-python#:~:text=The%20%E2%80%9Cif%20condition%E2%80%9D%20can%20be,%3B%20otherwise%2C%20it%20returns%20false.
- https://www.simplilearn.com/tutorials/python-tutorial/python-sets-and-dictionaries
- https://www.w3schools.com/python/ref_dictionary_get.asp
- https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
