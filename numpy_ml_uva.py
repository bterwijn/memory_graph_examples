import memory_graph as mg
import numpy as np
mg.extend_numpy()

"""
Relevante functies voor aanpassen:
- np.concatenate()
- np.squeeze()
- np.newaxis
- transpose

Relevante functies voor controleren:
- .shape
- print()
"""

print("=== Initializing the data")
data = np.array([[1, 8], [2, 4], [3, 4], [4, 5], [5, 7]])
output = np.array([-1.35, -3.27, 1.18, 4.84, 6.26])

print(f"Shape: {data.shape}")
print(f"Data:\n{data}")

print(f"Shape: {output.shape}")
print(f"Output:\n{output}")


print("=== Adding output to the data matrix")
output = output[np.newaxis]
print(output)

new_data = np.concatenate((data,output.T),axis=1)
print(new_data)


print("=== Extracting input_B from the data matrix")
input_B = new_data[:,1][np.newaxis].T
print(input_B)


print("=== Multiplying two matrices")
some_vector = np.array([[5,4,3,2,1]])
print(some_vector)

multiplication = np.dot(some_vector,input_B)
print(multiplication)

#how to extract the scalar?
print(np.squeeze(multiplication))
