num=142
temp=num
for i in range(1,300):
    temp=i
    arm=0
    while(i!=0):
        r=i%10
        arm=arm+r*r*r
        i=i//10
    if arm==temp:
        print(arm,"No is armstrong")


