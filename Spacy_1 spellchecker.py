import spacy
from spellchecker import SpellChecker

# create a spell checker object
nlp=spacy.load("en_core_web_sm")
spell = SpellChecker()
counter=0
# load the text to check
doc = nlp("Ths is a sampl sentnce with sme speling errrs.")

# split the text into individual words
words = doc.text.split()

# find misspelled words
misspelled = spell.unknown(words)
rightspelled=spell.known(words)
# print the misspelled words
print("Misspelled words:")

for word in misspelled:
        counter +=1
        print(word)
        

# correct the misspelled words
corrected = [spell.correction(word) for word in words]

# print the corrected text
print("\nCorrected text:")
print(" ".join(corrected))
print(f"Typo:{counter}")
print(f"{misspelled}")
print(f"{rightspelled}")
#Regarding the order of print(f"{misspelled}"), 
#the order of the items returned by the spell.unknown() method is not guaranteed to be consistent,
#as it depends on the order of the internal data structures used by the SpellChecker class. 
# Therefore, the order of the misspelled words printed by this line of code may be different each time 
# you run the program. If you want to print the misspelled words in a specific order, 
# you can sort the misspelled list before printing it.