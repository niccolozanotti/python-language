'''
Homework among the slides of Lecture6
'''

class Student:
    def __init__(self, registration_number, name, year):
        self.reg_no = registration_number
        self.name = name
        self.year = year # 1,2,3,4,5
    def show(self):
        print(self.reg_no,self.name,self.year)
    def pass_class(self):
        self.year += 1

People = [Student(i**2,'c'+str(i),i) for i in range(1,6)]


'''
Lab 4 : OOP
'''  

'''
Define a class Fraction to represent fractions as objects with three elements: sign, numerator, denominator, of types
 respectively str, int, int.

The __init__ takes as parameters two integers N and D.

N represents the numerator with sign of the fraction
D represents the denominator. It must always be >0. If it is not passed, it assumes the default value of 1.
The __init__ initializes the following private attributes:

__sign: a string of a single character that represents the sign of the fraction. It can assume only values '+' or '-'
__num: a positive (>=0) integer that represents the numerator
__den: a positive integer, different from 0 (i.e. >0), that represents the denominator
NB!! The __init__ checks that N and D are integers, and that D>0
In case the parameters do not respect these conditions, all the attributes for sign, numerator, and denominator must be
 initialized to None 

 The class implements several methods.

Write a method get that returns sign, numerator, and denominator as a tuple of type (str, int, int). E.g. fraction +1/10 
will be returned as the tuple ('+',1,10), while the fraction -3/5 will be returned as ('-', 3, 5)
Write a method value that takes as parameter an integer d and calculates the value of the fraction and returns it as a float,
 rounded with the round function at d decimals.
Write a method reduce that modifies the fraction by reducing it to the lowest terms. Hint: you can use the gcd function from 
the math module. For testing purposes, the method must also return self
Write the magic method __eq__ that checks if the fraction is equal to another fraction taken as a parameter. Two fractions 
are equal if their reduced forms are equal. Attention: the method must not reduce or modify the two objects. Do not use the 
value function and in general do not compare the float values of the fractions.
Write the magic method __str__ that returns a string representation of the fraction. The string is in the form SN/D (e.g. +1/3,
 -20/40), without spaces
Write the magic method __add__ that adds the fraction on which is called to another. The return value must be a new fraction, 
reduced to the lowest terms. Attention: the method must not reduce or modify the two original objects. If the resulting numerator
 is 0, return the reduced fraction with numerator 0 and the reduced denominator.
'''

# from math import gcd,lcm

# class Fraction:
#     __sign : str 
#     __num : int # >= 0 
#     __den : int # > 0
#     def __init__(self,N,D=1):
#         if isinstance(N,int) and isinstance(D,int) and D > 0:
#             self.__den = D
#             if N < 0 :
#                 self.__num = abs(N)
#                 self.__sign = '-'
#             else:
#                 self.__num = N
#                 self.__sign = '+'
#         else:
#             self.__num = None
#             self.__den = None
#             self.__sign = None
#     def get(self):
#         return  (self.__sign,self.__num,self.__den)
#     def value(self, d: int):
#         return round(self.__num/self.__den,d)
#     def reduce(self):
#         greatest_div = gcd(self.__num,self.__den)
#         self.__num //= greatest_div
#         self.__den //= greatest_div
#         return self
#     def __eq__(self,other):
#         return (other.__num // self.__num ) == (other.__den // self.__den )
#     def __str__(self):
#         return self.__sign + str(self.__num) + '/' + str(self.__den)
#     def __add__(self, other):
#         least_comm_mult = lcm(self.__den,other.__den)

#         new_num = self.__num*least_comm_mult + other.__den*least_comm_mult
#         new_gcd = gcd(new_num,least_comm_mult)
        
#         return Fraction(new_num//new_gcd,least_comm_mult//new_gcd)

# solution
from copy import deepcopy
from math import gcd


class Fraction:
    def __init__(self, N, D=1):
        if type(N)==int and type(D)==int and D>0:
            if N < 0: 
                self.__sign = "-"
                N = abs(N)
            else:
                self.__sign = "+"
            self.__num = N   
            self.__den = D 
        else: #in case of erroneus initialization, instantiate everything to None
            self.__sign = None 
            self.__num = None
            self.__den = None

    def get(self):
        return self.__sign, self.__num, self.__den
    
    def value(self,d):
        if self.__sign == '+':
            return round(self.__num/self.__den,d)
        else:
            return round(-self.__num/self.__den,d)

    def reduce(self):
        factor=gcd(self.__num,self.__den)
        if factor>1:
            self.__num=self.__num//factor # int
            self.__den=self.__den//factor # int
        return self

    def __eq__(self, other):
        sc = deepcopy(self)
        oc = deepcopy(other)
        sc.reduce() 
        oc.reduce()
        return sc.__sign==oc.__sign and sc.__num==oc.__num and sc.__den==oc.__den
    
    def __str__(self):
        return self.__sign+str(self.__num)+"/"+str(self.__den)
    
    def __add__(self, other):
        ss, sn, sd = self.__sign, self.__num, self.__den 
        os, on, od = other.__sign, other.__num, other.__den
        if ss == '+' and os == '+':
            num = sn * od + on * sd
        elif ss == '+' and os == '-':
            num = sn * od - on * sd
        elif ss == '-' and os == '+':
            num = on * sd - sn * od
        else:
            num = - sn * od - on * sd
        den = sd * od
        f = Fraction(num, den)
        f.reduce()
        return f
# print(Fraction(13,39)+Fraction(14,42))
# print(Fraction(13,39)+Fraction(-14,42))
# print(Fraction(-2,3)+Fraction(13,39))
# print(Fraction(-14,42)+Fraction(-2,3))
# print(Fraction(2**56,10*2**56)+Fraction(1,10))

