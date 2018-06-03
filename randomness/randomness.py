#!/usr/bin/env python3

"""Generates random secrets (passwords, etc)."""

import argparse
import math
from random import SystemRandom

import pkg_resources


RANDOM = SystemRandom()


def sgr(*args):
    """Creates a Select Graphic Rendition escape sequence. See
    https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters.
    """
    return '\x1b[{}m'.format(';'.join(str(i) for i in args))


def get_resource(name):
    """Convenience method for retrieving a package resource."""
    return pkg_resources.resource_stream(__name__, name)


def set_from_file(file):
    """Creates a set from a newline-delimited word file."""
    return [word.decode().strip() for word in file.readlines()]


SETS = dict(
    alphanum='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
    lowernum='0123456789abcdefghijklmnopqrstuvwxyz',
    uppernum='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    base58='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
    diceware=set_from_file(get_resource('diceware.txt')),
    eff5=set_from_file(get_resource('eff5.txt')),
    eff4=set_from_file(get_resource('eff4.txt')),
    effshort=set_from_file(get_resource('effshort.txt')),
)


def main():
    """The main function."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--length', type=int, default=8,
        help='the number of random items to generate')
    parser.add_argument(
        '--num', type=int, default=5,
        help='the number of random sequences to generate')
    parser.add_argument(
        '--sep', default='',
        help='the string to separate items with')
    parser.add_argument(
        '--set', choices=SETS.keys(), default='alphanum',
        help='the set of items to use')
    args = parser.parse_args()

    bits = math.log2(len(SETS[args.set])) * args.length
    print(f'{sgr(1)}Random bits per sequence{sgr(0)}: {bits:.01f}')

    for _ in range(args.num):
        items = RANDOM.choices(SETS[args.set], k=args.length)
        output = args.sep.join(items)
        print(output)


if __name__ == '__main__':
    main()
