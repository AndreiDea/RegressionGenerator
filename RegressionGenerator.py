import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# testfile rel: Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv
# testfile abs: /Users/andrei/Documents/CS projects/RegressionCreator/Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv

abs_or_rel = ('Welcome to RegressionGenerator! Would you prefer to enter:\n1. Absolute Path\n2. Relative Path\n')
valid = 0

while (valid == 0):
    if (abs_or_rel == '1'):
        curr_path = os.getcwd()
        n_levels = curr_path.count('/')
        for i in range(n_levels):
            os.chdir('../')
        path = input('Please enter the absolute path of the CSV file: ')
        try:
            valid = 1
            data = pd.read_csv(path)
        except FileNotFoundError:
            valid = 0
            print('File not found.')

    elif (abs_or_rel == '2'):
        path = input('Please enter the relative path of the CSV file: ')
        try:
            valid = 1
            data = pd.read_csv(path)
        except FileNotFoundError:
            valid = 0
            print('File not found.')
    else:
        abs_or_rel = input('Invalid input. Please enter 1 for absolute path or 2 for relative path.\n')

print('File successfully read! Enter columns that you would like inserted into linear regression:')

X_col_name = input('X-column:\n')
Y_col_name = input('Y-column:\n')

X = data[X_col_name]
Y = data[Y_col_name]

model = LinearRegression()
model.fit(X, Y)
Y_pred = model.predict(X)

plt.scatter(X, Y)
plt.plot(X, Y_pred, color='orange')

plt.xlabel(X_col_name)
plt.ylabel(Y_col_name)

plt.show()
