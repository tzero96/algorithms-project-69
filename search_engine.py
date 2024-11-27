import re

def search(lst_docs, words):
    term_words = re.findall(r"'?\b[0-9A-Za-z']+\b", words.lower())
    def compute_inverted_index(docs):
        inv_index = {}
        for doc in docs:
            token = doc['text'].lower()
            term = re.findall(r"'?\b[0-9A-Za-z']+\b", token)
            for word in term:
                if word not in inv_index:
                    inv_index[word] = set()
                inv_index[word].add(doc['id'])
        return inv_index

    def compute_idf(inverted_index, num_docs, term_words_):
        idf = {}
        for word in term_words_:
            idf[word] = log10(num_docs / len(inverted_index[word]))
        return idf

    def compute_tf_idf(docs, term_words_, idf):
        tf_idf = []
        for doc in docs:
            token = doc['text'].lower()
            term = re.findall(r"'?\b[0-9A-Za-z']+\b", token)
            doc_tf_idf = {"doc_id": doc['id'],"tf_idf": sum([(term.count(word)/len(term))*idf[word] for word in term_words_])}
            tf_idf.append(doc_tf_idf)
        return tf_idf

    inv_index = compute_inverted_index(lst_docs)
    idf = compute_idf(inv_index, len(lst_docs), term_words)
    tf_idf = compute_tf_idf(docs, term_words, idf)
    result = [d['doc_id'] for d in sorted(tf_idf, key=lambda d: d['tf_idf'], reverse=True) if d['tf_idf'] != 0]
    
    return result
