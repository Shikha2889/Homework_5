import random
import string

def random_letter():
    
    return random.choice(string.ascii_uppercase)
    #alternatively we can use a string of letters instead of string module
    #return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

generated_letter = random_letter()
print(generated_letter)
