
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
	dot = np.dot(v1, v2)
    v1_l2_norm = np.linalg.norm(v1)
    v2_l2_norm = np.linalg.norm(v2)
    return round(dot / (v1_l2_norm * v2_l2_norm), 3)
