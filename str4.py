str="P@#yn26at^&i5ve"
charCount,digitCount,symbolCount=0,0,0
for s in str:
    if s.isalpha():
        charCount+=1
    elif s.isdigit():
        digitCount+=1
    else:
        symbolCount+=1
print(f"DigitCount=(digitCount),charCount={charCount},symbolCount={symbolCount}")
