import re



class tokenizer():
    def __init__(self, text):
        self.unspaced_text = text
        self.spaced_text = text.split()
        self.look_for_punctuation = [".", "?", "!"]


    def calc_punctuations(self):
        basematrix = []
        for i in [".", "?", "!"]:
            identified = [b for b, c in enumerate(self.unspaced_text) if c == i]
            basematrix.append(identified)
            yield identified
        print(f"output: {basematrix}")

    def sentence_identifier(self):
        possible_text = []#if it thinks the text needs change then append it to the list
        
        for i, text in enumerate(self.spaced_text):
            for punct in [".", "?", "!"]:
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
    print(tokenizer("The hairy dog's head just does that bro. i dont know what else to say man... UHHHH DOO DOO DEE DA? who the fuck are you? AND WHY DO YOU HAVE A GUN!!!!").sentence_identifier())