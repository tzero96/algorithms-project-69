import re

def search(lst, word):
    result = []
    for d in lst:
        token = d['text'].lower()
        term = re.findall(r'\w+', token)
        term_str = ''.join(term)
        if word in token.split() or word in term:
            result.append({'id': d['id'], 'count': len(re.findall(word, token))})
    result = [doc['id'] for doc in sorted(result, key=lambda d: d['count'], reverse=True)]
    return result
