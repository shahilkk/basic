from posixpath import join


arr1=[20,47,26,89,10,23,24,2]
arr2=[21,34,33,26,10,43,22,47]
for i in arr1:
    for j in arr2:
        if i==j:
            print('same element in both array is',i)