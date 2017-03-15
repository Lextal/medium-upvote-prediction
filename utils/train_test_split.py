import sys

import json
import numpy.random as rnd
import numpy as np

class DataIter(object):

    def __init__(self, data_src):
        self.data_src = data_src

    def __iter__(self):
        for line in open(self.data_src):
            yield json.loads(line)

def filter_data(data_src, index_path, n_train):
    """
        Filters the documents, eliminating those with no text/no tags
        Generates a split index where there's at least n_train samples for a train set
        Writes the index to index_path
    """
    valid = []
    total = 0
    for i, doc in enumerate(DataIter(data_src)):
        if len(doc['text'].split()) > 0 and len(doc['tags']) > 0:
            valid.append(i)
        total += 1
    print('{} documents out of {} after filtering'.format(len(valid), total))
    index = np.zeros(total) - 1
    valid = np.array(valid)
    index[valid] = 1
    for i in rnd.choice(np.where(valid)[0], n_train, replace=False):
        index[i] = 0
    with open(index_path, 'w') as f:
        f.write(' '.join([str(x) for x in index.astype('int')]) + '\n')


def splitter(data_src, train_out, test_out, index_path):
    """
        data_src: path to medium.json
        train_out: path to store a file of the same structure as medium.json
        test_out: same
        index_path: a file with space-separated line of -1, 0, 1
        -1 means discard, 0 means train, 1 means test
    """
    # we consider 0 as train sample and 1 as test sample
    with open(index_path) as idx:
        index = [int(x) for x in idx.readline().strip().split()]
    with open(data_src) as f:
        with open(train_out, 'w') as train:
            with open(test_out, 'w') as test:
                for i, ind in enumerate(index):
                    buf = f.readline()
                    if buf is None:
                        return
                    if ind == 0:
                        train.write(buf)
                    elif ind == 1:
                        test.write(buf)
                    else:
                        pass

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Not enough args. Syntax: python {} <data src> <train_out> <test_out> <index_file>'.format(sys.argv[0]))
        quit()
    rnd.seed(1337) # for reproducibility
    print('Building index...')
    filter_data(sys.argv[1], sys.argv[4], 1200000)
    print('Writing the data...')
    splitter(*sys.argv[1:5])
