# script to take a word and count how many letters, how many vowels and how many consonants are in it
import sys

print("Enter your word: ")
myWord = str(input())
l = len(myWord)
v = 0
c = 0

for i in myWord:
    if(i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U'):
        v = v + 1
    elif(i == 'b' or i == 'B' or i == 'c' or i == 'C' or i == 'd' or i == 'D' or i == 'f' or i == 'F' or i == 'g' or i == 'G' or i == 'h' or i == 'H' or i == 'j' or i == 'J' or i == 'k' or i == 'K' or i == 'l' or i == 'L' or i == 'm' or i == 'M' or i == 'n' or i == 'N' or i == 'p' or i == 'P' or i == 'q' or i == 'Q' or i == 'r' or i == 'R' or i == 's' or i == 'S' or i == 't' or i == 'T' or i == 'v' or i == 'V' or i == 'w' or i == 'W' or i == 'x' or i == 'X' or i == 'y' or i == 'Y' or i == 'z' or i == 'Z'):
        c = c + 1
    else:
        print('Error. Please enter only one word without numbers.')
        #myWord = str(input())
        sys.exit()

print('Your word has %s vowel(s), %s consonant(s), and %s letter(s) in total.' % (v, c, l))