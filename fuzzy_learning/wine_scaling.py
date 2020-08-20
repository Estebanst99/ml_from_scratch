from fuzzy_system.fuzzy_learning_helper import load_winequality_red
from fuzzy_system.fuzzy_learning_helper import load_linear_model
from fuzzy_system.fuzzy_learning_helper import split_train_test
from fuzzy_system.fuzzy_learning_system import FuzzyLearningSystem
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from math import log



X, y = load_winequality_red()

s = 'chlorides'
c = X[s]
c_log = np.log(c)
c_log[c_log < -3.5] = -3.5
c_log[c_log > -1.5] = -1.5
X[s] = c_log

s='residual sugar'
c = X[s]
c_log = np.log(c)
c_log[c_log > 2] = 2
X[s] = c_log

s = 'sulphates'
c = X[s]
c[c > 1.25] = 1.25
X[s] = c

s = 'total sulfur dioxide'
c = X[s]
c_log = np.log(c)
X[s] = c_log


X.hist(bins=50)
plt.show()