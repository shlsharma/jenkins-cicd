'''
Simple Imputation
Label Encoding
MinMax Scalar
create custom preprocessing transformers
'''
'''
# create custom data transformers
# key things -- > we have to inherit - baseEstimator, TransformerMixin
implement fit and transform
accept input with __init__ method
'''
import os
import sys
from pathlib import Path

## Adding the below path to avoid module not found error
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from prediction_model.config import config


#numerical imputation - mean
class MeanImputer(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        self.variables = variables

    def fit(self, X, y=None):
        self.mean_dict = {}
        for col in self.variables:
            self.mean_dict[col] = X[col].mean()
        return self
    
    def transform(self, X):
        X = X.copy()
        for col in self.variables:
            X[col].fillna(self.mean_dict[col], inplace=True)
        return X

#numerical imputation - mode
class ModeImputer(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        self.variables = variables

    def fit(self, X, y=None):
        self.mode_dict = {}
        for col in self.variables:
            self.mode_dict[col] = X[col].mode()[0]
        return self
    
    def transform(self, X):
        X = X.copy()
        for col in self.variables:
            X[col].fillna(self.mode_dict[col], inplace=True)
        return X

# dropping the column
class DropColumns(BaseEstimator, TransformerMixin):

    def __init__(self, variables_to_drop=None):
        self.variables_to_drop = variables_to_drop

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X = X.drop(columns=self.variables_to_drop)
        return X
    
# Domain Processing
class DomainProcessing(BaseEstimator, TransformerMixin):

    def __init__(self, variable_to_modify=None, variable_to_add=None):
        self.variables_to_modify = variable_to_modify
        self.variables_to_add = variable_to_add

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.variables_to_modify:
            X[feature] = X[feature] + X[self.variables_to_add]
        return X
    
# Custom label Encoder
'''
Returning self in a method of a class is a common design pattern in object-oriented programming, particularly in Python. When a method returns self, it allows for method chaining. Method chaining is a technique where multiple methods are called on the same object sequentially in a single line of code. This pattern makes the code more concise and readable.

In the context of the CustomLabelEncoder class, returning self from the fit method means that after calling fit, the same instance of CustomLabelEncoder can be used for further operations. This is especially useful in the context of machine learning pipelines.
encoder = CustomLabelEncoder(variables=['color', 'size']).fit(data).transform(data)

'''
class CustomLabelEncoder(BaseEstimator, TransformerMixin):
    # Constructor to initialize the variables attribute
    def __init__(self, variables=None):
        self.variables = variables

    # Fit method to learn the mapping from categorical values to numerical labels
    def fit(self, X, y=None):
        self.label_dict = {}  # Dictionary to store the mappings for each variable
        for var in self.variables:
            # Get the index of the sorted value counts in ascending order
            t = X[var].value_counts().sort_values(ascending=True).index
            # Create a mapping dictionary for the variable
            self.label_dict[var] = {k: i for i, k in enumerate(t, start=0)}
        return self  # Return self to make this compatible with Scikit-learn's fit-transform interface
    
    # Transform method to apply the learned mappings to the data
    def transform(self, X):
        X = X.copy()  # Create a copy of X to avoid modifying the original dataframe
        for feature in self.variables:
            # Apply the mapping to the feature
            X[feature] = X[feature].map(self.label_dict[feature])
        return X  # Return the transformed dataframe
    
# Log Transformation
class LogTransforms(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        self.variables = variables

    def fit(self, X, y=None): # any learning
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = np.log(X[feature])
        return X
