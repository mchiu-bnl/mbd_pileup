#!/usr/bin/env python

import pandas as pd
from autogluon.tabular import TabularPredictor
from src.data_loader import DataLoader
from src.data_transformer import DataTransformer
from src.prediction_utils import *

data_path = "./"
file_path = ["data/"]

print('Loading Files')
data_loader = DataLoader(data_path, file_path)
files = data_loader.load_csvs()

print('Processing files to training format')
transformer = DataTransformer(files, label="pileup")

print('Training from data...')
train = transformer.get_train()
test = transformer.get_test()

print('Making predictions...')
predictor = TabularPredictor(label="pileup", eval_metric="log_loss").fit(train)
#models="AutogluonModels/ag-20250805_150253"
#predictor = TabularPredictor.load(models)

y_pred = predictor.predict(test.drop(["pileup"],axis=1))
probs = predictor.predict_proba(test.drop(["pileup"],axis=1))

test.insert(2, "pred", y_pred)
test.insert(3, "proba", probs[1])

test.to_csv("predictions.csv")
