def main(p,n,d,e,f):
    from random import randint
    q = p - 1
    list=[]
    list1=[]
    r=1
    while q>=0:
        s=1
        if r==1 and e==0:
            name = input(f"\nEnter {r}st player name : ")
        elif r==2 and e==0:
            name = input(f"\nEnter {r}nd player name : ")
        elif r==3 and e==0:
            name = input(f"\nEnter {r}rd player name : ")
        elif r>3 and e==0:
            name = input(f"\nEnter {r}th player name : ")
        elif r==1 and e!=0:
            name = print(f"{r}st player {f[r-1]}")
            list.append(f[r-1])
        elif r==2 and e!=0:
            name = print(f"\n{r}nd player {f[r-1]}")
            list.append(f[r - 1])
        elif r==3 and e!=0:
            name = print(f"\n{r}rd player {f[r-1]}")
            list.append(f[r - 1])
        elif r>3 and e!=0:
            name = print(f"\n{r}th player {f[r-1]}")
            list.append(f[r - 1])
        r=r+1
        count = 0
        i = n-1
        while i>=0:
            randomnumber = randint(1,d)
            if s == 1:
                n1 = int(input(f"Enter {s}st number : "))
            elif s == 2:
                n1 = int(input(f"Enter {s}nd number : "))
            elif s == 3:
                n1 = int(input(f"Enter {s}rd number : "))
            else:
                n1 = int(input(f"Enter {s}th number : "))
            if n1 == randomnumber:
                count = count+1
            i=i-1
            s=s+1
        q = q-1
        if e==0:
            list.append(name)
        list1.append(count)
    max1=max(list1)
    pos=list1.index(max1)
    win=list[pos]
    list2=[]
    pos1=0
    for x in list1:
        if x == max1:
            list2.append(list[pos1])
        pos1=pos1+1
    if len(list2)<=1:
        print(f" \nCongratulation (((***{win}***))), you have win the match.\n")
        i = 0
        for x in list:
            print(f"Point of {x} is {list1[i]}")
            i = i + 1
    else:
        print(f" \nDraw the game between ", end="")
        if len(list2) == 2:
            print(f"{list2[0]} and {list2[1]}", end="")

        elif len(list2) == 3:
            print(f"{list2[0]}, {list2[1]} and {list2[2]}", end="")

        else:
            print("a = ", end="")
            for i in range(1, len(list2) - 1):
                print(f"{i}, ", end="")
            print(f"{list2[-2]} and {list2[-1]}", end="")
        print(f" with point {max1}.")

        for x in list:
            print(f"Point of {x} is {list1[i]}")
            i = i + 1
            p=len(list2)
            e=e+1

        print(f" \nAgain match between ", end="")
        if len(list2) == 2:
            print(f"{list2[0]} and {list2[1]}.")

        elif len(list2) == 3:
            print(f"{list2[0]}, {list2[1]} and {list2[2]}.")

        else:
            print("a = ", end="")
            for i in range(1, len(list2) - 1):
                print(f"{i}, ", end="")
            print(f"{list2[-2]} and {list2[-1]}.")

        f=list2
        main(p,n,d,e,f)

p = int(input("Number of player   : "))
n = int(input("number of chance   : "))
d = int(input("Duration of number : "))
e = 0
f=[]
main(p,n,d,e,f)
