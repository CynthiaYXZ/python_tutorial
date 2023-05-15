import spacy
nlp=spacy.load("en_core_web_sm")

doc=nlp("Apple is loooking at buying U.K Startup for $1 billion")
#atas ada typo

#doc=nlp("Apple is looking at buying U.K Startup for $1 billion")

for token in doc:
    print(token.text, token.pos_,token.dep_,token.)

