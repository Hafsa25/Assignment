print(" ******* 9TH MARKSHEET*******")
print("CODED BY HAFSA BHATTI")
print("Enter your Roll number")
roll_no=int(input())
print("What did you chose in 9th? Biology or Computer?")
choice=input()
if choice=="Biology":
    final=choice
elif choice=="Chemistry":
    final=choice
print("Enter your Sindhi marks out of 75:")
sindhi=int(input())
print("Enter your Pakistan Studies marks out of 75:")
pst=int(input())
print("Enter your English marks out of 75:")
eng=int(input())
print("Enter your Chemistry marks out of 100:")
chem=int(input())
print("Enter your ",final," marks out of 100:")
fin=int(input())
percent=((sindhi+pst+eng+chem+fin)/425)*100
if percent>=80:
    print("Congratulations Roll no ",roll_no," you got A+ grade with ",percent,"%")
elif percent<=79 & percent>=70:
    print("Good! Roll no ",roll_no,"you got A grade with ",percent,"%")
elif percent<=69 & percent>=60:
    print("Roll no ",roll_no,"you got B grade with ",percent,"%")
elif percent<=59 & percent>=50:
    print("Roll no ",roll_no," you got C grade with ",percent,"%")
else:
    print("Roll no ",roll_no,"You are fail with  ",percent,"%")
