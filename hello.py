import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    'filename',
    # type=int,
    help='enter a filename to get insights'
)
parser.add_argument(
    '-wc',
    '--word-count',
    help='gives word count',
    action='store_true'
)
parser.add_argument(
    '-l',
    '--lines',
    help='gives line count',
    action='store_true'
)
parser.add_argument(
    '-v',
    '--verbose',
    help='increase output verbosity',
    action='store_true'
)
args = parser.parse_args()

f = open(args.filename, 'r')
text = f.read()


def word_count(txt):
    return len(txt.split(' '))

def lines(txt):
    return len(txt.split('\n'))

if args.word_count:
    print(word_count(text))

if args.lines:
    print(lines(text))
