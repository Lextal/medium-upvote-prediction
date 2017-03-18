from data_loader import DataLoader
from extraction import make_labels
from basic_transforms import *
from collections import defaultdict

import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Builds a list of words that occur at least N times in the dataset')
parser.add_argument('source_file', type=str, help='file with a dataset')
parser.add_argument('vocab_file', type=str, help='file to store the vocab')
parser.add_argument('--n', dest='min_count', type=int, default=100, help='Minimum number of occurencies, default: 100')
parser.add_argument('--top', dest='choose_top', type=int, default=-1, help='Change this to choose top N frequent words instead')
parser.add_argument('--ignore', dest='prefix', type=str, default=None, help='Words including this will be retained in any case')

args = parser.parse_args()

gen = DataLoader(args.source_file)
gen.add_transform(text_normalizer)
gen.add_transform(make_labels)
gen.add_transform(for_classifier)

counter = defaultdict(int)

for obj in tqdm(gen):
    text = obj
    for w in text.split():
        counter[w] += 1

wordcounts = sorted([x for x in counter.items()], key=lambda x: -x[1])

with open(args.vocab_file, 'w') as vocab:
    if args.choose_top != -1:
        n = 0
        for w in wordcounts:
            if args.prefix is not None or n < args.choose_top:
                check = args.prefix in w[0]
                if check or n < args.choose_top:
                    vocab.write(w[0] + '\n')
                    if not check:
                        n += 1
    else:
        for word, count in counter.items():
            if count >= args.min_count and (args.prefix is None or args.prefix != word[:len(args.prefix)]):
                vocab.write(word + '\n')
            if n == args.choose_top:
                break
