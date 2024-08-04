'''
need to run 'pytest' in terminal 
it will look for file which start with 'test_' and run those files
'''

'''
Test to perform
1. output from predict script should not be null
2. output from predict script is str data type
3. the output is Y for an example data
'''

import os
import sys
from pathlib import Path

## Adding the below path to avoid module not found error
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

import pytest
from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_predictions

# Fixtures -- > functions run before execution of each test function --> ensure single_prediction should run

@pytest.fixture # decorator this will run this function and keep it ready for test
def single_prediction():
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[:1]
    result = generate_predictions(single_row)
    return result

def test_single_pred_not_none(single_prediction):
    assert single_prediction is not None

def test_single_pred_str_type(single_prediction):
    assert isinstance(single_prediction.get('predictions')[0], str)

def test_single_pred_validate(single_prediction):
    assert single_prediction.get('predictions')[0] == 'Y'
