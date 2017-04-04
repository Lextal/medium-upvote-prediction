from collections import defaultdict
from argparse import ArgumentParser
from tqdm import tqdm

def global_word_counts(data_src, min_count=10, prefix='__rt*'):
    wc = defaultdict(int)
    for line in tqdm(open(data_src)):
        for w in line.strip().split():
            wc[w] += 1
    wc_filt = {}
    for k in wc:
        if wc[k] >= min_count and (prefix not in k):
            wc_filt[k] = wc[k]
    return wc_filt

def rarest_words_doc(doc, wc, k=10, prefix='__rt*'):
    words = [w for w in doc.strip().split() if prefix not in w]
    _words = list(set(words))
    labels = sorted([w for w in _words if w in wc], key=lambda w:wc[w])[:k]
    words = [w for w in words if w not in labels]
    labels = [prefix + x for x in labels]
    return ' '.join(labels) + ' ' + ' '.join(words)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('source_file', type=str)
    parser.add_argument('--min_count', type=int, default=10)
    parser.add_argument('--labels', type=int, default=10)

    args = parser.parse_args()
    src = args.source_file
    min_count = args.min_count
    k = args.labels
    wc = global_word_counts(src, min_count)
    for line in tqdm(open(src)):
        print(rarest_words_doc(line, wc, k))
