# -*- coding: utf-8 -*-
"""CDD_ML_Part_4_Progesterone_Regression_Random_Forest.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1roIt_7mlLl30YCeUzxEUuB2EA76Iv14w

# **Computational Drug Discovery: Assessing Descriptor Performance and Machine Learning Models for Progesterone Receptor - Part 4**

Building a regression model of progesterone inhibitors using the random forest algorithm

**Muhammad Abdur Rehman**

Original code by: **Chanin Nantasenamat**

[*'Data Professor'*](https://github.com/dataprofessor)

## **1. Import libraries**
"""

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

"""## **2. Load the data set**"""

df = pd.read_csv('progesterone_06_bioactivity_data_3class_pIC50_pubchem_fp.csv')

"""## **3. Input features**
The ***Progesterone*** data set contains 881 input features and 1 output variable (pIC50 values).

### **3.1. Input features**
"""

X = df.drop('pIC50', axis=1)
X

"""### **3.2. Output features**"""

Y = df.pIC50
Y

"""### **3.3. Let's examine the data dimension**"""

X.shape

Y.shape

"""### **3.4. Remove low variance features**"""

from sklearn.feature_selection import VarianceThreshold
selection = VarianceThreshold(threshold=(.8 * (1 - .8)))
X = selection.fit_transform(X)

X.shape

"""## **4. Data split (80/20 ratio)**"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

X_train.shape, Y_train.shape

X_test.shape, Y_test.shape

"""## **5. Building a Regression Model using Random Forest**"""

import numpy as np
np.random.seed(100)
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, Y_train)
r2 = model.score(X_test, Y_test)
r2

Y_pred = model.predict(X_test)

"""## **6. Scatter Plot of Experimental vs Predicted pIC50 Values**"""

import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn styles
sns.set(color_codes=True)
sns.set_style("white")

# Create the regression plot
ax = sns.regplot(x=Y_test, y=Y_pred, scatter_kws={'alpha': 0.4})

# Set labels and axis limits
ax.set_xlabel('Experimental pIC50', fontsize='large', fontweight='bold')
ax.set_ylabel('Predicted pIC50', fontsize='large', fontweight='bold')
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)

# Set figure size
ax.figure.set_size_inches(5, 5)

# Save the plot as a PDF in Colab storage
plt.savefig('/content/pIC50_plot.pdf', format='pdf')

# Display the plot
plt.show()