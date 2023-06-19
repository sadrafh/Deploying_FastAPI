# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The objective of the prediction task is to classify whether an individual's annual income exceeds $50,000. For this purpose, we employed a GradientBoostingClassifier from the scikit-learn library version 1.2.0, utilizing optimized hyperparameters. The hyperparameters were tuned using GridSearchCV, and the optimal values obtained are as follows:

- learning_rate: 1.0
- max_depth: 5
- min_samples_split: 100
- n_estimators: 10

The trained model has been saved as a pickle file in the designated "model" folder. A detailed record of all training steps and performance metrics can be found in the "journal.log" file.

## Intended Use
The intended application of this model is to predict the income level of an individual using a limited set of attributes. It is primarily designed for students, academics, or research purposes.

## Training Data
The Census Income Dataset was obtained from the UCI Machine Learning Repository as a csv file, which can be accessed at this link: https://archive.ics.uci.edu/ml/datasets/census+income. The original dataset consists of 32,561 rows and 15 columns. It includes a target label called "salary," 8 categorical features, and 6 numerical features. For detailed information about each feature, please refer to the UCI link provided.

The target label, "salary," has two classes ('<=50K' and '>50K'), and there is a class imbalance issue with a ratio of approximately 75% for the '<=50K' class and 25% for the '>50K' class.

To ensure data quality, a simple data cleansing process was performed on the original dataset. This involved removing leading and trailing whitespaces from the data. For more insights into the data exploration and cleansing steps, please refer to the "data_cleaning.py" file.

The dataset was split into a training set and a test set using an 80-20 split. Stratification was applied based on the target label, "salary," to maintain the class distribution in both sets.

For the training process, a One Hot Encoder was used to encode the categorical features, while a label binarizer was applied to the target label.
## Evaluation Data
A portion of 20% of the dataset was reserved specifically for evaluating the model's performance.

To prepare the categorical features and the target label for training, transformation techniques were applied. The One Hot Encoder was fitted on the training set to encode the categorical features, while the label binarizer was used to transform the target label. These transformations ensure compatibility with the machine learning model.
## Metrics
The classification performance of the model is assessed using metrics such as precision, recall, and f-beta score. These metrics provide insights into the model's accuracy, completeness, and overall performance in predicting the target labels.

Additionally, the confusion matrix is calculated to further analyze the model's performance. The confusion matrix provides a tabular representation of predicted labels versus actual labels, enabling a more detailed examination of true positives, true negatives, false positives, and false negatives.

- precision:0.767
- recall:0.635
- fbeta:0.706
- Confusion matrix: [[4627 318] [ 558 1008]]

## Ethical Considerations
It is important to note that the dataset should not be regarded as a fair representation of the salary distribution. Therefore, it is not appropriate to utilize this dataset to make assumptions about the salary levels of specific population categories.
## Caveats and Recommendations
The dataset was extracted from the 1994 Census database. However, it is crucial to acknowledge that this dataset is an outdated sample and should not be considered as a reliable statistical representation of the population. It is recommended to utilize this dataset primarily for training purposes in machine learning classification or similar problems.

