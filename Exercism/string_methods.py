
#%%
def capitalize_title(title):
    return title.title()

print(capitalize_title("my hobbies"))

#👉 .title() coloca a primeira letra de cada palavra em maiúscula.

#%%

def check_sentence_ending(sentence):
    return "." in sentence

print(check_sentence_ending("I like to hike, bake, and read."))