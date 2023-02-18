# function to sort the list
def sorting(Number, List):
    for i in range(Number):
        for j in range(i, Number):
            if List[i] > List[j]:
                temp = List[i]
                List[i] = List[j]
                List[j] = temp
    return List


# function to add a number to the sorted list
def add_to_sorted_list(sorted_list, new_number):
    index = 0
    while index < len(sorted_list) and sorted_list[index] < new_number:
        index += 1
    sorted_list.insert(index, new_number)
    return sorted_list


List = []
try:
    # taking the total number of elements in the list
    Number = int(input("Please enter the Total Number of List Elements: "))
    # taking the elements one by one, iterating the total number of elements
    for i in range(Number):
        value = int(input("Please enter the Value of %d Element : " % i))
        List.append(value)
    # printing the sorted list using the sorting function
    sorted_list = sorting(Number, List)
    print("Element After Sorting List in Ascending Order is : ", sorted_list)
    try:
        # taking the new number and adding it to the sorted position
        new_number = int(input("enter new number"))
        updated_list = add_to_sorted_list(sorted_list, new_number)
        print(updated_list)
    except:
        print("Error: You must enter a valid number.")
except:
    print("Error: You must enter a valid number.")
