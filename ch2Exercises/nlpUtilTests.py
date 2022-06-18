from nlpUtil import nlpUtil

def minEditDistanceTest(source, target, answer):
    result = nlpUtil.minEditDistance(source, target)
    assert result == answer, f'Something went wrong. Answer should be {answer}'
    
def testEditAlgorithms():
    try:
        sources = ['dog', 'dog', 'leda', 'drive', 'drive', 'drivers']
        targets = ['dog', 'bot', 'deal', 'brief', 'drivers', 'drive']
        results = [0, 2, 3, ]
        for i in range(len(sources)):
            minEditDistanceTest(sources[i], targets[i], results[i])
    except:
        print("Something went wrong")

def main():
    testEditAlgorithms()

main()