'''
find the shortest word in a sentence
'''
sentence = input("Enter a sentence: ")
words = sentence.split()
if words:
    print("Shortest word:", min(words, key=len))
else:
    print("No words found")
