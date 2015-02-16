# cs136-bunny
Automatically perform I/O tests on a program. By default, it looks for .in files in ./tests and uses that as keyboard input for the program, comparing it to .expect files in ./tests. Tailored for CS 136, Winter 2015.

## Installation
```
pip install bunny.zip
```

## Usage
```
usage: bunny.py [-h] [-t path] [-i ext] [-o ext] program

positional arguments:
  program               binary to test

optional arguments:
  -h, --help            show this help message and exit
  -t path, --test-dir path
                        Path to test directory (default: tests)
  -i ext, --input ext   File extension for input file (default: .in)
  -o ext, --output ext  File extension for output file (default: .expect
```