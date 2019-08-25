import matplotlib.pyplot as plt
import pprint
from string import ascii_lowercase as letters


def read_and_count_letters(to_read):
    # Open the file that is passed in as an argument to the function
    with open(to_read, encoding='utf-8') as f:
        text = f.read().lower()
        text_count = dict((l, text.count(l)) for l in letters)
        # Sorting the returned data to be processed further
        text_sort = sorted(text_count.items(), key=lambda x: x[1], reverse=True)
        # Printing the returned data to the command line
        pprint.pprint(text_sort)

    # Initialising a new matplotlib bar graph illustrating the occurences of letters detected in the text file
    plt.bar(*zip(*text_count.items()))
    plt.show()

# Enter the .txt document you wish to process between the two apostrophes below


to_read = ''
read_and_count_letters(to_read)