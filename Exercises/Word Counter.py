string = input('Please insert the paragraph that you want to count the number of words in it.')

words = string.split()
word_counter ={}

for word in words:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1 

print(word_counter)