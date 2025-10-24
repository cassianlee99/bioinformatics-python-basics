# gene_expression_summary.py
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("gene_expression_data.csv")

# Basic stats
mean_expression = data["Expression_Level"].mean()
highest_gene = data.loc[data["Expression_Level"].idxmax(), "Gene"]
lowest_gene = data.loc[data["Expression_Level"].idxmin(), "Gene"]

print(f"Average expression level: {mean_expression:.2f}")
print(f"Highest expressed gene: {highest_gene}")
print(f"Lowest expressed gene: {lowest_gene}")

# Plot
plt.figure(figsize=(8, 5))
plt.bar(data["Gene"], data["Expression_Level"], color="skyblue")
plt.axhline(y=mean_expression, color="red", linestyle="--", label=f"Mean = {mean_expression:.2f}")
plt.title("Gene Expression Levels")
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.legend()
plt.tight_layout()
plt.savefig("gene_expression_plot.png")
plt.show()