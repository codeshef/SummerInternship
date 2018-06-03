import os
path = "/home/anchal/SummerInternship/Day4"
os.chdir(path)





if not os.path.isdir(path+"/CSVs"):
    os.mkdir(path + "/CSVs")

os.chdir(path+"/CSVs")

print(os.getcwd())
with  open("employee.csv", 'a+') as f:

    f.seek(0)
    # file.write("foo,hoo")
    print(f.read())

    # columns = []
    # file.write("hello,world")
    #
    # columns= list(input("Enter column names : ").split(" "))
    # columns = ','.join(columns)
    # line = file.read()
    # print(line)
    # file.write("Bryce, 34, NYC, 67000\n")
