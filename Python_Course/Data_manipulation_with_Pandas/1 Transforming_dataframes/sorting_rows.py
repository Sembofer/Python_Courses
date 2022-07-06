    """ one column 	df.sort_values("breed")
        multiple columns 	df.sort_values(["breed", "weight_kg"])
    """

# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values('individuals')

# Print the top few rows
print(homelessness_ind.head())