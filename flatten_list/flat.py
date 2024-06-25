def flatList(param):
    arr = []

    for i in param:
        if isinstance(i, list):
            arr += flatList(i)
        else:
            arr.append(i)
    return arr


#----------------------------------------------------------------------

value = input("Please enter the list that you want to flat: ")

try:
    value = eval(value)
    flatList = flatList(value)
    print(flatList)
except Exception as e:
    print("Please enter a valid list.")
    print(e)