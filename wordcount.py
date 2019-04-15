# put your code here.
def count_words(filename):

    # open_file = open(filename)
    word_counts = {}

    with open(filename) as open_file:
        for line in open_file:
            line = line.rstrip()
            line = line.split(" ")
            for word in line:
                word_counts[word] = word_counts.get(word, 0)+1

    for keys in word_counts:
        print(f"{keys} {word_counts[keys]}")
    # open_file.close()

count_words("twain.txt")
