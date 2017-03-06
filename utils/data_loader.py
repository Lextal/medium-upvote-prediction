import json

class DataLoader(object):

    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.transforms = []

    def __iter__(self):
        for line in open(self.data_dir + '/medium.json'):
            obj = json.loads(line)
            for t in self.transforms:
                obj = t(obj)
            yield obj


    def add_transform(self, transform):
        """
            A transform should be a lambda function
        """
        self.transforms.append(transform)
