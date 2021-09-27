
def string_stats(s):
    d=dict()
    length = len(s)
    d['Length:'] = length
    

    words = len(s.split())
    d['Words:'] = words
    

    exclamation_count = s.count('!')
    d['Exclamation_count'] = exclamation_count
    

    return d


    



sentence = input("Enter a sentence to know the number of words,characters and ! :")
data =string_stats(sentence)
print(data)



