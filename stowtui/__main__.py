import sys
import os

from stowtui.stowApp import StowApp


def main():
    StowTui = StowApp()
    StowTui.run()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os.system('reset')
        os.system('stty sane')
        try:
            sys.exit(0)
        except SystemExit:    # pragma: no cover
            os._exit(0)
