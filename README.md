# slack-cleaner

Bulk delete files on Slack.

## Requirements
Python 3, pip3 and Slacker (a python package)

## Install

Download package then install `slacker` through the command:

`pip3 install slacker`

## Usage

```bash

# Write all files on slack server to file. Does not delete files.
# Delete file names from the given file that you want to keep.
python3 cli.py --token <TOKEN> -f <FILE_TO_WRITE>

# Delete files contained in the given file in previous command.
python3 cli.py --token <TOKEN> -f <FILE_TO_WRITE> --perform

## Get information about the program
python3 cli.py --help

```

Generate tokens with the following link: https://api.slack.com/custom-integrations/legacy-tokens
