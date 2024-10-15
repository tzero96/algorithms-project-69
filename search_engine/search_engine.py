def search(lst, word):
    result = [d['id'] for d in lst if word in set(d['text'].split())]
    return result
