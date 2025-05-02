#program to reverse the words in given string

str="Data Analysis using python"
list2=str.split()[::-1]
str2=" ".join(list2)
print(str2)

#to find the length of the string

str="Data Analysis using Python"
list2=str.split()
for word in list2:
    print(word,len(word))

#count number of vowels

str="Data Analysis using python"
list3=['a','e','i','o','u']
for n in list3:
    count=0
    for char in str:
        if char==n:
            count+=1
    print(f"Number of {n} in str",count)
 

