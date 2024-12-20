# -*- coding: utf-8 -*-

# Data handling
import numpy as np
import pandas as pd

# Libraries for plotting
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly import tools

# Statistical tests
import statsmodels.api as sm
import scipy

# Standard ML Models for comparison
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
import xgboost as xgb

# Sklearn utilities
from sklearn.model_selection import (
    cross_val_predict,
    KFold,
    cross_val_score,
    GridSearchCV,
    train_test_split,
    RandomizedSearchCV,
)
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)
from sklearn.preprocessing import MinMaxScaler


# ignore warnings
import warnings
warnings.filterwarnings("ignore")

from google.colab import drive
drive.mount('/content/drive')

loan = pd.read_csv('/content/drive/MyDrive/RBAC 2024_Ngoc/merged_loan.csv')

loan.info()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame
# df = pd.read_csv('your_dataset.csv')

# Function to visualize distributions of all columns
def plot_distributions(df):
    # Set up the matplotlib figure size
    n_cols = len(df.columns)
    plt.figure(figsize=(15, 5 * n_cols))

    # Iterate over columns
    for i, col in enumerate(df.columns, 1):
        plt.subplot(n_cols, 1, i)

        # Check if the column is numerical
        if pd.api.types.is_numeric_dtype(df[col]):
            sns.histplot(df[col], kde=True)  # Histogram with KDE for numerical columns
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.title(f"Distribution of {col}")
        else:
            sns.countplot(y=df[col])  # Count plot for categorical columns
            plt.xlabel("Count")
            plt.ylabel(col)
            plt.title(f"Distribution of {col}")

    plt.tight_layout()
    plt.show()

# Apply the function to visualize distributions
plot_distributions(loan)

demo = pd.read_csv('/content/drive/MyDrive/RBAC 2024_Ngoc/Demographic_cluster.csv')
demo

loan['no'] = range(1, len(loan) + 1)

# Display the updated DataFrame
loan

loan.to_csv("/content/drive/MyDrive/RBAC 2024_Ngoc/merged_loan.csv", index=False)

loan

demo.info()

import pandas as pd

# Example DataFrame (Replace with your actual dataset)
# loan = pd.read_csv('your_dataset.csv')  # Load your data here

# Function to remove outliers based on the 25th and 75th quantiles
def remove_outliers(df, columns):
    for column in columns:
        Q1 = df[column].quantile(0.25)  # 25th percentile
        Q3 = df[column].quantile(0.75)  # 75th percentile
        IQR = Q3 - Q1  # Interquartile range
        # Define the bounds for non-outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        # Filter out outliers for the current column
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df

# Specify the columns where you want to remove outliers
columns_to_check = ['LOAN_TERM', 'MONTH_INTEREST']  # Adjust based on your dataset

# Remove outliers from specified columns
loan_no_outliers = remove_outliers(loan, columns_to_check)

# Display the cleaned data
print(loan_no_outliers)
loan_no_outliers.to_csv('/content/drive/MyDrive/RBAC 2024_Ngoc/Loan_No_Outliers.csv')

loan_no_outliers.info()

merge = pd.merge(loan_no_outliers, demo, on='no')
merge

# Example 1: Histogram for `loan_amount`
plt.figure(figsize=(8, 6))
sns.histplot(data=loan_df, x='loan_amount', bins=30, kde=True)
plt.title('Distribution of Loan Amount')
plt.xlabel('Loan Amount')
plt.ylabel('Frequency')
plt.show()

# Example 2: Box plot for `month_interest`
plt.figure(figsize=(8, 6))
sns.boxplot(data=loan_df, x='month_interest')
plt.title('Box Plot of Monthly Interest Rate')
plt.xlabel('Monthly Interest Rate')
plt.show()

# Example 3: Bar plot for `loan_purpose`
plt.figure(figsize=(8, 6))
sns.countplot(data=loan_df, x='loan_purpose', order=loan_df['loan_purpose'].value_counts().index)
plt.title('Loan Purpose Distribution')
plt.xlabel('Loan Purpose')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x labels if they are long
plt.show()

# Example 4: Pie chart for `product_category`
product_counts = loan_df['product_category'].value_counts()
plt.figure(figsize=(8, 6))
product_counts.plot.pie(autopct='%1.1f%%', startangle=90, cmap='coolwarm')
plt.title('Product Category Distribution')
plt.ylabel('')  # Hide y-axis label
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'merged_df' is your DataFrame with the dataset

# Step 1: Calculate the correlation matrix
numeric_df = loan_df[['loan_amount','month_interest','loan_term']]

# Step 2: Calculate the correlation matrix
correlation_matrix = numeric_df.corr()

# Step 3: Display the correlation matrix
print(correlation_matrix)

