"""There are several useful methods and attributes for this.

    .head() returns the first few rows (the “head” of the DataFrame).
    .info() shows information on each of the columns, such as the data type and number of missing values.
    .shape returns the number of rows and columns of the DataFrame.
    .describe() calculates a few summary statistics for each column.
"""

# Print the head of the homelessness data
print(homelessness.head())

# Print the information on each of the columns
print(homelessness.info())

# Return the number of rows and columns of homelessness
print(homelessness.shape)

# Calculate a few summary statistics for each column
print(homelessness.describe())