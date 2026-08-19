#%%

def add_prefix_un(word):
    return "un" + word 
print(add_prefix_un("happy"))
print(add_prefix_un("manageable"))

#%%

def make_word_groups(vocab_words):
    return " :: ".join(vocab_words).replace(" :: ", " :: " + vocab_words[0])
    
print(make_word_groups(['en', 'close', 'joy', 'lighten']))
print(make_word_groups(['pre', 'serve', 'dispose', 'position']))
print(make_word_groups(['auto', 'didactic', 'graph', 'mate']))
print(make_word_groups(['inter', 'twine', 'connected', 'dependent']))

#%%

def remove_suffix_ness(word):
    word = word[:-4]
    
    if word[-1] == "i":
        word = word.replace("i", "y")
        
    return word     

print(remove_suffix_ness("heaviness"))
print(remove_suffix_ness("sadness"))

#%%

def adjective_to_verb(sentence, index):
    words = sentence.split()
    word = words[index].strip(".")
    return word + "en"

print(adjective_to_verb("I need to make that bright.", -1))
print(adjective_to_verb("It got dark as the sun set.", 2))