# Step 4: Visualize the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix of Numeric Variables')
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Create a contingency table
contingency_table = pd.crosstab(loan_df['loan_purpose'], loan_df['product_category'])

# Plot heatmap
sns.heatmap(contingency_table, annot=False, cmap="coolwarm")
plt.figure(figsize=(12, 10))
plt.show()

# Calculate Chi-square and Cramér's V
chi2, p, dof, _ = chi2_contingency(contingency_table)
n = contingency_table.sum().sum()  # total sample size
cramers_v = np.sqrt(chi2 / (n * (min(contingency_table.shape) - 1)))
print("Contingency Table:\n", contingency_table)
print("Cramér's V:", cramers_v)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Create a contingency table
contingency_table = pd.crosstab(loan_df['liquidity'], loan_df['product_category'])

# Plot heatmap
sns.heatmap(contingency_table, annot=False, cmap="coolwarm")
plt.figure(figsize=(12, 10))
plt.show()

# Calculate Chi-square and Cramér's V
chi2, p, dof, _ = chi2_contingency(contingency_table)
n = contingency_table.sum().sum()  # total sample size
cramers_v = np.sqrt(chi2 / (n * (min(contingency_table.shape) - 1)))
print("Contingency Table:\n", contingency_table)
print("Cramér's V:", cramers_v)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Create a contingency table
contingency_table = pd.crosstab(loan_df['rate'], loan_df['product_category'])

# Plot heatmap
sns.heatmap(contingency_table, annot=False, cmap="coolwarm")
plt.figure(figsize=(12, 10))
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Create a contingency table
contingency_table = pd.crosstab(loan_df['rate'], loan_df['liquidity'])

# Plot heatmap
sns.heatmap(contingency_table, annot=False, cmap="coolwarm")
plt.figure(figsize=(12, 10))
plt.show()

# Calculate Chi-square and Cramér's V
chi2, p, dof, _ = chi2_contingency(contingency_table)
n = contingency_table.sum().sum()  # total sample size
cramers_v = np.sqrt(chi2 / (n * (min(contingency_table.shape) - 1)))
print("Contingency Table:\n", contingency_table)
print("Cramér's V:", cramers_v)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Create a contingency table
contingency_table = pd.crosstab(loan_df['rate'], loan_df['liquidity'])

# Plot heatmap
sns.heatmap(contingency_table, annot=False, cmap="coolwarm")
plt.figure(figsize=(12, 10))
plt.show()

loan_df
loan_df.info()

loan_df['customer_profile_cluster'].unique()

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Checking unique values in each variable to ensure variability
print("Unique values in Variable A:", loan_df['loan_purpose'].unique())
print("Unique values in Variable B:", loan_df['product_category'].unique())



# Create a contingency table
contingency_table = pd.crosstab(columns=[loan_df['loan_purpose'], loan_df['product_category']], index=True)

# Calculate Chi-square and Cramér's V
chi2, p, dof, _ = chi2_contingency(contingency_table)
n = contingency_table.sum().sum()  # total sample size
cramers_v = np.sqrt(chi2 / (n * (min(contingency_table.shape) - 1)))
print("Contingency Table:\n", contingency_table)
print("Cramér's V:", cramers_v)

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
features = ['customer_income', 'working_in_year', 'number_of_dependants']  # Adjust based on your dataset
loan_types = loan_df[features]

# Step 3: Handle missing values if necessary (example: fill with mean or drop)
loan_types = loan_types.dropna()  # Adjust this line based on your preferred approach

# Step 4: Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(loan_types)
'''
# Elbow method to determine the optimal number of clusters
inertia_values = []
cluster_range = range(1, 16)  # Try from 1 to 15 clusters

for k in cluster_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia_values.append(kmeans.inertia_)

# Plotting the elbow graph
plt.figure(figsize=(10, 6))
plt.plot(cluster_range, inertia_values, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia (Sum of Squared Distances)')
plt.title('Elbow Method for Optimal K')
plt.show()
'''
# Step 5: Choose the optimal number of clusters based on the elbow plot (e.g., 4)
optimal_clusters = 3  # Update based on the elbow plot

# Step 6: Apply KMeans clustering with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
loan_df['customer_cluster'] = kmeans.fit_predict(scaled_data)

# Step 7: Save the new DataFrame with cluster labels
loan_df.to_csv('/content/drive/MyDrive/RBAC 2024_Ngoc/Bản sao của data_merged.csv', index=False)

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot in 3D
scatter = ax.scatter(
    loan_df['customer_income'],
    loan_df['working_in_year'],
    loan_df['number_of_dependants'],
    c=loan_df['customer_cluster'],
    # Adjust size based on LOAN_AMOUNT
    cmap='plasma',
    alpha=0.6,

)

