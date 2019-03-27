x=[]
ordered={'smallest': 0, 'greater': 0, 'greatest': 0}
while len(x) != 3:
    try:
        number = input("Enter number: ")
        x.append(int(number))
    except ValueError:
        try:
            x.append(float(number))
        except ValueError:
            print("\nPlease input a number\n")
x.sort()
count=0
for key in ordered:
    ordered[key]=x[count]
    count += 1
print("\n"+str(ordered['greater']*ordered['greatest']))