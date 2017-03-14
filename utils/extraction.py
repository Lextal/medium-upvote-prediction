import re

def make_labels(obj, prefix='__rt*'):
    # extracts only tags, adding a prefix before them - used as label for
    # classification. Adds a list of labels to json object
    res = []
    for q in obj['tags']:
        res.append(prefix + re.sub(' ', '_', q['name']))
    obj['labels'] = res
    return obj
