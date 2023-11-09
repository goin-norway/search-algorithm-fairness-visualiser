import pyterrier as pt
import ir_datasets
import pandas as pd
import math
from pyterrier.measures import *

def hello_world():
    if not pt.started():
        pt.init()
    dataset = pt.get_dataset('irds:cranfield')
    index_ref = pt.IndexRef.of('C:\\Users\\cockb\\Downloads\\indices\\cranfield') # assumes you have already built an index

    docs = pd.DataFrame(ir_datasets.load("cranfield").docs_iter());
    docs = docs[docs['author'].str.startswith('a')];
    docs["doc_id"] = pd.to_numeric(docs["doc_id"])

    tfidf = pt.BatchRetrieve(index_ref, wmodel="TF_IDF")
    bm25 = pt.BatchRetrieve(index_ref, wmodel="BM25")

    authors_beginning_with_a = pt.apply.generic(lambda res: res[res["docid"].isin(docs["doc_id"])])

    results = pt.Experiment(
        [tfidf, tfidf >> authors_beginning_with_a],
        dataset.get_topics(),
        dataset.get_qrels(),
        ["map", nDCG@20]
    )

    return 1 - results["map"][0] - results["map"][1]