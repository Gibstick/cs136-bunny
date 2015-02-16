__author__ = 'Charlie'

import envoy
from glob import glob

def run_test(program, in_file, out_file):
    with open(in_file, 'r') as f:
      input_data = f.read()

    with open(out_file, 'r') as f:
      output_data = f.read()


    test = envoy.run(program, data=input_data, timeout=30)
    result_data = test.std_out
    if not test.status_code == 0:
        return 'error: process returned ' + str(test.status_code)
    if result_data == output_data:
        return 'passed ' + in_file
    else:
        return 'failed: expected\n' + output_data + '\nreceived:\n' + result_data

def main():
    import sys
    import argparse

    if not len(sys.argv) == 2:
        print('Usage: bunny <program to test>')
        sys.exit()

    program = sys.argv[1]

    IN_EXT = '.in'
    OUT_EXT = '.expect'

    in_files = tuple((glob('tests/*' + IN_EXT)))
    out_files = tuple((glob('tests/*' + OUT_EXT)))

    results = map(lambda x, y: run_test(program, x, y), in_files, out_files)
    print("Testing...")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()