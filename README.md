# slack-cleaner

Bulk delete files on Slack.

## Install

Download package then install `slacker` through the command:

`pip install slacker`

## Usage

```bash

# Switch into the slack_cleaner folder from the base of the project
cd slack_cleaner

# Write all files on slack server to file. Does not delete files.
# Delete file names from the given file that you want to keep.
python cli.py --token <TOKEN> -f <FILE_TO_WRITE>

# Delete files contained in the given file in previous command.
python cli.py --token <TOKEN> -f <FILE_TO_WRITE> --perform

## Get information about the program
python cli.py --help

```

Generate tokens with the following link: https://api.slack.com/custom-integrations/legacy-tokens
