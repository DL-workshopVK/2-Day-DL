import os
import shutil
import argparse
import yaml
import pandas as pd
import numpy as np
from get_data import get_data, read_params

# CREATING FOLDER
def create_fold(config, image=None):
    config = get_data(config)
    dirr = config['load_data']['preprossed_data']
    cla = config['load_data']['num_classes']
    
    # Check if the train/test folders exist
    if os.path.exists(dirr + '/' + 'train') and os.path.exists(dirr + '/' + 'test'):
        print("Train & Test Already Exists...")
        print("I am Skipping it...!")
    else:
        # Create the 'train' and 'test' folders, including missing parent directories
        os.makedirs(dirr + '/' + 'train', exist_ok=True)
        os.makedirs(dirr + '/' + 'test', exist_ok=True)
        
        # Create class folders inside train and test
        for i in range(cla):
            os.makedirs(dirr + '/' + 'train' + '/' + 'class_' + str(i), exist_ok=True)
            os.makedirs(dirr + '/' + 'test' + '/' + 'class_' + str(i), exist_ok=True)
            print(f"Folder for class_{i} Created Successfully...!")

if __name__ == '__main__':
    # Argument parsing for the config file
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    passed_args = args.parse_args()
    
    # Create the folder structure based on the config
    create_fold(config=passed_args.config)