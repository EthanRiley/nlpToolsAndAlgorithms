from ngrams import ngrams

def testUnsmoothUnigram(corpus, results):
    print(ngrams.findUnsmoothUnigram(corpus))
    

def testUnsmoothBigram(corpus, results):
    pass

#testUnsmoothUnigram(corpus="Sam I am, I am Sam. I do not like green eggs and ham.", results='Ur mom')
print(ngrams.findUnsmoothUnigram('Sam I am, I am Sam. I do not like green eggs and ham.'))