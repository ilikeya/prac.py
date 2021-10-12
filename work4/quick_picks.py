def add_memberwise():
    lst1 = [eval(x) for x in input("请输入一个列表：").split()]
    print(lst1)
    lst2 = [eval(x) for x in input("请输入一个列表：").split()]
    print(lst2)

    sum_lst = []
    list3=0
    if len(lst1)==len(lst2):
        for index, item in enumerate(lst2):
            sum_lst.append(item + lst1[index])
        print(sum_lst)
    elif len(lst1)>len(lst2):
        lst2.append(list3)
        for index, item in enumerate(lst1):
            sum_lst.append(item + lst2[index])
        print(sum_lst)
    elif len(lst2)>len(lst1):
        lst1.append(list3)
        for index, item in enumerate(lst2):
            sum_lst.append(item + lst1[index])
        print(sum_lst)
add_memberwise()