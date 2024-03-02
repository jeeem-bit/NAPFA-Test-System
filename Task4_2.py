import sqlite3

def write_student(filename):
    with open(filename, "r") as f:
        result = []
        line = f.readline()
        while line:
            result.append(line[:-1])
            line = f.readline()
    print(result)
    for s in result[1:]:
        MatricNo, Name, Class, IndexNo, Gender, BirthYear = s.split(",")
        conn = sqlite3.connect('napfa.db')
        conn.execute("""INSERT INTO Student VALUES (?,?,?,?,?,?)""", (MatricNo, Name, Class, IndexNo, Gender, BirthYear))
        conn.commit()
        conn.close()
    

#write_student("students.csv")


def write_standard(filename):
    with open(filename, "r") as f:
        result = []
        line = f.readline()
        while line:
            result.append(line[:-1])
            line = f.readline()
    print(result)
    for s in result:
        temp = s.split(',')
        Age, Gender, Item, FEDCB = temp[0], temp[1], temp[2], (temp[3]+","+temp[4]+","+temp[5]+","+temp[6]+","+temp[7])
        print(Age, Gender, Item, FEDCB)
        conn = sqlite3.connect('napfa.db')
        conn.execute("""INSERT INTO Standard VALUES (?,?,?,?)""", (Age, Gender, Item, FEDCB))
        conn.commit()
        conn.close()

#write_standard("standards.csv")

def write_results(filename):
    with open(filename, "r") as f:
        result = []
        line = f.readline()
        while line:
            result.append(line[:-1])
            line = f.readline()
    print(result)
    for s in result[1:]:
        temp = s.split(',')
        MatricNo, Year, result = temp[0], temp[1], (temp[2]+","+temp[3]+","+temp[4]+","+temp[5]+","+temp[6])
        print(MatricNo, Year, result)
        conn = sqlite3.connect('napfa.db')
        conn.execute("""INSERT INTO Result VALUES (?,?,?)""", (MatricNo, Year, result))
        conn.commit()
        conn.close()


write_results("results.csv")
