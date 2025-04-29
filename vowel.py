#To read a charachter from console and print it is vowel or consonant
char=input("Enter a single character")
char=char.lower()
if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
    print("It is Vowel")
else:
    print("It is Consonant")
