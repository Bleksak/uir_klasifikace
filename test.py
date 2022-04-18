from cls import Class
from dialog import Dialog
from symptom import tf, tfidf

def idf_test():
    classes = set()
    cls = Class('TEST')
    classes.add(cls)

    d1 = Dialog('a quick brown fox jumps over the lazy dog. what a fox', cls)
    d2 = Dialog('a quick brown fox jumps over the lazy fox what a fox', cls)

    tf_idf = tfidf(classes, [d1, d2])



idf_test()