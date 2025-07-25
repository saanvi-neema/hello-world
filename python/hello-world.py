

# prompt: generate insertion sort 

def insertionSort(arr):
  """
  Sorts an array using the insertion sort algorithm.

  Args:
    arr: A list of comparable elements.

  Returns:
    The sorted list.
  """
  for i in range(1, len(arr)):
    key = arr[i]  # The element to be inserted
    j = i - 1  # Start from the element before the key

    # Move elements of arr[0..i-1], that are greater than key,
    # to one position ahead of their current position
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key  # Place the key in its correct position
  return arr

# Example usage:
my_list = [5, 2, 4, 6, 1, 3]
sorted_list = insertionSort(my_list)
print("Sorted array is:", sorted_list)
