def str_sort(str):
    str = str.lower()
    str = str.split(' ')
    str_len = []
    for s in str:
        str_len.append((len(s), s))
    print(str_len)
    str_len = sort(str_len)
    str = []
    for s in str_len:
        str.append(s[1])
    str = " ".join(str)
    str = str.capitalize()

    return str


def sort(array):


    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0][0]
        for x in array:
            if x[0] < pivot:
                less.append(x)
            elif x[0] == pivot:
                equal.append(x)
            elif x[0] > pivot:
                greater.append(x)

        return sort(less)+equal+sort(greater)

    else:
        return array

if __name___=='__main__':
	str = "Keep calm and carry on"
	print(str_sort(str))