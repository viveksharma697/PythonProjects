# Write a Python program to delete all occurrences of a specified character in a given string.
# Sample Output:
# Original string:
# Delete all occurrences of a specified character in a given string
# Modified string:
# Delete ll occurrences of specified chrcter in given string

def delete_all_occurrences(str1, ch):
     result = str1.replace(ch, "")
     return(result)

str_text = "Delete all occurrences of a specified character in a given string"
print("Original string:")
print(str_text)
print("\nModified string:")
ch='a'
print(delete_all_occurrences(str_text, ch))
