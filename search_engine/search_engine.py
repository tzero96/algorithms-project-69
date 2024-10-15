import re

def search(lst, word):
    result = [d['id'] for d in lst if word in re.findall(r'\w+', d['text']) or word in d['text'].split()]
    return result
