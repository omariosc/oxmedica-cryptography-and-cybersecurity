# Practical 22: Specialist Topic - Machine Learning

## Overview

This practical exercise is designed to provide a crash course on basic machine learning (ML) fundamentals and examine different ML models using Python. We will focus on linear regression, lasso regression, and decision trees (including random forest models). You will also learn how to apply these ML models to the datasets you worked on in the Data Processing and Visualisation Labs. This session will take about 2 hours to complete.

## Part 1: Machine Learning Fundamentals (30 minutes)

### Section 1: Introduction to Machine Learning (10 minutes)

1. **What is Machine Learning?**
   - Machine Learning is a subset of artificial intelligence (AI) that focuses on building systems that learn from data to make predictions or decisions without being explicitly programmed.

2. **Types of Machine Learning:**
   - **Supervised Learning:** Models are trained using labeled data (e.g., classification, regression).
   - **Unsupervised Learning:** Models are trained using unlabeled data to find hidden patterns (e.g., clustering, dimensionality reduction).
   - **Reinforcement Learning:** Models learn through trial and error to achieve a goal (e.g., game playing, robotics).

3. **Common Machine Learning Models:**
   - **Linear Regression:** A regression model that assumes a linear relationship between input variables and the output variable.
   - **Lasso Regression:** A regression model that adds a penalty term to the linear regression to enforce sparsity.
   - **Decision Trees:** A model that splits the data into subsets based on feature values to make predictions.
   - **Random Forest:** An ensemble model that combines multiple decision trees to improve performance and reduce overfitting.

### Section 2: Practical Exercises on Linear Regression (20 minutes)

1. **Loading and Preparing Data:**
   ```python
   %pip install pandas scikit-learn
   import pandas as pd
   from sklearn.model_selection import train_test_split

   # Load dataset
   df = pd.read_csv('data.csv')

   # Select features and target
   X = df[['feature1', 'feature2']]
   y = df['target']

   # Split data into training and testing sets
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
   ```

2. **Implementing Linear Regression:**
   ```python
   from sklearn.linear_model import LinearRegression
   from sklearn.metrics import mean_squared_error

   # Initialize and train the model
   lr_model = LinearRegression()
   lr_model.fit(X_train, y_train)

   # Make predictions
   y_pred = lr_model.predict(X_test)

   # Evaluate the model
   mse = mean_squared_error(y_test, y_pred)
   print(f"Mean Squared Error: {mse}")
   ```

   **Exercise 1:**
   - TODO: Load a different dataset and implement linear regression to predict a target variable.

### Section 3: Practical Exercises on Lasso Regression (20 minutes)

1. **Implementing Lasso Regression:**
   ```python
   from sklearn.linear_model import Lasso

   # Initialize and train the model
   lasso_model = Lasso(alpha=0.1)
   lasso_model.fit(X_train, y_train)

   # Make predictions
   y_pred = lasso_model.predict(X_test)

   # Evaluate the model
   mse = mean_squared_error(y_test, y_pred)
   print(f"Mean Squared Error: {mse}")
   ```

   **Exercise 2:**
   - TODO: Load a different dataset and implement lasso regression to predict a target variable.

## Part 2: Decision Trees and Random Forest Models (1 hour 10 minutes)

### Section 1: Practical Exercises on Decision Trees (30 minutes)

1. **Implementing Decision Trees:**
   ```python
   from sklearn.tree import DecisionTreeRegressor

   # Initialize and train the model
   dt_model = DecisionTreeRegressor(random_state=42)
   dt_model.fit(X_train, y_train)

   # Make predictions
   y_pred = dt_model.predict(X_test)

   # Evaluate the model
   mse = mean_squared_error(y_test, y_pred)
   print(f"Mean Squared Error: {mse}")
   ```

   **Exercise 3:**
   - TODO: Load a different dataset and implement a decision tree to predict a target variable.

2. **Visualizing Decision Trees:**
   ```python
   from sklearn.tree import plot_tree
   import matplotlib.pyplot as plt

   # Plot the decision tree
   plt.figure(figsize=(12, 8))
   plot_tree(dt_model, filled=True)
   plt.show()
   ```

   **Exercise 4:**
   - TODO: Visualize the decision tree for your dataset.

### Section 2: Practical Exercises on Random Forest (30 minutes)

1. **Implementing Random Forest:**
   ```python
   from sklearn.ensemble import RandomForestRegressor

   # Initialize and train the model
   rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
   rf_model.fit(X_train, y_train)

   # Make predictions
   y_pred = rf_model.predict(X_test)

   # Evaluate the model
   mse = mean_squared_error(y_test, y_pred)
   print(f"Mean Squared Error: {mse}")
   ```

   **Exercise 5:**
   - TODO: Load a different dataset and implement a random forest to predict a target variable.

2. **Feature Importance in Random Forest:**
   ```python
   # Get feature importances
   importances = rf_model.feature_importances_
   feature_names = X.columns

   # Plot feature importances
   plt.figure(figsize=(10, 6))
   plt.barh(feature_names, importances)
   plt.xlabel('Feature Importance')
   plt.title('Feature Importance in Random Forest')
   plt.show()
   ```

   **Exercise 6:**
   - TODO: Plot the feature importances for your dataset using a random forest model.

### Summary of Part 2

- You have learned about decision trees and random forest models.
- You have practiced implementing and visualizing decision trees.
- You have explored how to implement and evaluate random forest models and analyze feature importances.

## Submission

- Complete the exercises and ensure all solutions are documented.
- Save your progress and ensure all solutions are documented and submitted to GitHub.
- Save the file with the name `"22 Specialist Topic - Machine Learning.ipynb"` in the `"Practical Solutions"` directory.
