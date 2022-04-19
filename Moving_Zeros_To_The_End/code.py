# code
'''python'''

def move_zeros(array):
    array1=[]
    array2=[]
    for i in array:
        if i == 0:
            array1.append(i)
        if i != 0:
            array2.append(i)
    array2.extend(array1)

    return array2

