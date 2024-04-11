import itertools

# Find all permutations of a scrabmbled string, and compare to valid word dictionary
def unscramble_word(scrambled_word, dictionary):
    permutations = itertools.permutations(scrambled_word)
    for permutation in permutations:
        word = "".join(permutation)
        if word in dictionary:
            return word

    return "shit so broke"

if __name__ == "__main__":
    # Build valid word dictionary
    good_word_file = input("Select a file for the dictionary: ")
    good_word_list = []

    with open(good_word_file) as fp:
        good_word_list = [str(line.strip()) for line in fp.readlines()]

    # Build scrambled word dictionary
    bad_word_file = input("Select a file for the unscrambled words: ")
    bad_word_list = []
    with open(bad_word_file) as fp:
        bad_word_list = [line.strip() for line in fp.readlines()]

    # Build dictionary of unscrambled words
    out_word_list = []
    for bad_word in bad_word_list:
        out_word_list.append(unscramble_word(bad_word, good_word_list))

    # Display unscrambled word list
    print(",".join(out_word_list))