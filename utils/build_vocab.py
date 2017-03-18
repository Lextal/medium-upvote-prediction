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

def check_eligibility(word, count, n):
    if str(args.prefix) in word:
        return True, n
    if args.choose_top != -1:
        return n < args.choose_top, n + 1
    else:
        return count >= args.min_count, n + 1

with open(args.vocab_file, 'w') as vocab:
    n = 0
    for word, count in wordcounts:
        check, n_ = check_eligibility(word, count, n)
        if check:
            vocab.write(word + '\n')
            n = n_
