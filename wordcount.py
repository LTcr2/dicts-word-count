# put your code here.
def count_words(filename):

    # open_file = open(filename)(Ashley explained that the concept of "with")
    word_counts = {}

    with open(filename) as open_file:
        for line in open_file:
            line = line.rstrip()
            line = line.split(" ")
            for word in line:
                word_counts[word] = word_counts.get(word, 0)+1

    for keys, number in word_counts.items():
        print(f"{keys} {number}") #refactored to implement the .items function
    # open_file.close() (Removed duirng Ashley's explanation)

count_words("test.txt")
