#!/usr/bin/env python

import argparse

import Solutions as S

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--problem', action='store', type=int, help='specify problem number <1...')
parser.add_argument('-i', '--input', action='store', type=str, help='specify override input file')

args = parser.parse_args()


def main():
    if args.problem is None:
        for p in S.solutions:
            print("problem {}: {}".format(p, S.solutions[p]()))
    else:
        print("problem {}: {}".format(args.problem, S.solutions[args.problem]()))
    return 0


if __name__ == '__main__':
    main()
