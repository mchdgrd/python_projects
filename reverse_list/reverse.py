def reverseList(param):
    arr = []
    param.reverse()

    for i in param:
        if isinstance(i, list):
            arr.append(reverseList(i))
        else:
            arr.append(i)
    return arr


#----------------------------------------------------------------------

value = input("Please enter the list that you want to reverse: ")

try:
    value = eval(value)
    reversedList = reverseList(value)
    print(reversedList)
except Exception as e:
    print("Please enter a valid list.")
    print(e)