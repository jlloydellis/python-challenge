import os

with open('MasterPara.txt', 'r') as file:
    file_contents = file.read()
    
    # Count words

    Words = len(file_contents.split())

    # Count sentences

    Sentences = file_contents.count('.')

    # Get average word length
    
    Characters = len(file_contents)
    WordLeng = Characters / Words

    # Get average sentence length

    SentLeng = sum(len(x.split() for x in Sentences) / len(Sentences)

    # Print results

    print 'Paragraph Analysis'
    print '------------------------------'
    print'Approximate Word Count: ', Words
    print'Approximate Sentence Count: ', Sentences
    print'Average Word Length: ', WordLeng
    print'Average Sentence Length: ', SentLeng
	