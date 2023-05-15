import token 
doc=("Apple is loooking at buying U.K Startup for $1 billion ****")

print(f"Data:{doc}")
for token in doc:
    print(token.star)

#sebisa mungkin token 


#The token.NOTEQUAL constant is used to represent the token value for the "!=" operator in Python.
# To use it, you can import the token module and then use the constant in your code like this:
#CODE#

#import token
# if some_variable != some_other_variable:
    # Do something

#In this example, the != operator is used to compare two variables, 
# and the token.NOTEQUAL constant is used internally by Python to represent this operator as a token.

#You generally don't need to interact directly with the token module in your code 
# unless you are doing something specific with the Python tokenizer or parser. Most Python developers will work with higher-level libraries like spacy or NLTK for natural language processing tasks.