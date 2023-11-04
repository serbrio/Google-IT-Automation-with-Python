#!/usr/bin/env python3

import logging
import mylib


def main():
    logging.basicConfig(format='%(asctime)s||%(levelname)s||%(module)s|| %(message)s', filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')


if __name__ == '__main__':
    main()
