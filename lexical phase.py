import re
def tokenize(order):
    token_regex = r"[\w]+|[\+\-*/=<>!\?]|[\(\)\{\}]|[:;,.]"  
    tokens = re.findall(token_regex, order)  
    return tokens

order = " p384rj*/56+-/57/631*/6+97rfmdi8frint(x); }"
tokens = tokenize(order)
print("Generated tokens:", tokens)
