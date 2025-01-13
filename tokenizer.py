
###The Tokenizer to my AI###
#===========================#

class tokenizer():
    def __init__(self, text):
        self.unspaced_text = text
        self.spaced_text = text.split()
        self.look_for_punctuation = [".", "?", "!"]

    


    def find_contraction(self, word):
        con_dict = {"contractions": ["'s", "'m", "'ve", "'ll", "'re", "'d"], "replacing": "n't"}
        for i in con_dict.keys():
            for item in con_dict[i]:
                if word.endswith(item) and "'" in word:
                    print(f"found item {item} in {word}  |  {word} {item}")
                    break
        
        return ([word[:word.find(item)], item], True)
            
    def calc_punctuations(self):
        
        base_tokenizer = []
        punct_count = lambda words, puncts: list(words).count(puncts)
        for word in self.spaced_text:
            con_or_not = False
            if self.find_contraction(word):
                base_tokenizer.extend(self.find_contraction(word)[0])

            for punct in self.look_for_punctuation:
                if punct_count(word, punct) >= 3:
                    base_tokenizer.extend([word.strip(punct), f"{punct}{punct}{punct}"]) 
                    con_or_not = True
                    continue
            if not con_or_not:
                
                base_tokenizer.append(word)
        return base_tokenizer
        # basematrix = []
        # for i, word in enumerate(self.spaced_text):
        #     word = word
        #     for punct in self.look_for_punctuation:
        #         char_loc = word.find(punct)
        #         if char_loc>0:
        #             last_num = 0
        #             times_found = 0
        #             for iter, char in enumerate(word):
        #                 if char == punct:
        #                     if iter-last_num == 1:
        #                         times_found += 1
        #                         last_num = iter
        #                         if times_found >= 3:
        #                             if punct == ".":
        #                                 basematrix.extend([word.strip(word[iter:]), f"[ex-]"]) 
                                    

        #                             print(word)
        #                         continue

        #                     times_found += 1
        #                     last_num = iter
        #     basematrix.append(word)
                    # punct_count = Counter(char for char in word if char == punct)

                    # print(punct_count)
                    # basematrix.append([punct, i])
                
        

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
    print(tokenizer("The hairy dog's head just does that bro. i dont know what else to say man... UHHHH DOO DOO DEE DA? who the fuck are you? AND WHY DO YOU HAVE A GUN!!!!").calc_punctuations())


    