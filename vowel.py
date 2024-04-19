"""
Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.
eg " Hello World " => returns 2
"""

def vow_count(sentence):
    vowel = 'aeiouAEIOU'
    vowel_count = 0

    for char in sentence:
        if char in vowel:
            vowel_count += 1

    return vowel_count

ipt_sentence = input("Enter a sentence: ")     

print("Number of vowels:", vow_count(ipt_sentence))