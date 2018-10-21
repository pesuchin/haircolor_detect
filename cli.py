from src.core.engine import Engine
import argparse


def set_argparser():
    parser = argparse.ArgumentParser(
        description='This script is hair color detector.'
        )
    parser.add_argument('folder_path',
                        action='store',
                        nargs=None,
                        const=None,
                        default=None,
                        type=str,
                        choices=None,
                        help='Directory path where image files are located.',
                        metavar=None)
    parser.add_argument('--debug',
                        action='store_true',
                        default=False,
                        help='debug mode if this flag is set (default: False)')
    args = parser.parse_args()
    return args


def main():
    args = set_argparser()
    eng = Engine(args)
    eng.run()


if __name__ == '__main__':
    main()
