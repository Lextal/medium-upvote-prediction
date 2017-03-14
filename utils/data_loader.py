import json
from basic_transforms import *
from extraction import *

import sys

class DataLoader(object):

    def __init__(self, file_path):
        self.transforms = []
        self.file_path = file_path

    def __iter__(self):
        for line in open(self.file_path):
            obj = json.loads(line)
            for t in self.transforms:
                obj = t(obj)
            yield obj


    def add_transform(self, transform):
        """
            A transform should be a lambda function
        """
        self.transforms.append(transform)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python {} <file_path>'.format(sys.argv[0]))
        quit()
    path = sys.argv[1]
    loader = DataLoader(path)
    loader.add_transform(text_normalizer)
    loader.add_transform(make_labels)
    loader.add_transform(for_classifier)

    for doc in loader:
        print(doc)
