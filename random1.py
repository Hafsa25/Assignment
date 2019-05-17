import random
arr=[]
for i in range(101):
    arr.append(random.randint(1,10000))
print("What do you want to do with this list?")
print("1: Find the minimum")
print("2: Find the maximum")
print("3: Find the average")
choice=int(input())
#MINIMUM NUMBER OF RANDOM LIST
if choice==1:
    min=arr[0]
    for i in range(len(arr)):
            if min>arr[i]:
                min=arr[i]     
    print("Minimum number of this list is",min,"at index",arr.index(min))
#MAXIMUM NUMBER OF RANDOM LIST    
elif choice==2:
    max=arr[0]
    for i in range(len(arr)):
            if max<arr[i]:
                max=arr[i]     
    print("Maximum number of this list is",max,"at index",arr.index(max))
#MEAN OF RANDOM LIST
elif choice==3:
    mean=0
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    mean=sum/len(arr)
    print("Mean of all values of this list is",mean)


