print("Enter the word")
word=input()
strlen=len(word)
news=word[strlen::-1]
if (news==word):
    print("It is a Palindrome")
else:
    print("Not palindrome")