list = [1,2,3,4,5]
my_dictionary = {'Yusuf': 'Yusuf'}


def reduce(collection, accumulator, start):
    for item in collection:
        start = accumulator(start, item)
    return start

print(reduce(list, lambda total, val: total + val, 5))



#each function
def each(collection, callback):
    for val in collection:
        callback(val)

#each(list, print)

def indexOf(array, target):
    for i in range(len(array)):
        if(target == array[i]):
            return i
    return -1

# print(indexOf(list, 9))

def contains(collection, target):
    return reduce(collection, lambda total, val: total or val == target, False)
# print(contains(list, 3))

def histogram(array):
    d = dict()
    for item in array:
        if item not in d:
            d[item] = 1
        else:
            d[c] += 1
    return d

#print(histogram(list))

def some_stuff():
    n = input()
    str = input()
    arr = str.split()
    distinct = set(arr)
    res = []
    for x in distinct:
        res.append(int(x))



    return sum(res)/len(res)
print(some_stuff())


