import numpy as np
import pandas as pd
import glob
import re

verbosity = 0

class DataTransformer:
    def __init__(self, dataframes, label):
        print('DataTransformer')
        self.dfs = dataframes
        print(self.dfs)
        self.train = self.dfs['train_pileup.csv']
        self.test = self.dfs['test_pileup.csv']

    def get_train(self):
        return self.train
    
    def get_test(self):
        return self.test
