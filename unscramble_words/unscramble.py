import itertools

class WordNotUnscramblable(Exception):
    pass

# Find all permutations of a scrabmbled string, and compare to valid word dictionary
def unscramble_word(scrambled_word, dictionary):
    permutations = itertools.permutations(scrambled_word)
    for permutation in permutations:
        word = "".join(permutation)
        if word in dictionary:
            return word

    raise WordNotUnscramblable("No valid word found")

if __name__ == "__main__":
    # Build valid word dictionary
    good_word_file = input("Select a file for the dictionary: ")
    good_word_list = []

    try:
        with open(good_word_file) as fp:
            good_word_list = [str(line.strip()) for line in fp.readlines()]
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        exit()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        exit()
    
    # Build scrambled word dictionary
    bad_word_file = input("Select a file for the unscrambled words: ")
    bad_word_list = []
    try:
        with open(bad_word_file) as fp:
            bad_word_list = [line.strip() for line in fp.readlines()]
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        exit()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        exit()

    # Build dictionary of unscrambled words
    out_word_list = []
    errors = []
    for bad_word in bad_word_list:
        try:
            out_word_list.append(unscramble_word(bad_word, good_word_list))
        except WordNotUnscramblable:
            print(f"Scrambled word {bad_word} was not in dictionary.")
            errors.append(bad_word)

    # Display unscrambled word list
    print(",".join(out_word_list))
    if errors:
        print(f"{len(errors)} words could not be unscrambled. {",".join(errors)}")