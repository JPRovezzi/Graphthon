import numpy as np

import matplotlib.pyplot as plt

# Example data: Replace this with your actual collected values
# Each sublist represents the values for one titration

values = np.array([
    3.84, 3.84, 3.72, 3.4, 3.38, 3.38, 1.53, 1.43, 1.5, 1.35, 1.23, 1.34, 1.16,
    1.1, 1.15, 1.16, 1.18, 1.13, 1.1, 1.08, 1.04, 1.01, 0.99, 1.03, 1, 0.96,
    0.97, 0.88, 0.94, 0.94, 0.91, 0.95, 0.94, 0.94, 0.89, 0.95, 0.9, 0.92, 0.9
])


time = np.array([
    0, 0.01, 0.15, 0.5, 0.75, 1, 1.5, 2, 3, 4, 5, 6, 7])



num_groups = 13
group_sizes = np.full(num_groups, len(values) // num_groups)
group_sizes[:len(values) % num_groups] += 1
indices = np.cumsum(group_sizes)
data = np.split(values, indices[:-1])


# Create the boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(
    data,
    notch=False,
    patch_artist=True,
    boxprops=dict(facecolor='gray', color='black'),
    medianprops=dict(color='blue'),
    whiskerprops=dict(color='black'),
    capprops=dict(color='black'),
    whis=[0, 100],
    widths=0.2
    )




        
# Customize the plot
plt.title('Box Chart of Titration Data with Error Bars')
plt.xlabel('Titration Number')
plt.ylabel('Values')
plt.xticks(range(1, len(data) + 1), [f'T{i}' for i in range(1, len(data) + 1)])
plt.ylim(0, 4)  # Set y-axis limits
plt.yticks(np.linspace(min(values), max(values), 20))
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
