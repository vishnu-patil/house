import pandas as pd
import numpy as np
import pickle
import json
import config
import sklearn

class US_House_PP():

    def __init__(self,Income_Area, House_Age, Rooms_Qty, Bedrooms_Qty, 
                    Area_Population):
        print("INIT FUNCTION")
        self.Income_Area = Income_Area
        self.House_Age =  House_Age
        self.Rooms_Qty = Rooms_Qty
        self.Bedrooms_Qty = Bedrooms_Qty
        self.Area_Population = Area_Population


    def load_saved_data(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.us_house_data = json.load(f)

    def get_us_house_pp(self):
        self.load_saved_data()

        # col_list = x.columns

        test = np.zeros(self.model.n_features_in_, int)
        test[0] = self.Income_Area
        test[1] =  self.House_Age
        test[2] = self.Rooms_Qty
        test[3] = self.Bedrooms_Qty
        test[4] = self.Area_Population

        price1 = np.around(self.model.predict([test])[0] , 2)
        print(f"Predicted House price in US is : {price1} $")    
        return price1
    
if __name__ == "__main__":
    ushp = US_House_PP()
    ushp
