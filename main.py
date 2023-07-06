#!/usr/bin/env python

import random

def main():
    """Start a genre music guessing game between jazz - rock - disco- classical - hip hop - alternative."""
    print("Guess the genre music!")
    
    music = ["jazz", "rock", "disco", "classical", "hip hop", "alternative"]
    
    
    x = random.choice(music)
    guess = None 
    
    while x != guess:
        
        guess = str(input("pick a genre music between jazz, rock, disco, hip hop, classical, alternative: "))
        
        if x == guess:
            print("You genius!")
        else:
            print("Try again.")
main()