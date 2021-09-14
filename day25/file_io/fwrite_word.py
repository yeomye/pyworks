with open('word.txt', 'w') as f:
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 'strawberry', 'grape', 'garlic', 'onion', 'potato']

    for w in word:
        f.write(w + ' ')