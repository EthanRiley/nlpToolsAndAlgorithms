#import nltk
#nltk.download('punkt')
from nltk.tokenize import word_tokenize
from collections import Counter, defaultdict

class ngrams:
    
    def findUnsmoothUnigram(corpus):
        words = [x.lower() for x in word_tokenize(corpus)]
        length = len(words)
        
        unigramDict = Counter(words)
        unigramProbabilityDict = unigramDict.copy()
        unigramProbabilityDict.update( y / length for x, y in unigramDict.items())
        return unigramProbabilityDict
    
    def findUnsmoothBigram(corpus):
        pass