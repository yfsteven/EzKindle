#!/usr/bin/env python3
import argparse
import pathlib
from ezkindle import send_to_kindle, extract_clippings

parser = argparse.ArgumentParser(prog='EzKindle',
                                description='EzKindle allows you to send ebooks to your kindle and extract clippings txt to make anki cards')
parser.add_argument("-s", "--send", nargs=1, metavar=('BOOK'),
                    help="send book file to kindle")
parser.add_argument("-e", "--extract", nargs=1, metavar=('CLIPPINGS'),
                    help="extract words from clippings file and make flashcards to be sent to your anki deck")

args = parser.parse_args()

if args.send:
    send_to_kindle(args.send[0])
elif args.extract:
    extract_clippings(args.extract[0])
