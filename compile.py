#!/usr/bin/env python
import os
from pathlib import Path
from argparse import ArgumentParser
from subprocess import run, PIPE


def compile(files):
    root_dir = Path(__file__).resolve().parent
    project_dir = root_dir / 'specifications'
    os.chdir(project_dir)
    cmd = ['pdflatex', '-jobname=specifications',
           '-output-directory={}'.format(str(root_dir))] + files
    try:
        run(cmd)
    except FileNotFoundError:
        print('You need to install pdfLaTeX to compile the project.')
        exit(1)

def main():
    p = ArgumentParser(description='Compile the project')
    p.add_argument('file',
                   nargs='*',
                   default='main',
                   help=("The .tex file to compile, without the extension "
                         "(default: %(default)s)"))
    args = p.parse_args()

    if isinstance(args.file, str):
        files = ['{}.tex'.format(args.file)]
    else:
        files = ['{}.tex'.format(f) for f in args.file]

    compile(files)


if __name__ == '__main__':
    main()
