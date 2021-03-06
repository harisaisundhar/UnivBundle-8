# -*- coding: utf-8 -*-
"""GA_fitness_function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g1URhgjo49rN2UVta9uIXH2pV9_W5Qs2
"""

import math
from random import random
from IPython.display import display
import pandas as pd

def rastrigin_function(x,y,maximisation):
  f_x = pow(x*x+y-11,2)+pow(x+y*y-7,2)
  if maximisation:
    F_x = f_x
  else:
    F_x = 1 / ( 1 + f_x)
  return round(f_x,5),round(F_x,5)


def binary_decoding(xb,ll,ul,no_of_bits):
   xd = int(str(xb),2)
   xi = ll + (ul-ll) * (xd/(pow(2,no_of_bits)-1))
   return round(xi,5)

def printTable(print_set):
    df = pd.DataFrame(print_set)
    display(df)
    
def selection(population,objective,fitness):
    cummulative = []
    random_number = []
    new_population = []
    
    s = 0
    probability = []
    for i in range(len(fitness)):
        p = fitness[i] / sum(fitness)
        probability.append(p)

    for i in range(len(fitness)):
        s = s + probability[i]
        cummulative.append(s)
    '''for i in range(len(fitness)):
        random_number.append(random())'''
    random_number = ['0.472','0.108','0.723','0.536','0.931','0.972']
    s_no_new=[]
    for i in range(len(fitness)):
        for j in range(len(fitness)):
            if cummulative[j] > float(random_number[i]):
                new_population.append(population[j])
                s_no_new.append(j+1)
                break
    print_set = {"population":population,"objective":objective,"fitness": fitness,"probability":probability, "cummulative": cummulative, "random_number": random_number, 
                 "new_population":new_population,"new_population_sequence_number":s_no_new}
    printTable(print_set)


x_val = ['1110010000','0001001101','1010100001','1001000110','1100011000','0011100101']
y_val = ['1100100000','0011100111','0111001000','1000010100','1011100011','0011111000']
fx=[]
Fx=[]
population =[]

ll = 0
ul = 6
bits=10

for i in range(len(x_val)):
    x_val[i] = binary_decoding(x_val[i],ll,ul,bits)
    y_val[i] = binary_decoding(y_val[i],ll,ul,bits)
    ox, Ox = rastrigin_function(x_val[i], y_val[i], False)
    population.append((x_val[i],y_val[i]))
    fx.append(ox)
    Fx.append(Ox)

selection(population,fx,Fx)
