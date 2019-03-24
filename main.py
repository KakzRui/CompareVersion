import argparse
from compare_version import compare


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-v1', help='version 1')
        parser.add_argument('-v2', help='version 2')
        args = parser.parse_args()
        print(compare(args.v1, args.v2))
    except Exception:
        raise parser.error('Invalid arguments')


if __name__ == '__main__':
    main()
