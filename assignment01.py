import random
import string

def random_chars(length=7):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Initialize an array of random strings (with 7 characters for simplicity)
random_strings_arr = ['egp2bn6', 'PORuxX6', 'VYDDGgv', 'O3TfFAq', 'oAsT0EB', 'r63cAow', 'xQaNsMW', 'zV5SIst', 'UTfeCis', 'mW9idzW', 'yOwmfHM', '5WPypgo', 'wXzT3Hw', 'fzlBmEB', 'GbYT8SY', 'GBz0O31', 'hm9cRGL', '5JKiOe1', 'GnKKuhg', 'j6lUphQ', 'rBHxvlx', 'PsUvZBH', 'Gi47dcd', 'cXJBFHf', 'WronZ6J', 'G1Gi3bO', 'M7EN6IV', 'h2UpIdC', 'OFbYe3L', 'CpEFJ7q', 'GPOYD96', 'hXPtEWa', 'rz25iMW', 'I461I7P', 'VJVrQ8r', 'TMs9Wah', 'r3uEd3s', 'qoZ4XzK', '8gqaRc7', 'fRAtbpT', '4XHVUZh', 'MgUnsr9', 'F0VP5mt', 'AM18Fs4', 'x18an4B', 'LohNzch', 'SguSWI6', '7knMWh2', '3MZx9Sg', 'rH58nh8', 'yglvwSs', 'SwYJoDV', 'iM6kWD6', 'GjC4KKY', 'W1UPyPG', '1YFQ8Mw', 'sA9qaeY', 'UOC3R21', 'WehWgIh', 'RnquXfG', '18VSQWl', 'S92FaVh', 'NoOVQGQ', 'yTVm58Y', 'g3IO0vO', 'f2s5Mbx', '4tkSZZT', 'G1fLAAG', 'wnjc3RG', 'RVnzEmk', 'M8kpsqH', 'XEOgf6u', 'lu18HwB', '3JKsQOB', 'euXnPEo', 'Q1gcUQq', 'w4h0703']

def find_most_similar(text, arr):
    # Initialize a list to store elements with the most characters in common
    most_common_matches = []
    max_common_chars = 0

    for index, elem in enumerate(arr):
        # Check if length and order match exactly
        if len(elem) == len(text) and all(elem[i] == text[i] for i in range(len(text))):
            return elem  # Return immediately if an exact match is found

        # Count the number of matching characters in the same order
        common_chars = 0
        pattern = ""
        text_index = 0

        for char in elem:
            # Check if the current character matches the current index of `text`
            if text_index < len(text) and char == text[text_index]:
                pattern += char  # Add matching character to pattern
                common_chars += 1
                text_index += 1  # Move text index forward
            elif text_index < len(text):
                text_index += 1  # Still move text index forward for checking order

        # Update if this element has the most common characters
        if common_chars > max_common_chars:
            max_common_chars = common_chars
            most_common_matches = [elem]
        elif common_chars == max_common_chars:
            most_common_matches.append(elem)

        # Print the pattern for the current element for debugging
            if common_chars > 0:
                print(f"txt: {text} => el: {elem}; arr_index: {index} \n Pattern: \"{pattern}\", len: {common_chars}")

    # If no exact match, return the elements with the most characters in common
    return most_common_matches

result = find_most_similar(random_chars(), random_strings_arr)
print(random_chars() + ' => ' + ", ".join(result))