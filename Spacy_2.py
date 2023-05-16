import spacy
nlp=spacy.load("en_core_web_sm")
doc=nlp("Apple is looking at buying U.K Startup for $1 billion")
counter=0
stopcounter=0
stopword=[]
nonstopword=[]

for token in doc:
    print(token.text, token.lemma_, token.pos_,token.dep_, token.is_stop)
    if token.is_stop == False:
        counter +=1
        nonstopword.append(token.text)
    else:
        stopcounter +=1
        stopword.append(token.text)

print(f"Number of stopword:{stopcounter}", f"Number of non-stopword:{counter}")
print(f"Nonstopwords:{nonstopword}")
print(f"Stopwords:{stopword}")

