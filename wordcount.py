# put your code here.
def count_words(filename):

    open_file = open(filename)
    word_counts = {}


    for line in open_file:
        line = line.split(" ")
        for word in line:
            word_counts[word] = word_counts.get(word, 0)+1

    for keys in word_counts:
        print(f"{keys} {word_counts[keys]}")

count_words("test.txt")
