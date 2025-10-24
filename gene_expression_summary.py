# gene_expression_summary.py
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("gene_expression_data.csv")

# Basic stats
mean_expression = data["Expression_Level"].mean()
max_gene = data.loc[data["Expression_Level"].idxmax(), "Gene"]
min_gene = data.loc[data["Expression_Level"].idxmin(), "Gene"]

print(f"Average expression level: {mean_expression:.2f}")
print(f"Highest expressed gene: {max_gene}")
print(f"Lowest expressed gene: {min_gene}")

# Plot
plt.figure(figsize=(8, 5))
plt.bar(data["Gene"], data["Expression_Level"])
plt.title("Gene Expression Levels")
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.tight_layout()
plt.savefig("gene_expression_plot.png")

print("Plot saved as 'gene_expression_plot.png'")