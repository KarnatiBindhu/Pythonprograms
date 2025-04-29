
sub1=int(input("Enter marks for subject 1: "))
sub2=int(input("Enter marks for subject 2: "))                
sub3=int(input("Enter marks for subject 3: "))
if sub1>=40 and sub2>=40 and sub3>=40:
    avg=(sub1+sub2+sub3)/3               
    print("Result:Passed")
    if avg>=90:
            print("Grade: A1")
    elif avg>=80:
            print("Grade: A")
    elif avg>=70:
            print("Grade: B+")
    elif avg>=60:
            print("Grade: B")
    elif avg>=50:
            print("Grade: C")
    else:
            print("Grade:D")
else:
    print("Result:Failed")
