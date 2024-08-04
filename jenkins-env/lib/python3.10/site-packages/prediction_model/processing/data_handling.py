'''
This is required to load the dataset, it will be having functions which will
help to save the ml model that is to perform the serialization as well as deserialization
'''

import os
import pandas as pd
import joblib
from prediction_model.config import config

#load the dataset
def load_dataset(file_name):
    filepath = os.path.join(config.DATAPATH, file_name)
    _data = pd.read_csv(filepath) # private variable _data
    return _data

# serialization
def save_pipeline(pipeline_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    joblib.dump(pipeline_to_save, save_path)
    print("Model has been saved under the name", config.MODEL_NAME)

# deserialization
def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    model_loaded = joblib.load(save_path)
    print("Model has been loaded")
    return model_loaded
