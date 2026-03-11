word = input("Enter a word to check if it's a palindrome: ")  
word = word.replace(" ", "").lower()
reversed_word = word[::-1]

if word == reversed_word:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

