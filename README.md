# cs136-bunny
Automatically perform I/O tests on a program. By default, it looks for .in files in ./tests and uses that as keyboard input for the program, comparing it to .expect files in ./tests. Tailored for CS 136, Winter 2015.

## Installation
```
pip install cs136-bunny.zip
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
## License


The MIT License (MIT)

Copyright (c) 2015 Shijian (Charlie) Wang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