# Add labels
ax.set_xlabel('CUSTOMER INCOME')
ax.set_ylabel('WORKING EXPERIENCE')
ax.set_zlabel('NUMBER OF DEPENDANTS')
plt.colorbar(scatter, ax=ax, label='customer_clutser')
plt.title('3D Scatter Plot of Clusters')
plt.show()
for angle in np.linspace(0, 360, 90):  # 90 frames for a smooth rotation
    ax.view_init(elev=20, azim=angle)
    plt.draw()
    plt.pause(0.1)  # Pause between frames to create the animation effect
plt.show()

df = pd.read_csv('/content/drive/MyDrive/RBAC 2024_Ngoc/Bản sao của data_merged.csv')

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
features = ['business_line', 'month_interest', 'loan_amount']  # Adjust based on your dataset
loan_types = df[features]

# Step 3: Handle missing values if necessary (example: fill with mean or drop)
loan_types = loan_types.dropna()  # Adjust this line based on your preferred approach

# Step 4: Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(loan_types)
'''
# Elbow method to determine the optimal number of clusters
inertia_values = []
cluster_range = range(1, 16)  # Try from 1 to 15 clusters

for k in cluster_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia_values.append(kmeans.inertia_)

# Plotting the elbow graph
plt.figure(figsize=(10, 6))
plt.plot(cluster_range, inertia_values, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia (Sum of Squared Distances)')
plt.title('Elbow Method for Optimal K')
plt.show()
'''
# Step 5: Choose the optimal number of clusters based on the elbow plot (e.g., 4)
optimal_clusters = 3  # Update based on the elbow plot

# Step 6: Apply KMeans clustering with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled_data)

# Step 7: Save the new DataFrame with cluster labels
df.to_csv('/content/drive/MyDrive/RBAC 2024_Ngoc/MERGE.csv', index=False)

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot in 3D
scatter = ax.scatter(
    df['business_line'],
    df['loan_amount'],
    df['month_interest'],
    c=df['cluster'],
    # Adjust size based on LOAN_AMOUNT
    cmap='plasma',
    alpha=0.6,

)

# Add labels
ax.set_xlabel('BUSINESS LINE')
ax.set_ylabel('LOAN AMOUNT')
ax.set_zlabel('MONTH INTEREST')
plt.colorbar(scatter, ax=ax, label='cluster')
plt.title('3D Scatter Plot of Clusters')
plt.show()
for angle in np.linspace(0, 360, 90):  # 90 frames for a smooth rotation
    ax.view_init(elev=20, azim=angle)
    plt.draw()
    plt.pause(0.1)  # Pause between frames to create the animation effect
plt.show()

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
features = ['business_line', 'month_interest', 'loan_term','loan_amount','disbursement_channel','liquidity','rate','has_insurance']  # Adjust based on your dataset
loan_types = loan_df[features]

# Step 3: Handle missing values if necessary (example: fill with mean or drop)
loan_types = loan_types.dropna()  # Adjust this line based on your preferred approach

# Step 4: Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(loan_types)
'''
# Elbow method to determine the optimal number of clusters
inertia_values = []
cluster_range = range(1, 16)  # Try from 1 to 15 clusters

for k in cluster_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia_values.append(kmeans.inertia_)

# Plotting the elbow graph
plt.figure(figsize=(10, 6))
plt.plot(cluster_range, inertia_values, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia (Sum of Squared Distances)')
plt.title('Elbow Method for Optimal K')
plt.show()
'''
# Step 5: Choose the optimal number of clusters based on the elbow plot (e.g., 4)
optimal_clusters = 18 # Update based on the elbow plot

# Step 6: Apply KMeans clustering with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
loan_df['cluster'] = kmeans.fit_predict(scaled_data)

# Step 7: Save the new DataFrame with cluster labels


from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot in 4D
scatter = ax.scatter(
    loan_df['business_line'],
    loan_df['month_interest'],
    loan_df['loan_amount'],
    c=loan_df['product_category'],
    # Adjust size based on LOAN_AMOUNT
    cmap='plasma',
    alpha=0.6,

)

# Add labels
ax.set_xlabel('BUSINESS LINE')
ax.set_ylabel('MONTH INTEREST')
ax.set_zlabel('LOAN AMOUNT')
plt.colorbar(scatter, ax=ax, label='product categories')
plt.title('3D Scatter Plot of Clusters')
plt.show()
for angle in np.linspace(0, 360, 90):  # 90 frames for a smooth rotation
    ax.view_init(elev=20, azim=angle)
    plt.draw()
    plt.pause(0.1)  # Pause between frames to create the animation effect
plt.show()

merge['cluster'] = merge['cluster'] + 1

merge

merge.info()

