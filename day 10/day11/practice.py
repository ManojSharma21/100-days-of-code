""" iven an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not n  is weird."""
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(raw_input())
    if(N%2==0): 
        if(1<=N<=5):
            print ("Not Weird")
        if(6<=N<=20):
            print("Weird")
        if(21<=N<=100):
            print("Not Weird")
    else:  
        print ("Weird")
