import re

def search(lst, words):
    result = []
    words_set = set(words.split())
    index = {}
    for d in lst:
        token = d['text'].lower()
        term = re.findall(r'\w+', token)
        #term_str = ''.join(term)
        for word in term:
            _index = index.setdefault(word, [])
            _index.append(d['id'])
        occurr_number = words_set.intersection(set(term) | set(token.split()))
        if occurr_number:
            result.append({'id': d['id'], 'occurr_number': len(occurr_number),'count': sum(i in words_set for i in term)})
    result = [doc['id'] for doc in sorted(result, key=lambda d: (d['occurr_number'], d['count']), reverse=True)]
    return result
