import os

# printing header

print ("Paragraph Anaylsis")
print ("-------------------------------")


# Counting words

num_words = 0
 
with open('MasterPara.txt', 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Approximate Word Count: ")
print(num_words)

# Counting sentences

sentence = line.split('.')
num_sent += len(sentence)
print "Approximate Sentence Count: "
print(num_sent)

# Getting letter count

avr = sum(map(len, words))/len(words)
print("Average Letter Count: ")
print(avr)

# Getting average sentence length in words.

print("Average Sentence Length: ")
print