loan_df = pd.read_csv('/content/drive/MyDrive/RBAC 2024_Ngoc/Bản sao của data_merged.csv')

"""3 clusters have intertwine loan purpose education, shopping, and vehicle. among those main purpose, loan purpose for shopping seems to hold majority priority."""

plt.figure(figsize=(12, 6))

# Create a countplot to visualize how 'LOAN_PURPOSE' is distributed by clusters
sns.countplot(data=loan_df, x='loan_purpose', hue='product_category', palette='Set2')

# Set plot title and labels
plt.title('Loan purpose by product category', fontsize=16)
plt.xlabel('Loan Purpose', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Rotate x-axis labels for better visibility (if needed)
plt.xticks(rotation=45)

# Show the plot
plt.show()

"""They mostly borrow money within the term of 1 year, 1,5 years, 2 years and 3 years. 2 years loan term mostly taken. Cluster 1 seems to loan in a longer term than cluster 2, 3

cluster 1,2 are in business line 0, cluster 3 in business line 2 (assumption: cluster 1,2 not own a self-employed business, just a bit among freelencer in cluster 2 open their own business (agency for example)), Cluster 3 seems to be self-employed.
"""

plt.figure(figsize=(12, 6))

# Create a countplot to visualize how 'LOAN_PURPOSE' is distributed by clusters
sns.countplot(data=loan_df, x='business_line', hue='product_category', palette='Set2')

# Set plot title and labels
plt.title('Business Line by product category', fontsize=16)
plt.xlabel('Business Line', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Rotate x-axis labels for better visibility (if needed)
plt.xticks(rotation=45)

# Show the plot
plt.show()

plt.figure(figsize=(12, 6))

# Create a countplot to visualize how 'LOAN_PURPOSE' is distributed by clusters
sns.countplot(data=loan_df, x='loan_typescluster', hue='product_category', palette='Set2')

# Set plot title and labels
plt.title('Product category by Cluster', fontsize=16)
plt.xlabel('product category', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Rotate x-axis labels for better visibility (if needed)
plt.xticks(rotation=45)

# Show the plot
plt.show()

"""Clusters mostly choose 2 common disbusement channel 1 and 2"""

plt.figure(figsize=(12, 6))

# Create a countplot to visualize how 'LOAN_PURPOSE' is distributed by clusters
sns.countplot(data=loan_df, x='disbursement_channel', hue='product_category', palette='Set2')

# Set plot title and labels
plt.title('Disbursement channel by product category', fontsize=16)
plt.xlabel('Disbursement channel', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Rotate x-axis labels for better visibility (if needed)
plt.xticks(rotation=45)

# Show the plot
plt.show()

plt.figure(figsize=(12, 6))

# Create a countplot to visualize how 'LOAN_PURPOSE' is distributed by clusters
sns.countplot(data=loan_df, x='income_resource', hue='product_category', palette='Set2')

# Set plot title and labels
plt.title('Income Resource by product category', fontsize=16)
plt.xlabel('Income Resource', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Rotate x-axis labels for better visibility (if needed)
plt.xticks(rotation=45)

# Show the plot
plt.show()

plt.figure(figsize=(12, 6))

# Create a countplot to visualize how 'LOAN_PURPOSE' is distributed by clusters
sns.countplot(data=loan_df, x='income_resource', hue='rate', palette='Set2')

# Set plot title and labels
plt.title('Income Resource by Loan Rating', fontsize=16)
plt.xlabel('Income Resource', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Rotate x-axis labels for better visibility (if needed)
plt.xticks(rotation=45)

# Show the plot
plt.show()

plt.figure(figsize=(12, 6))

# Create a countplot to visualize how 'LOAN_PURPOSE' is distributed by clusters
sns.countplot(data=merge, x='LOAN_TERM', hue='loan_types cluster', palette='Set2')

# Set plot title and labels
plt.title('Distribution of LOAN TERM by Cluster', fontsize=16)
plt.xlabel('LOAN TERM', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Rotate x-axis labels for better visibility (if needed)
plt.xticks(rotation=45)

# Show the plot
plt.show()

loan

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
from statsmodels.api import MNLogit
import statsmodels.api as sm
# Independent variables
X = loan_df[['loan_amount', 'month_interest', 'business_line', 'liquidity','loan_term']]

# Dependent variable with multiple classes
y = loan_df['product_category']

# Standardize the data (optional but often improves model performance)
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a multinomial logistic regression model
multi_log_reg = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=200)

# Fit the model
multi_log_reg.fit(X_train, y_train)

# Predict on the test set
y_pred = multi_log_reg.predict(X_test)

multi_log_reg = MNLogit(y, X)
result = multi_log_reg.fit()

# Model evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(result.summary())

