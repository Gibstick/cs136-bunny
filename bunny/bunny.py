__author__ = 'Charlie'

import envoy
from glob import glob
from collections import namedtuple

Test_result = namedtuple('Test_result',
                         'return_code, '
                         'test_file, '
                         'expected_data, '
                         'actual_data, '
                         'passed')


def run_test(program, in_file, out_file):
    '''
    Run one test, using input from in_file and comparing to output specified in out_file.

    :param program: Program to test (str)
    :param in_file: Input file to pipe to std.in (str)
    :param out_file: File containing correct output (str)
    :return: Test_result tuple
    '''
    with open(in_file, 'r') as f:
        input_data = f.read()

    with open(out_file, 'r') as f:
        output_data = f.read()

    test = envoy.run(program, data=input_data, timeout=30)
    result_data = test.std_out
    return Test_result(test.status_code, in_file, output_data, result_data,
                       result_data == output_data)


def get_test_files(test_dir, in_ext, out_ext):
    '''
    Get all test files in test_dir.

    :param test_dir: Path (str)
    :param in_ext: File extension for input files (str)
    :param out_ext: File extension for output files (str)
    :return: A tuple of two tuples, input files and output files
    '''
    return tuple(
        ((glob(test_dir + '/*' + in_ext)), (glob(test_dir + '/*' + out_ext))))


def run_all_tests(program, test_files):
    '''
    Run all tests

    :param program: Program to test (str)
    :param test_files: A tuple of in_files and out_files
    :return: Test_result tuple
    '''
    in_files, out_files = test_files

    for in_file, out_file in zip(in_files, out_files):
        result = run_test(program, in_file, out_file)
        if not result.return_code == 0:
            print('error: Process returned {} for {}'.format(result.return_code,
                                                             result.test_file))
        elif result.passed:
            print('passed {}'.format(result.test_file))
        else:
            print('failed: expected\n{}\nbut received\n{}'.format(
                result.expected_data, result.actual_data))


def main():
    import argparse

    # setup parser and parse
    parser = argparse.ArgumentParser()
    parser.add_argument('program', help='binary to test')
    parser.add_argument('-t', "--test-dir", metavar='path',
                        help='Path to test directory (default: tests)',
                        action='store')
    parser.add_argument('-i', '--input', metavar='ext',
                        help='File extension for input file (default: .in)')
    parser.add_argument('-o', '--output', metavar='ext',
                        help='File extension for output file (default: .expect)')
    args = parser.parse_args()

    # store parsed arguments
    test_dir = args.test_dir or 'tests'
    program = args.program
    in_ext = args.input or '.in'
    out_ext = args.output or '.expect'

    run_all_tests(program, get_test_files(test_dir, in_ext, out_ext))


if __name__ == "__main__":
    main()