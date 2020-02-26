numlist=["d","f","g","h"]

for a in numlist:
    for b in numlist:
        for c in numlist:
            if a!=b and b!=c and c!=a :
                print(a,b,c)
     