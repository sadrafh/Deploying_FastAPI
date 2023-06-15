# Script to train machine learning model.

from sklearn.model_selection import train_test_split



# Add the necessary imports for the starter code.
import pickle, os
import pandas as pd
from data import process_data
from model import train_model, compute_model_metrics, inference, compute_slices
from model import compute_confusion_matrix
import logging
# Add code to load in the data.
def remove_if_exists(filename):
    if os.path.exists(filename):
        os.remove(filename)

# Initialize logging
logging.basicConfig(filename='journal.log',
                    level=logging.INFO,
                    filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')

# Add code to load in the data.
datapath = "../data/census.csv"
data = pd.read_csv(datapath)

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)

# Proces the test data with the process_data function.

# Train and save a model.
