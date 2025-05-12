# import numpy as np
# import pandas as pd
# from DecisionTree import build_tree, predict
#
# # Load data
# data = pd.read_csv('data/house_data.csv')
# X = data[['living_in_m2', 'bedrooms', 'grade']].values
# y = data['price'].values
#
# # Build the tree
# tree = build_tree(X, y, max_depth=5)
#
# # Make predictions
# predictions = [predict(tree, x) for x in X]
# print(predictions)
#
#

#
# # main.py
#
# import numpy as np
# import pandas as pd
# from DecisionTree import build_tree, predict, print_tree
#
# # Load data
# data = pd.read_csv('data/house_data.csv')
# X = data[['living_in_m2', 'bedrooms', 'grade']].values
# y = data['price'].values
#
# # Build the tree
# tree = build_tree(X, y, max_depth=5)
#
# # Print the tree structure
# print_tree(tree)
#
# # Make predictions
# predictions = [predict(tree, x) for x in X]
# print(predictions)






# main.py

import numpy as np
import pandas as pd
from DecisionTree import build_tree, predict, print_tree, visualize_tree

# Load data
data = pd.read_csv('data/house_data.csv')
X = data[['living_in_m2', 'bedrooms', 'grade']].values
y = data['price'].values

# Build the tree
tree = build_tree(X, y, max_depth=5)

# Print the tree structure in detail
print("Detailed Tree Structure:")
print_tree(tree, feature_names=['square_feet', 'num_bedrooms', 'grade'])

# Visualize the tree using matplotlib
print("Visualizing the Decision Tree...")
visualize_tree(tree, feature_names=['square_feet', 'num_bedrooms', 'grade'])

# Make predictions
predictions = [predict(tree, x) for x in X]
print("Predictions:", predictions)





