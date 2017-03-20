from argparse import ArgumentParser

from tqdm import tqdm

def cut_tags(text, prefix='__rt*'):
    return ' '.join([w for w in text.split() if prefix not in w])


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('source_file', type=str)
    parser.add_argument('--prefix', type=str, default='__rt*', help='words containing this substring are considered to be labels')

    args = parser.parse_args()

    with open(args.source_file) as f:
        for line in tqdm(f):
            print(cut_tags(line))
