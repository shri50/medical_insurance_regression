import numpy as np
import json
import pickle

class MedicalInsurance():

    def __init__(self,data):
        self.data = data
        print(self.data)

    def __loading(self): # private method
        """
        docstring 
        """
        with open('artifacts\project_data.json','r') as file:
            self.project_data = json.load(file)

        with open('artifacts\scale.pkl','rb') as file:
            self.scaler = pickle.load(file)

        with open('artifacts\model.pkl','rb') as file:
            self.model = pickle.load(file)

    def get_insurnace_price_prediction(self):  # Public method 
        """
        docstring
        """
        self.__loading()

        age =  self.data['html_age']
        gender =  self.data['html_gender']
        bmi =  self.data['html_bmi']
        smoker =  self.data['html_smoker']
        region =  self.data['html_region']

        user_data = np.zeros(len(self.project_data['column_names']))
        user_data[0] = age
        user_data[1] = self.project_data['gender'][gender]
        user_data[2] = bmi
        user_data[3] = self.project_data['smoker'][smoker]

        search_region = 'region_'+region
        index = np.where(np.array(self.project_data['column_names']) == search_region)[0][0]
        user_data[index] = 1

        user_data_scale = self.scaler.transform([user_data])   # Scaling the user data 
        return self.model.predict(user_data_scale)[0]
    