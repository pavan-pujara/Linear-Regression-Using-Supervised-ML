# -*- coding: utf-8 -*-
"""LinearRegressionUsingSupervisedML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BjRSRPr_ggWUXUgBvuKsjek6gJuz86t0

# **Pavan Pujara**

# **Data Science & Business Analytics Tasks** 

# **Task - Prediction using Supervised ML**

**Importing Libraries**
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

"""**Reading** **Data**"""

url = "https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv"
s_data = pd.read_csv(url)
print("Data imported sucessfully")

s_data

"""**Plotting the Distribution of the scores**"""

s_data.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()

"""From the graph above,we can clearly see that there isapositive linear relation between the number of hours studied and percentage of score.

**Preparing the data**

The next step is to divide the data into"attributes"(inputs)and"labels"(outputs).

**Indenpendent and Dependent features**
"""

x = s_data.iloc[:, :-1].values
y = s_data.iloc[:, -1].values

"""Now that we have our attributes and labels,the next step is to split this data into training and test sets.

We'll do this by using Scikit-Learn's built-in train_test_split()method:

"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

"""**Training the Algorithm**

We have split our data into training and testing sets,and now is finally the time to train our algorithm.
"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)
print("Training complete.")

"""**Plotting the regression Line**"""

line =regressor.coef_*x+regressor.intercept_

"""**Plotting for the test data**"""

plt.scatter(x,y)
plt.plot(x, line);
plt.show()

"""**Making Predictions**

Now that we've trained our algorithm, It is time to make some predictions
"""

#Testing data-In Hours
print(x_test)

#Predicting the scores
y_pred = regressor.predict(x_test)

"""**Comparing Actual vs Predicted**"""

df = pd.DataFrame({'Actual':y_test,'Predicted':y_pred})
df

"""**Model Evaluation**"""

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))

"""**Task Objective**

"""

hours = 9.25
own_pred = regressor.predict([[hours]])
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(own_pred[0]))