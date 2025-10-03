"""programming_glossary."""
programming_glossary = {
    'Variable': 'A variable is used to store data values.',
    'Function': 'A function is a block of code that only runs when it is called.',
    'Loop': 'A loop is used to repeat a block of code multiple times.',
    'List': 'A list is a collection of items in a particular order.',
    'Dictionary': 'A dictionary is a collection of key-value pairs.'
}

for term in programming_glossary:
    difinition = programming_glossary[term]
    print(f"{term} : {difinition}")

programming_glossary1 = {
    'Variable': 'A variable is used to store data values.',
    'Function': 'A function is a block of code that only runs when it is called.',
    'Loop': 'A loop is used to repeat a block of code multiple times.',
    'List': 'A list is a collection of items in a particular order.',
    'Dictionary': 'A dictionary is a collection of key-value pairs.',
    'Tuple': 'An immutable sequence of items.',
    'Set': 'A collection of unique items.',
    'Boolean': 'A data type with only True or False.',
    'String': 'A sequence of characters.',
    'Integer': 'A whole number, positive or negative.'
    }
for term, definition in programming_glossary1.items():
    print(f"{term}:\n{definition}\n")
