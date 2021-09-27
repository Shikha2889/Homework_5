import random
import string

def string_stats(s):
    d=dict()
    length = len(s)
    d['Length:'] = length
    

    words = len(s.split())
    d['Words:'] = words
    

    exclamation_count = s.count('!')
    d['Exclamation_count'] = exclamation_count
    

    return d


def random_letter():

    return random.choice(string.ascii_uppercase)
    #alternatively we can use a string of letters instead of string module
    #return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    



sentence = input("Enter a sentence to know the number of words,characters and ! :")
data =string_stats(sentence)
print(data)

generated_letter = random_letter()
print(generated_letter)


