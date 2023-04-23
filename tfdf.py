import math
import time
from nltk.corpus import reuters, inaugural, gutenberg


class Search:
    corpus = gutenberg


    def __init__(self):
        # self.index = self.inverse_index()
        self.df_dict = self.df()
        self.tf_dict = self.tf()
        self.tf_idf_dict = self.tf_idf()
        return

    # dictionary for w
    def inverse_index(self):
        index = {}
        for id_doc in self.corpus.fileids():
            for word in self.corpus.words(id_doc):
                if word not in index:
                    index[word] = set()
                index[word].add(id_doc)
        return index

    def tf(self):
        tf_dict = {}
        for doc_id in self.corpus.fileids():
            tf_dict[doc_id] = dict()
            for word in self.corpus.words(doc_id):
                if word.lower() in tf_dict[doc_id]:
                    tf_dict[doc_id][word.lower()] += 1
                else:
                    tf_dict[doc_id][word.lower()] = 1
        return tf_dict

    def df(self):

        df_dict = {}
        for doc_id in self.corpus.fileids():
            for word in {word.lower() for word in set(self.corpus.words(doc_id))}:
                if word.lower() in df_dict:
                    df_dict[word.lower()] += 1
                else:
                    df_dict[word.lower()] = 1
        print('df finished')
        return df_dict

    def tf_idf(self):
        def idf(self, term):
            if self.df_dict[term.lower()] > len(self.corpus.fileids()):
                print(term, self.df_dict[term.lower()])
            return math.log(len(self.corpus.fileids()) / self.df_dict[term.lower()])
        tf_idf_dict = dict(self.tf_dict)
        for doc in self.tf_dict:
            tf_idf_dict[doc] = dict()
            for word in self.tf_dict[doc]:
                tmp = idf(self,word)
                tf_idf_dict[doc][word.lower()] = self.tf_dict[doc][word.lower()]*tmp
        print('tf-idf finished')

        return tf_idf_dict

    # query is a list of words that comprises search terms
    def doc_score(self, query, doc_id):
        score = 0
        for term in query:
            if term.lower() in self.tf_idf_dict[doc_id]:
                score += self.tf_idf_dict[doc_id][term.lower()]
        return score

    def query_result(self, query):

        result = list()
        for doc_id in self.corpus.fileids():
            result.append((doc_id, self.doc_score(query, doc_id)))
        return sorted(result, key = lambda x:x[1], reverse=True)







