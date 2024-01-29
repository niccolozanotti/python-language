'''
The mode of a list is the most frequent item on the list. For example, the mode of [2,7,5,7,7,2,4] is 7, which appears 3 times. The most frequent values (tie) can be more than one. For example, the mode of [1,2,99,1,0,2] is 1, 2 which appears 2 times each. 

Write a function mode(L) which returns the mode of L as a list.

Suppose (without checking) that the elements of L are immutable (and therefore can be dictionary keys).

Tip: Use a dictionary for frequencies and an auxiliary function (do not use the default max) that returns the maximum item in a list.
'''
def biggest(L):
    max = L[0]
    for l in L:
        if l > max:
            max = l
    return max

def mode(L):
    # L is a list of immutable objects
    # returns list containing the mode(s)
    Freq = {} # empty frequency dict
    for l in L:
        if l in Freq: # the key already exists
            Freq[l] += 1
        else:
            Freq[l] = 1
    values = list(Freq.values())
    high_count = biggest(values) # highest frequency
    # print(high_count)
    # create list with the keys associated to the most frequent element(s)
    return [key for key in Freq if Freq[key] == high_count]

'''
Write a function dict_to_str(D) that takes as parameter a dictionary D (which represents a string, see below) and returns that string.
The dictionary items are of the kind <character>:[<list of indexes>], where the key is a character of the string, and the value is the list of all indexes of that character in the string.
Note that the keys of D are all the unique characters of the string to be returned.
Moreover, the order of the dictionary items, and also of indexes in the lists, is not relevant, and should not influence the function results.

Suppose - without checking - that D is a dictionary, its keys are strings representing characters, and its values are lists of integer indexes.
'''

def lowest(L:list):
    min = L[0]
    for l in L:
        if l < min:
            min = l
    return min


# def dict_to_str(D):
#     # D is a dictionary encoding a string as <character>:[<list of indexes>]
#     # returns the string
#     plain_values = [index for sublist in D.values() for index in sublist]
#     str_len = biggest(plain_values) + 1
#     print(str_len)
#     res = ''

#     # bug: does not handle multiple occurrences of a character
#     # for i in range(str_len):
#     #     for char in D:
#     #         lowest_i = lowest(D[char]) # values are lists
#     #         if lowest_i == i:
#     #             res += char
#     # return res

# solution
    
def dict_to_str(D):
    turned = {} # a new dictionary
    for k,v in D.items():
        for i in v: #the value 'v' is the list of indexes
            turned[i] = k
    print(turned)
    s = ''
    for i in range(len(turned)):
        s += turned[i]
    return s

'''
# a more complete version with parameter controls
def dict_to_str_w_controls(D):
    if not type(D)==dict:
        return 'not dict'
    turned = {}
    for k,v in D.items():
        if not type(v)==list:
            return 'not list'
        for i in v:
            if not type(i)==int:
                return 'invalid index'
            turned[i] = k
    s = ''
    for i in range(len(turned)):
        s += turned[i]
    return s
'''
'''
Write a function invert(D) which takes as a parameter a dictionary whose values are immutable 
objects returns a new dictionary, inverse of D, that is:
each distinct value of D becomes a key in the resulting dictionary
for each inverted dictionary key, the value will be a list of the original keys associated with
that value
Example:

 > D = {'a':2, 'b':2, 'c':3, 'd':4, 'e':3, 'f':0, 'g':3, 'h':2}
 >  invert(D)

{2: ['a', 'b', 'h'], 3: ['c', 'e', 'g'], 4: ['d'], 0: ['f']}
'''
# def invert(D):
#     # returns a new inverted key-value dictionary
#     invD = {} # empty dict
#     for key,vals in D.items():
#         if v isitt
#         for v in vals: # iterate over the vals associated with key if multiple, vals are immutable
#             invD[v] = key
#     return invD
# ciao

def invert(D):
    INV = {}
    for key in D:
        val = D[key] #only for clarity
        if val not in INV: 
            INV[val] = [key]
        else:
            #key is unique so append to the list of previous values
            INV[val].append(key) 
    return INV
    
'''
print(invert({'a':2, 'b':2, 'c':3, 'd':4, 'e':3,'f':0, 'g':3, 'h':2}))
print(invert({}))
print(invert({1:'a', 2:'b', 3:'c'}))
print(invert({'a':'a', 'b':'a', 'c':'a'}))
'''



'''
Write a function threes(a,b) that takes 2 integers as parameters and returns, 
using only one instruction (return of a list comprehension), the list of 
integers between a and b (both endpoints included!) that contain the digit 3.
'''
def threes(a,b):
    #assuming a<= b
    return [num for num in range(a,b+1) if '3' in str(num)]

'''
Write a function flatten(LL) that takes a list of lists of integers, and 
creates a new list wich is simply a list of integers. Use only one instruction
(return of a list comprehension) inside the function.
'''
def flatten(LL):
    return [num for subl in LL for num in subl]
'''
Write a merge(LD) function that takes a list (assume it is, without controls) 
LD of dictionaries as a parameter (if not, return None). Dictionary keys are 
of any type allowable for a key, the values of any type but not lists (if you
find a list, return None). The function returns a new dictionary obtained by 
merging all dictionaries.

In case the same key is present in more than one LD dictionary:
if all values val associated with key in different dictionaries are the same,
then the resulting dictionary will contain the key:val item only once.
if there are different values (val1, val2, ..., valk) for key in LD 
dictionaries, the resulting dictionary must have the item key:[val1,val2,...,valk]
i.e. the key will have as value a list with all the distinct k-values (without 
duplicates) associated in the different dictionaries to the key.
Example:
 >> D1 = {1:'E1',2:'R4',3:'M2'}
 >>	D2 = {2:'V3',3:'M2',(5,'a'):'G?1'}.
The merge([D1, D2]) invocation returns 
{1: 'E1', 2: ['R4', 'V3'], 3: 'M2', (5, 'a'): 'G?1'}.
'''
def merge(LD):
    # returns new dict, merge of all the dicts
    if type(LD) != list:
        return None
    
    mergeD = {}
    for D in LD:
        for key,value in D.items():
            if key in mergeD:
                list(mergeD[key]).append(value)
            else:
                mergeD[key] = value
    return mergeD

print(merge([{1:'E1',2:'R4',3:'M2'}, {2:'V3',3:'M2',(5,'a'):'G?1'}]) == {1: 'E1', 2: ['R4', 'V3'], 3: 'M2', (5, 'a'): 'G?1'})
