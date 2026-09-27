
#%%
def capitalize_title(title):
    return title.title()

print(capitalize_title("my hobbies"))

#👉 .title() coloca a primeira letra de cada palavra em maiúscula.

#%%

def check_sentence_ending(sentence):
    return "." in sentence

print(check_sentence_ending("I like to hike, bake, and read."))

#%%

def clean_up_spacing(sentence):
    return sentence.strip()

print(clean_up_spacing(" I like to go on hikes with my dog.  "))

#%%

def replace_word_choice(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)

print(replace_word_choice("I bake good cakes.", "good", "amazing"))