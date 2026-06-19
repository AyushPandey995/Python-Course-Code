text = input("Enter a word- ")
reverse_text = text[::-1]
if text == reverse_text:
    print("The word is Palindrome!!!")
else:
    print("Not a Palindrome")