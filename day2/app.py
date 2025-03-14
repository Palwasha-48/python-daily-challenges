# Aisa Python program likhna hai jo user se ek sentence le aur usme jitne words hain, count kare! 🔢💡 

# take input
sentence = input("Enter a sentence: ")

# count words
words = sentence.split()
word_count = len(words)
print(f"Total words: {word_count}")

# Bonus Challenge: Words ko reverse order me print karna
reversed_sentence = " ".join(words[::-1])
print(f"Reversed sentence: {reversed_sentence}")
