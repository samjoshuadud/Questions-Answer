
#QUESTION 2

empty = []

def link_to_list(linked_lst):
    print(list(linked_lst))

def link(a, b):
    empty.insert(0, a)

list1 = link(1, link(2, link(3, empty)))


link_to_list(empty)






#QUESTION 3

empty = []

def insert_at_end(lst, elem):
    empty.append(elem)
    print(empty)

lst1 = insert_at_end(empty, 1)

lst2 = insert_at_end(lst1, 2)

lst3 = insert_at_end(lst2, 3)