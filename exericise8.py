# Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def uniqueElems(ml):
    newl = [];
    
    for el in ml:
        if el not in newl:
            newl.append(el);
    return newl

print("Unique elems list:", uniqueElems([1, 2, 3, 3, 3, 3, 4, 5]));