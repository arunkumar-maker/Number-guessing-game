# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 17:19:58 2022

@author: ARUN KUMAR
"""

import random
top_of_range=input("Type a number ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<0:
        print("Please input the number greater than zero(0) next time you play")
        quit()
else:
    print("Please type a number next time you play!! ")
    quit()
random_number=random.randint(0,top_of_range)
#print(random_number) 
 
# generally the while loop in python runs until the condition is satisfied
# so we always take the condition is satisfied and we break the loop whenever it requries.
guesses=0
while True:
    guesses+=1
    user_guess=input("guess a number ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Type a number next time when u play ")
        continue # here this continue statement makes the terminal to start running from while loop again
    if user_guess== random_number:
        print("Hurrah...")
        break
    elif user_guess > random_number:
        print("You are above the requried number..")
    else:
        print("You are below the requried number..")
    
print("you won the game in",guesses,"guesses")
    
    
    
    
    
    
    
    
    
    
    
    