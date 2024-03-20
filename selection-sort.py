def userInput():
    n = int(input("Enter number of elements: "))
    list = []
    for i in range(n):
        list.append(int(input(f"Enter element{i+1}: ")))
    return list

def selectionSortAscend(list):

    for i in range(0, len(list) - 1):
        keys = i
        for j in range(i + 1, len(list)):
            if list[j] < list[keys]:
                keys = j
                print(list)
        list[i], list[keys] = list[keys], list[i]

def selectionSortDescend(list):

    for i in range(0, len(list) - 1):
        keys = i
        for j in range(i + 1, len(list)):
            if list[j] > list[keys]:
                keys = j
                print(list)
        list[i], list[keys] = list[keys], list[i]

list = userInput()
print("Unsorted List: ", list)
selectionSortAscend(list)
print("Ascending Order: ", list)
selectionSortDescend(list)
print("Descending Order: ", list)
