import re

def text_normalizer(obj):
    text = obj['text']
    text = text.lower()

    def add_spaces(group):
        return ' ' + group + ' '

    obj['text'] = re.sub('[^a-z^0-9^ ]', lambda x: add_spaces(x.group()), text)
    return obj

