def print_name():
    print("First name: Yusuf")
    #print("Last name: Modan")


def do_twice(f):
    f()
    f()

myObj = {'Name': 'Yusuf', 'Age': 24, 'Location': 'San Rafael'};
vals = myObj.values()

# #print('Yusuf' in vals)

def reverse_lookup(dictionary, val):
    for key in dictionary:
        if dictionary[key] == val:
            return key
    raise ValueError


def rps_permutations():
    rps = ['r', 'p', 's']
    res = []

    def subroutine(string):
        if len(string) >= 3:
            res.append(string)
            return
        for item in rps:
            subroutine(string + item)
            

    subroutine('')
    return res


def min_max(t):
    return (min(t), max(t)) #returning a tuple here

# #print(min_max([1,2,3,4,5,6,7]))

a, b = ('a', 'b')

def printall(*args):
    print(args)

printall(1, 2.0, '3')

t = (7, 3)

#print(divmod(*t))

s = 'abc'
t = [0, 1, 2, 3]

t = [('a', 'a'), ('b', 1)]
def has_match(tt):
    for letter, number in tt:
        if letter == number:
            return True
    return False

# #print(has_match(t))
stuff = myObj.items()
for l in stuff:
    print(l)

d = dict(zip(range(3), 'abc'))
#print(d)

# for key, val in d.items():
#     print(key, val)

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
    print('t before sorting: ', t)
    t.sort()

    result = []

    for length, word in t:
        result.append(word)
    return result

print('sort_by_length', sort_by_length(['aslf', 'a', 'lllll']))

