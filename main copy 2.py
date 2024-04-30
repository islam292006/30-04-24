def find_6(list1):
    for i in range (len(list1)):
      if list1[i] == 6:
            return " 6 Индекс:",i
print(find_6(list1=[5,7,9,9,3,9,2,0,1,2,8,9,6]))

def find_6(list1):
    index = 0
    for i in list1:
        if i == 6:
            return "6 Индекс:", index
        index += 1
    return "6 нет"
    
print(find_6(list1=[5,7,9,9,3,9,2,0,1,2,8,9,6]))
