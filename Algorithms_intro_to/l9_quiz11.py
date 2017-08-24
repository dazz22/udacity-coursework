import csv
with open('l9_quiz11_names.txt','rb') as names:
    Fname = []
    for name in names:
        if name.split(',')[1] == "F":
            Fname.append(name)
            
    Fname.sort(key=lambda x: int(x.split(',')[2]))
    print(Fname[-2])
