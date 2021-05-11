#!/usr/bin/env python

import argparse

import Solutions as S

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--problem', action='store', type=int, help='(optional) specify problem number <1...{}>'.format(len(S.solutions)))
parser.add_argument('-i', '--input', action='store', type=str, help='(optional) specify override input')

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
