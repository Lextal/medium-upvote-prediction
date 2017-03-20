from argparse import ArgumentParser
import numpy.random as rnd
from tqdm import tqdm
import numpy as np

def cut_tags(text, prefix='__rt*'):
    return ' '.join([w for w in text.strip().split() if prefix not in w and w != '\n'])

def linecount(path):
    n = 0
    for line in open(path):
        n += 1
    return n

def index(ratio, n):
    rnd.seed(12321)
    m = int(np.round(ratio * n))
    index = np.zeros(n)
    retaining_ind = rnd.choice(np.arange(n), m)
    index[retaining_ind] = 1
    index = (index == True)
    return index.astype('int').tolist()


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('source_file', type=str)
    parser.add_argument('--prefix', type=str, default='__rt*', help='words containing this substring are considered to be labels')
    parser.add_argument('--ratio', type=float, default=0.1, help='float, percentage of documents that should retain their labels')
    parser.add_argument('--skip-unsup', action='store_true')

    args = parser.parse_args()

    n = linecount(args.source_file)
    index = index(args.ratio, n)

    with open(args.source_file) as f:
        for i in tqdm(range(n)):
            line = f.readline()
            if index[i]:
                print(line.strip())
            else:
                if not args.skip_unsup:
                    print(cut_tags(line))
