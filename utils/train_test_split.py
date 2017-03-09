import sys

def splitter(data_src, train_out, test_out, index_path):
    """
        data_src: path to medium.json
        train_out: path to store a file of the same structure as medium.json
        test_out: same
        index_path: a file with space-separated line of 0 and 1
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
                    else:
                        test.write(buf)

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Not enough args. Syntax: python {} <data src> <train_out> <test_out> <index_file>'.format(sys.argv[0]))
        quit()
    splitter(*sys.argv[1:5])
