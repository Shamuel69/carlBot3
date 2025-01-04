import re

def punct_grabber(sentence):
    word = ''

    for char in sentence:
        if char.isalnum():
            word+= char
        else:
            if char in [".", "!", "?"]:
                word+="[punct]"
            word+="_"
    
    return word


class tokenizer():
    def __init__(self, text):
        self.unspaced_text = text
        self.spaced_text = text.split()
        self.look_for_punctuation = [".", "?", "!"]


    def calc_punctuations(self):
        basematrix = []
        for i in [".", "?", "!"]:
            try:
                self.unspaced_text.index(i)
                basematrix.append(i)
            except ValueError:
                pass
        return basematrix

    def sentence_identifier(self):
        possible_text = []#if it thinks the text needs change then append it to the list
        pulled_punctuation = self.calc_punctuations()
        for i, text in enumerate(self.spaced_text):
            for punct in pulled_punctuation:
                try:
                    if text.index(punct):
                         values = (text, i, punct)
                         possible_text.append(values)
                except ValueError:
                    pass
        
        adjusted_text = ""

        for iter, data_gathered in enumerate(possible_text):
            word =  data_gathered[0]
            punct = data_gathered[0][-1]
            counted = word.count(punct)
            
            unajusted_text = self.unspaced_text.find(word)
            print(unajusted_text)
            
            if counted > 2:
                if iter > 0:
                    adjusted_text += self.unspaced_text[:data_gathered[1]]

            print(adjusted_text)
        
        return possible_text

            

if __name__ == "__main__":
    # print(tokenizer("The hairy dog's head just does that bro. i dont know what else to say man... UHHHH DOO DOO DEE DA? who the fuck are you? AND WHY DO YOU HAVE A GUN!!!!").sentence_identifier())
    print(punct_grabber("The hairy dog's head just does that bro. i dont know what else to say man... UHHHH DOO DOO DEE DA? who the fuck are you? AND WHY DO YOU HAVE A GUN!!!!"))