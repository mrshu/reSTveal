"""reSTveal

Usage:
  restveal <file> <directory>
  restveal (-h | --help)
  restveal --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt


def main():
    arguments = docopt(__doc__, version='reSTveal 0.1')
    print(arguments)

if __name__ == "__main__":
    main()
