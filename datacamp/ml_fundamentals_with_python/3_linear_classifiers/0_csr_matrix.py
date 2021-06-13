import numpy as np 
from scipy.sparse import csr_matrix 

def example_contructor(): 
    m1 = csr_matrix((3, 4), dtype=np.int8).toarray()
    print(m1)


def build_term_document_matrix(): 
    docs = [["hello", "world", "hello"], ["goodbye", "cruel", "world"]]
    indptr = [0]
    indices = []
    data = []
    vocabulary = {}
    for d in docs:
        for term in d:
            index = vocabulary.setdefault(term, len(vocabulary))
            indices.append(index)
            data.append(1)
        indptr.append(len(indices))

    a1 = csr_matrix((data, indices, indptr), dtype=int).toarray()
    print("vocabulary", vocabulary)
    print("documents", docs)
    print("term_doc_matrix")
    print(a1)


#example_contructor()
build_term_document_matrix()
