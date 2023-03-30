import numpy as np

# Define two fuzzy sets as numpy arrays
set_a = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
set_b = np.array([0.2, 0.4, 0.6, 0.8])

# Calculate the complement of each set
comp_a = 1 - set_a
comp_b = 1 - set_b

# De Morgan's Law for union
dm_union = np.minimum(comp_a, comp_b)
dm_union = 1 - dm_union
print("De Morgan's Law for union:", dm_union)


dm_intersection = np.maximum(comp_a, comp_b)
dm_intersection = 1 - dm_intersection
print("De Morgan's Law for intersection:", dm_intersection)


union_comp = np.union1d(comp_a, comp_b)
intersection_comp = np.intersect1d(comp_a, comp_b)


comp_union = 1 - union_comp
comp_intersection = 1 - intersection_comp


assert np.allclose(dm_union, comp_intersection)


assert np.allclose(dm_intersection, comp_union)
