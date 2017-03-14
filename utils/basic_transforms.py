import re

def text_normalizer(obj):
    text = obj['text']
    text = text.lower()

    def add_spaces(group):
        return ' ' + group + ' '

    obj['text'] = re.sub('[^a-z^0-9^ ]', lambda x: add_spaces(x.group()), text)
    obj['text'] = re.sub('\s+', ' ', obj['text'])
    return obj

def for_classifier(obj):
    s = ''
    if 'labels' in obj:
        s += ' '.join(obj['labels'])
        s += '\t'
    s += obj['text']
    return s
