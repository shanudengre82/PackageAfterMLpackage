"""
This file helps to split timeseries and normal data into test and train.
Based on the reuqirements, it can also make train, val, and test set.
"""

from sklearn.model_selection import train_test_split

def train_test_advanced(X, y, per=0.3, time = False, val = 0):
    """
    Default split of train and test data is 70% to 30%.
    It is assumed that the data set is not a time series.
    For time series data, use time=True.
    Default value of val is 0. Meaning that we do not need validation set.
    If validation test is needed, change the value to desired further split of train set.
    Val value can be from 0 to 0.5
    """

    if per < 0 or val < 0 or per > 1 or val > 1:
        return "Values of split percentage are not valid.\n Try a range beteen 0 to 1."
    if val == 0:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
        return X_train, X_test, y_train, y_test

    else:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=val, random_state=1)
        return X_train, X_test, X_val, y_val, y_train, y_test

