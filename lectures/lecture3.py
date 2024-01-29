# Exercises related to lecture3 of LAAIm-mod1 

# Write the function mul_integers(N) that takes the tuple N, multiply all the int elements in N, and returns the product.
# If N is not a tuple, the functions returns the int number -999.
# If N is a tuple, but does not contain any int number, the function returns 1.
# Scanning the tuple N, when a non-integer element, or the int number 0 is encountered, that element is ignored.

# my dumb solution

def contains_int(N):
    if type(N) != tuple:
        raise TypeError('Not a tuple!')
    for n in N:
        if type(n) == int:
            return True
    return False

def mul_integers(N):
    if type(N) != tuple:
        return -999
    elif contains_int(N):
        prod = 1
        for n in N:
            if type(n) == int and n != 0:
                prod = prod * n
        return prod
    else:
        return 1
    
# solution:
def mul_integers(N):
    if type(N) != tuple:
        return -999
    # we do not need the 'else' statement, since
    # the previuous 'return', if ecountered, terminates the execution
    prod = 1
    for e in N:
        if type(e) == int and e != 0:
            prod = prod * e
    return prod
#-----------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------#

# Write a function get_vowels(S) that returns a tuple with all the unique vowels found in the string S.
# The result tuple contains the vowels in the same order they are present in S.
# If a vowel is found in S more than once, only the first occurrence is considered.
# Suppose - without checking - that S is composed only by lowercase characters.

# Tips:
# returning a tuple is different than printing
# the result tuple should be initialized to the empty tuple before the linear scan of S
# see slide 20 on how to "add" elements to a tuple
# see slide 18 ("Examples vs. non examples") on how to express a tuple of a single element]

# my dumb solution

def remove_vowel(V, v):
    # remove vowel 'v' from string 'S'
    for i in range(len(V)):
        if V[i] == v:
            return V[:i] + V[i+1:]

def get_vowels(S):
    # returns tuple of vowels in string, counted once and in order
    # S is a lower cased string
    vowels = 'aeiou'
    vowels_found = ()
    for s in S:
        if s in vowels:
            vowels = remove_vowel(vowels,s)
            vowels_found = vowels_found + (s,)
    return vowels_found

#solution:
def get_vowels(S):
    R = ()
    for c in S:
        if c in 'aeiou' and c not in R:
            R = R + (c,) 
    return R
#-----------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------#
