# Practical 21: Specialist Topic - Data Science

## Overview

This practical exercise is designed to provide a crash course on data processing and visualisation using Python. You will learn how to collect and clean data, manipulate datasets, and create visualisations. The session is divided into two parts and will take about 1 hour and 45 minutes to complete.

**Note: You will need to create your own notebook for this exercise.**

## Part 1: Data Processing (45 minutes)

### Section 1: Introduction to Data Processing (10 minutes)

1. **Collecting Data Online:**
   - Data can be collected from various online sources such as APIs, web scraping, and publicly available datasets.
   - Example: Using an API to fetch weather data or web scraping a news website for articles.

2. **Using Existing Datasets:**
   - Numerous platforms provide ready-to-use datasets, such as Kaggle, UCI Machine Learning Repository, and government databases.
   - Example: Downloading a dataset from Kaggle for analysis.

3. **Types of Data:**
   - **Structured Data:** Data that is organized in a tabular format, such as spreadsheets or SQL databases.
   - **Unstructured Data:** Data that does not have a predefined format, such as text, images, and videos.
   - **Semi-Structured Data:** Data that does not conform to a rigid structure but has some organizational properties, such as JSON or XML.

4. **Issues with Data:**
   - **Missing Data:** Occurs when some values are absent.
   - **Noisy Data:** Contains errors or outliers.
   - **Inconsistent Data:** Data that contains discrepancies or variations in formats.

### Section 2: Practical Exercises on Data Cleaning and Manipulation (35 minutes)

1. **Loading Data with Pandas:**
   ```python
   import pandas as pd

   # Example: Loading a CSV file
   df = pd.read_csv('data.csv')
   print(df.head())
   ```

2. **Handling Missing Data:**
   ```python
   # Check for missing values
   print(df.isnull().sum())

   # Fill missing values with a specific value
   df.fillna(0, inplace=True)

   # Drop rows with missing values
   df.dropna(inplace=True)
   ```

   **Exercise 1:**
   - TODO: Load a dataset of your choice and handle missing values appropriately. Hint: Use "filetype:csv" in Google search to find CSV files easily.

3. **Removing Duplicates:**
   ```python
   # Remove duplicate rows
   df.drop_duplicates(inplace=True)
   ```

   **Exercise 2:**
   - TODO: Load a dataset and remove any duplicate entries.

4. **Data Transformation:**
   - **Renaming Columns:**
     ```python
     # Rename columns
     df.rename(columns={'old_name': 'new_name'}, inplace=True)
     ```
   
   - **Changing Data Types:**
     ```python
     # Convert data types
     df['column_name'] = df['column_name'].astype('int')
     ```

   **Exercise 3:**
   - TODO: Load a dataset and perform data transformation tasks such as renaming columns and changing data types.

5. **Feature Engineering:**
   - **Creating New Columns:**
     ```python
     # Create a new column based on existing columns
     df['new_column'] = df['column1'] + df['column2']
     ```

   **Exercise 4:**
   - TODO: Create new features in your dataset that could be useful for analysis.

### Summary of Part 1

- You have learned how to collect, clean, and manipulate data using Python.
- You have practiced loading datasets, handling missing data, removing duplicates, transforming data, and creating new features.

## Part 2: Data Visualisation (1 hour)

### Section 1: Introduction to Data Visualisation (15 minutes)

**Note: you may need to use `%pip install seaborn` to install the Seaborn library, and `%pip install plotly` to install the Plotly library.**

1. **Why Data Visualisation?**
   - Data visualisation helps in understanding complex data through graphical representation.
   - It allows for better communication of insights and patterns.

2. **Popular Python Visualisation Libraries:**
   - **Matplotlib:** A versatile library for creating static, animated, and interactive plots.
   - **Seaborn:** Built on top of Matplotlib, it provides a high-level interface for drawing attractive and informative statistical graphics.
   - **Plotly:** A library for creating interactive plots that can be embedded in web applications.
   - **Pandas Visualization:** Built-in capabilities for simple plots from Pandas DataFrames.

3. **Components of Plots and Graphs:**
   - **Title:** Describes the plot.
   - **Axes:** Represents the data dimensions.
   - **Labels:** Describes the data points.
   - **Legends:** Explains the symbols and colors used in the plot.

### Section 2: Practical Exercises on Data Visualisation (45 minutes)

1. **Basic Plotting with Matplotlib:**
   ```python
   import matplotlib.pyplot as plt

   # Example: Line plot
   plt.plot(df['column1'], df['column2'])
   plt.title('Line Plot')
   plt.xlabel('X-axis')
   plt.ylabel('Y-axis')
   plt.show()
   ```

   **Exercise 1:**
   - TODO: Create a line plot using a dataset of your choice.

2. **Creating Bar Charts and Histograms:**
   ```python
   # Example: Bar chart
   df['column1'].value_counts().plot(kind='bar')
   plt.title('Bar Chart')
   plt.xlabel('Categories')
   plt.ylabel('Counts')
   plt.show()

   # Example: Histogram
   df['column2'].plot(kind='hist', bins=20)
   plt.title('Histogram')
   plt.xlabel('Value')
   plt.ylabel('Frequency')
   plt.show()
   ```

   **Exercise 2:**
   - TODO: Create a bar chart and a histogram using your dataset.

3. **Using Seaborn for Statistical Plots:**
   ```python
   import seaborn as sns

   # Example: Box plot
   sns.boxplot(x='column1', y='column2', data=df)
   plt.title('Box Plot')
   plt.show()

   # Example: Pair plot
   sns.pairplot(df)
   plt.title('Pair Plot')
   plt.show()
   ```

   **Exercise 3:**
   - TODO: Create a box plot and a pair plot using your dataset.

4. **Interactive Plots with Plotly:**
   ```python
   import plotly.express as px

   # Example: Scatter plot
   fig = px.scatter(df, x='column1', y='column2', title='Scatter Plot')
   fig.show()
   ```

   **Exercise 4:**
   - TODO: Create an interactive scatter plot using your dataset.

### Summary of Part 2

- You have learned about different data visualisation libraries in Python.
- You have practiced creating various types of plots and graphs using Matplotlib, Seaborn, and Plotly.
- You have explored how to use visualisations to better understand and communicate data insights.

## Submission

- Complete the exercises and ensure all solutions are documented.
- Save your progress and ensure all solutions are documented and submitted to GitHub.
- Save the file with the name `"21 Specialist Topic - Data Science.ipynb"` in the `"Practical Solutions"` directory.
