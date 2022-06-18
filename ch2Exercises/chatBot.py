from nltk.chat.util import Chat, reflections

class Chatter:
    def __init__(self):
        self.pairs = [['my name is (.*)', ['hi %1']],
                      ['(hi|hello|hey there|hola|bonjour)',
                       ['hey there!', 'Hello!', 'Good day to you']],
                      ['The (.*) today is (.*)', ['Yes the %1 today is %2']],
                      ['who created you', ['Ethan created me using nltk']],
                      ['I want (.)', ['Then get %1']]]
        self.reflections = reflections
        
    def chat(self):
        chat = Chat(pairs=self.pairs, reflections=self.reflections)
        print('Hello, I am Ethans naive chatbot')
        chat.converse()
        
def main():
    chatBot = Chatter()
    chatBot.chat()
    
main()
