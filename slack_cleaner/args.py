# -*- coding: utf-8 -*-

import argparse


class Args():
    def __init__(self):
        p = argparse.ArgumentParser(prog='slack-cleaner')

        # Token
        p.add_argument('--token', required=True,
                       help='Slack API token (https://api.slack.com/web)')

        # Perform or not
        p.add_argument('--perform', action='store_true',
                       help='Perform the task')

        p.add_argument('--file', '-f', type=str, required=True,
                       help='File to write and read files that are to be deleted')

        args = p.parse_args()

        self.token = args.token

        self.perform = args.perform

        self.files_to_delete = args.file
