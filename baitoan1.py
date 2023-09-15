s = input()
count,sum  = 0,0 
for i in s :
    if ( i.isnumeric()):
        count+=1
        sum+=int(i)

print("Tổng các số là : {0}".format(sum))
print("Trung bình các số : {0}".format(sum/count))