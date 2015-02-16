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
    import argparse

    # setup parser and parse
    parser = argparse.ArgumentParser()
    parser.add_argument('program', help='binary to test')
    parser.add_argument('-t', "--test-dir", metavar='path', help='Path to test directory (default: tests)',
                        action='store')
    parser.add_argument('-i', '--input', metavar='ext', help='File extension for input file (default: .in)')
    parser.add_argument('-o', '--output', metavar='ext', help='File extension for output file (default: .expect')
    args = parser.parse_args()

    # store parsed arguments
    test_dir = args.test_dir or 'tests'
    program = args.program
    in_ext = args.input or '.in'
    out_ext = args.output or '.expect'

    in_files = tuple((glob(test_dir + '/*' + in_ext)))
    out_files = tuple((glob(test_dir + '/*' + out_ext)))

    results = map(lambda x, y: run_test(program, x, y), in_files, out_files)

    print("Testing...")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()