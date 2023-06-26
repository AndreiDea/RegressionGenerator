import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

abs_or_rel = input('Welcome to RegressionGenerator! Would you prefer to enter:\n1. Absolute Path\n2. Relative Path\n')
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

print('File successfully read! Here are the columns available:')
for column in data.columns:
    print(column)
print()

X = None
y = None

print("Please enter columns X and Y to be inserted into linear regression:")

while 1:
    try:
        X_col_name = input('X-column:\n')
        X = data[[X_col_name]]

    except KeyError:
        print("Invalid column. Please check spelling.")
        continue

    break

while 1:
    try:
        Y_col_name = input('Y-column:\n')
        y = data[[Y_col_name]]
    except KeyError:
        print("Invalid column. Please check spelling.")
        continue

    break

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

plt.scatter(X_train, y_train)
plt.plot(X_test, y_pred, color='orange')

plt.xlabel(X_col_name)
plt.ylabel(Y_col_name)

plt.show()
