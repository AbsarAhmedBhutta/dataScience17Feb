List = []

# input range of list from the user

Number = int(input("Please enter the Total Number of List Elements: "))

# input each element of list
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " % i))
    List.append(value)

# sorting the list
for i in range(Number):
    for j in range(i, Number):
        if List[i] > List[j]:
            temp = List[i]
            List[i] = List[j]
            List[j] = temp

sorted_list = List
print("Element After Sorting List in Ascending Order is : ", sorted_list)


# function to add new number to the list in a sorted position
def add_to_sorted_list(sorted_list, new_number):
    index = 0
    while index < len(sorted_list) and sorted_list[index] < new_number:
        index += 1
    sorted_list.insert(index, new_number)
    return sorted_list


try:
    new_number = int(input("enter new number"))
    updated_list = add_to_sorted_list(sorted_list, new_number)
    print(updated_list)
except:
    print("Error: You must enter a valid number.")
