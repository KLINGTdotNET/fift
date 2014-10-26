#!/usr/bin/env python3

import argparse
from os import path, walk

def main():
    args = _get_args()
    if path.exists(args.path):
        exts = _get_exts(args.path)
        for ext in sorted(exts):
            print(ext)
    else:
        print('this path "{}" does not exist'.format(args.path))
        exit(1)

def _get_exts(root):
    extensions = []
    for _, _, files in walk(root):
        for f in files:
            _, ext = path.splitext(f)
            if ext not in extensions:
                extensions.append(ext)
    return extensions


def _get_args():
    parser = argparse.ArgumentParser(description='Get all the different file extension contained in a directory tree')
    parser.add_argument('path', help='root path of the directory tree, f.e. /home/someone/Music')
    return parser.parse_args()

if __name__ == '__main__':
    main()
