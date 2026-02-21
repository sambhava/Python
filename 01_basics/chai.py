
my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
# A list of the indexes you want to print
indexes_to_print = [1, 3, 6] 

for index in indexes_to_print:
    if index < len(my_list): # Check if the index is within the list's range
        print(my_list[index])
    else:
        print(f"Index {index} is out of range.")
