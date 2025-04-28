import json
import os
import pickle
#to import data from, JSON file

def file_checker(data):
    try:
        if str(data).endswith(".json"):
            return "json"
        elif str(data).endswith(".pkl"):
            return "pkl"
    except:
        if type(data) == list:
            compiled_data = []
            for item in data:
                compiled_data.append(file_checker(item))
            
            if compiled_data.count("json") > compiled_data.count("pkl"):
                return "json"
            else:
                return "pkl"

class Data:
    """Class that handles the input and output of data. \n\n\n All data is stored in BINARY format in either pkl or json; with more focus towards pkl."""
    def __init__(self, folder_PATH: str, **kwargs):
        self.binary_set = 0
        try:
            self.file_list = os.listdir(rf"{folder_PATH}")
        except:
            self.file_list = False
        self.PATH = folder_PATH
        self.pulled_data = []
        self.is_binary = file_checker(folder_PATH)
        self.is_folder = kwargs.get("is_folder", False)

    def retrieve(self, bin_set=False):
        "Pulls data out of file"
        data = []
        read = "rb" if bin_set else "r"
        if self.is_folder:
                for item in self.file_list:
                    with open(f"{self.PATH}/{item}", read) as read_file:
                        data.append(pickle.load(read_file))
                    return data
        else:
            with open(f"{self.PATH}", read) as read_file:
                return pickle.load(read_file)

    #write inputed data into a file in binary

    def push_data(self, data):
        
        if self.is_folder:
            pass

        with open(f"{self.PATH}", "wb") as open_file:
            pickle.dump(data, open_file)
        pass 
    #must calculate the any difference in the data then replace
    
    @staticmethod
    def pull_pickle(file_name, bin_set=True):
        pull_bin = "rb" if bin_set else "r"
        try:
            with open(f"{file_name}", pull_bin) as read_file:
                return pickle.load(read_file)
        except:
            data = []
            for item in os.listdir(file_name):
                with open(f"{file_name}/{item}", pull_bin) as read_file:
                    data.append(pickle.load(read_file))
            return data
    
    @staticmethod
    def push_pickle(file_name, push_bin=True):
        """Saves data to a binary or text file using pickle.
        
            Args:
                file_name (str): The name of the file or directory to which data should be saved.
                push_bin (bool, optional): If True, save in binary mode; if False, save in text mode. Defaults to True.

            Raises:
                Exception: If an error occurs during file writing."""

        push_bin = "wb" if push_bin else "w"
        try:
            with open(file_name, push_bin) as read_file:
                pickle.dump(read_file)
        except:
            for item in os.listdir(file_name):
                with open(f"{file_name}/{item}", push_bin) as read_file:
                    pickle.dump(read_file)
    
    @staticmethod
    def pull_json(file_name, bin_set=False):
        pull_bin = "rb" if bin_set else "r"
        try:
            with open(f"{file_name}", pull_bin) as read_file:
                return pickle.load(read_file)
        except:
            data = []
            for item in os.listdir(file_name):
                with open(f"{file_name}/{item}", pull_bin) as read_file:
                    data.append(pickle.load(read_file))
            return data
    
    @staticmethod
    def push_json(file_name, push_bin=False):
        push_bin = "wb" if push_bin else "w"
        try:
            with open(file_name, push_bin) as read_file:
                pickle.dump(read_file)
        except:
            for item in os.listdir(file_name):
                with open(f"{file_name}/{item}", push_bin) as read_file:
                    pickle.dump(read_file)

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
    with open("lib/JSON-FILES/puke.pkl", "rb") as f:
        print(f.read())
    

    print(weiner.pull_pickle(is_folder=False, bin_set=True))