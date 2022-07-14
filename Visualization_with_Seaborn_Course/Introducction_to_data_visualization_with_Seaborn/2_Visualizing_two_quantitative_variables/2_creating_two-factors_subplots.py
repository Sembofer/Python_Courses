# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3",
            data=student_data,
            kind="scatter",
            col="schoolsup",
            row="famsup",
            row_order=['yes','no'],
            col_order=["yes", "no"])

# Show plot
plt.show()