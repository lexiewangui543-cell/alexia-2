import numpy as np

arr_2d = np.array([[10, 20, 30],
                   [40, 50, 60]])
print("Original 2D Array:\n", arr_2d) 

arr_2d[0, 1] = 99
print("\nAfter Edit (Row 0, Col 1):\n", arr_2d)

arr_deleted = np.delete(arr_2d, 1, axis=0)
print("\nAfter Deleting Row 1:\n", arr_deleted)

new_row = np.array([[70, 80, 90]])
arr_added = np.append(arr_2d, new_row, axis=0)
print("\nAfter Adding a New Row:\n", arr_added)

