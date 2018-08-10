# -*- coding: utf-8 -*-

import logging
import pprint
import sys
import mmap

from slacker import Slacker

from __init__ import __version__
from utils import Colors, Counter
from args import Args


# Get and parse command line arguments
args = Args()

# Nice slack API wrapper
slack = Slacker(args.token)

# So we can print slack's object beautifully
pp = pprint.PrettyPrinter(indent=4)

# Count how many items we deleted
counter = Counter()

# Initial logger
logger = logging.getLogger('slack-cleaner')
logger.setLevel(10)

# And always display on console
stderr_log_handler = logging.StreamHandler()
logger.addHandler(stderr_log_handler)

# Print version information
logger.info('Running slack-cleaner v' + __version__)


def delete_file(file):
    # Actually perform the task
    if args.perform:
        try:
            # No response is a good response
            slack.files.delete(file['id'])
        except:
            logger.error(Colors.YELLOW + 'Failed to delete ->' + Colors.ENDC)
            pp.pprint(file)
            return

        logger.warning(Colors.RED + 'Deleted file -> ' + Colors.ENDC
                       + file.get('title', ''))

    counter.increase()


def get_files():
    has_more = True
    listed = 0
    exit_loop = False
    while has_more:
        res = slack.files.list().body

        if not res['ok']:
            logger.error('Error occurred on Slack\'s API:')
            pp.pprint(res)
            sys.exit(1)

        files = res['files']
        current_page = res['paging']['page']
        total_pages = res['paging']['pages']
        has_more = current_page < total_pages

        with open(args.files_to_delete, 'w') as to_delete:
            for f in files:
                if listed == args.batch_size:
                    exit_loop = True
                    break
                else:
                    to_delete.write(f['id'] + " : " + f.get('title', '') + " : size=" + str(f.get('size')) + '\n')
                    logger.warning(Colors.YELLOW + 'Will delete file -> ' + Colors.ENDC
                                   + f.get('title', ''))
                    listed += 1

        if exit_loop:
            break


def remove_files():
    has_more = True
    deleted = 0
    exit_loop = False
    while has_more:
        res = slack.files.list().body

        if not res['ok']:
            logger.error('Error occurred on Slack\'s API:')
            pp.pprint(res)
            sys.exit(1)

        files = res['files']

        with open(args.files_to_delete, 'rb', 0) as file, \
                mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
            for f in files:
                if deleted == args.batch_size:
                    exit_loop = True
                    break

                elif s.find(str.encode(f['id'])) != -1:
                    delete_file(f)
                    deleted += 1

        if exit_loop:
            break


def main():
    if not args.perform:
        get_files()
    else:
        remove_files()

    if not args.perform:
        logger.info('Now you can re-run this program with `--perform`' +
                    ' to actually perform the task.' + '\n')


if __name__ == '__main__':
    main()
