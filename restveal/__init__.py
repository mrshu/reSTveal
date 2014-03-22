"""reSTveal

Usage:
  restveal <file> <directory>
  naval_fate.py (-h | --help)
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt


def main():
    arguments = docopt(__doc__, version='reSTveal 0.1')
    print(arguments)
