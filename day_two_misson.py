def find_sublist_in_string(sublist, long_string):
    """Find items from a small string list present in a longer string."""
    found_items = ""
    for idx, item in enumerate(sublist):
        if item in long_string:
            found_items += str(idx + 1)
        
    return found_items

# Example usage:
small_list = ["one", "two", "three", "four","five", ]
long_string = "the nums are fouronegtwobthree1a2"

found_items = find_sublist_in_string(small_list, long_string)

print("Found items in the long string:", found_items)
