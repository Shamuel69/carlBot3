import json
import os
import pickle
#to import data from, JSON file

class Data:
    def __init__(self, folder_PATH: str):
        self.binary_set = 0
        try:
            self.file_list = os.listdir(rf"{folder_PATH}")
        except:
            self.file_list = []
        self.PATH = folder_PATH
        

    def retrieve(self, is_folder=False, bin_set=False):
        data = []
        if is_folder is True:
            if bin_set:
                for item in self.file_list:
                    with open(f"{self.PATH}/{item}", "rb") as read_file:
                        data.append(pickle.load(read_file))
                return data
            for item in self.file_list:
                with open(f"{self.PATH}/{item}", "r") as read_file:
                    data.append(read_file)
            return data
        
        if bin_set:
            with open(f"{self.PATH}", "rb") as read_file:
                return pickle.load(read_file)
            
        with open(f"{self.PATH}", "r") as read_file:
            return read_file      


    #write inputed data into a file in binary

    def push_data(self, data, is_folder=True):
        if is_folder is True:
            pass
        with open(f"{self.PATH}", "wb") as open_file:
            pickle.dump(data, open_file)
        pass 
    #must calculate the any difference in the data then replace
    
    def pull_pickle(self, is_folder=True, bin_set=False):
        #bin_set: binary_set
        data = []
        if is_folder is True:
            if bin_set:
                for item in self.file_list:
                    with open(f"{self.PATH}/{item}", "rb") as read_file:
                        data.append(pickle.load(read_file))
                return data
            for item in self.file_list:
                with open(f"{self.PATH}/{item}", "rb") as read_file:
                    data.append(pickle.load(read_file))
            return data
        if bin_set:
            with open(f"{self.PATH}", "rb") as read_file:
                return pickle.load(read_file)
        
    def push_pickle(self, input_data, is_folder=True):
        if is_folder is True:
            for item in self.file_list:
                with open(f"{self.PATH}/{item}", "wb") as read_file:
                    pickle.dump(input_data, read_file)
            return 

        with open(f"{self.PATH}", "wb") as read_file:
            pickle.dump(input_data, read_file)
        return
        

if __name__ == "__main__":
    data = [
    "The dog jumps over the fence.",
    "A banana fell from the tree.",
    "The elephant walked through the jungle.",
    "She found a mango in the kitchen.",
    "The giraffe reached the tall tree.",
    "It started raining heavily outside.",
    "The computer is on the desk.",
    "The fruit basket is on the table.",
    "The car parked near the house.",
    "Birds flew high in the sky.",
    "The lemon tree grew in the garden.",
    "A mountain appeared in the distance.",
    "The apple was fresh and juicy.",
    "The dog barked at the stranger.",
    "The kitchen was filled with the smell of cookies.",
    "He climbed the tree to pick apples.",
    "The rain washed the dusty streets.",
    "The mangoes ripened under the sun.",
    "The car was parked in the driveway.",
    "The giraffe walked slowly through the savannah."
    ]
    weiner = Data(r"lib\JSON-FILES\puke.pkl")
    weiner.pull_pickle(is_folder=False)
    with open("lib/JSON-FILES/puke.pkl", "r") as f:
        print(f.read())
    

    # print(weiner.pull_pickle(is_folder=False, bin_set=True))