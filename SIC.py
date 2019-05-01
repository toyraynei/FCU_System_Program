def PassOne(data):
    data_copy = data.copy()
    counter = []
    symtable = {}
    index = 0

    #預設assembly開頭必定為START且有label name
    start = data_copy[0].split()
    if (start[1] == "START"):
        if (len(start[0]) > 6):
            print("ERROR")
            exit(0)
        symtable[start[0]] = int(start[2])
        counter.append(int(start[2]))
        counter.append(int(start[2]))
        data_copy.pop(0)

    for i in data_copy:
        i = i.split()[0:3] #分割字串並去除註解
        index += 1
        if (len(i) == 3):
            if (i[0] in Opcode):
                print("Label name is Opcode???") #判斷label name是否為Opcode
                exit(0)
            
            if (i[0] in symtable): #判斷label name是否重複
                print("label name already exists")
                exit(0)
            else:
                symtable[i[0]] = counter[index]
            if (i[1] == "END"):
                return counter, symtable
            elif (i[1] == "WORD"):
                counter.append(counter[index] + 3)
            elif (i[1] == "BYTE"):
                lens = int(len(i[2][2:-1]))
                if (i[2][0:1] == "C"):
                    counter.append(counter[index] + 1 * lens)
                elif (i[2][0:1] == "X"):
                    if (len(i[2][2:-1]) % 2 != 0):
                        print("Invalid length of hex encoding " + i[2][1:])
                        exit(0)
                    else:
                        counter.append(counter[index] + 1 * int(lens / 2))
            elif (i[1] == "RESW"):
                counter.append(counter[index] + 3 * int(i[2]))
            elif (i[1] == "RESB"):
                counter.append(counter[index] + 1 * int(i[2]))
            else:
                if (i[1] in Opcode):
                    counter.append(counter[index] + 3)
                else:
                    print("Invalid Command")
                    exit(0)
        elif (len(i) == 2):
            if (i[0] == "END"):
                return counter, symtable
            elif (i[0] in Opcode):
                counter.append(counter[index] + 3)
            else:
                print("Invalid Command")
                exit(0)
        else:
            print("Invalid Command")
            exit(0)

def PassTwo(data, passone, symtable):
    obj = []
    j = -1
    data_copy = data.copy()
    
    for i in data_copy:
        j += 1
        if (j == 0):
            obj.append("      ")
        else:
            i = i.split()[0:3]
            if (len(i) == 3):
                if (i[1] in Opcode):
                    X = i[2].split(",")
                    if (len(X) == 2):
                        if (X[1] != "X"):
                            print("ERROR")
                            exit(0)
                        else:
                            sp = symtable[X[0]] + 32768
                    else:
                        sp = symtable[X[0]]
                    tmp = Opcode[i[1]] + "0" * (6-len(hex(sp))) + "%X" % sp
                elif (i[1] == "END"):
                    return obj
                elif (i[1] == "WORD"):
                    tmp = "0" * (8-len(hex(int(i[2])))) + "%X" % int(i[2])
                elif (i[1] == "BYTE"):
                    if (i[2][0:1] == "X"):
                        tmp = i[2][2:-1]
                    elif (i[2][0:1] == "C"):
                        tmp = i[2][2:-1].encode("utf-8").hex()
                elif (i[1] == "RESW" or i[1] == "RESB"):
                    tmp = "000000"
            elif (len(i) == 2):
                if (i[0] in Opcode):
                    X = i[1].split(",")
                    if (len(X) == 2):
                        if (X[1] != "X"):
                            print("ERROR")
                            exit(0)
                        else:
                            sp = symtable[X[0]] + 32768
                    else:
                        sp = symtable[X[0]]
                    tmp = Opcode[i[0]] + "0" * (6-len(hex(sp))) + "%X" % sp
                elif (i[0] == "END"):
                    return obj
                else:
                    print("ERROR")
                    exit(0)
            obj.append(tmp)                        

def write (data, obj, loc):
    obj_copy = obj.copy()
    loc_copy = loc.copy()
    tmp = ""
    flag = 1
    recode = ""
    f = open("OBJFILE", "w")
    
    start = data[0].split()[0]
    pro_len = loc_copy[-1] - loc_copy[1]
    f.write("H" + start + " " * (6-len(start)) + "0" * (8-len(hex(loc_copy[1]))) + "%X" % loc_copy[0] + "0" * (8-len(hex(pro_len))) + "%X" % pro_len + "\n")
    obj_copy.pop(0)
    loc_copy.pop(0)
    
    while (True):
        if (len(loc_copy) == 1):
            if (len(tmp) <= 30):
                t = hex(int(len(tmp) / 2))
                f.write("T" + recode + "0" * (4-len(t)) + "%X" % int(len(tmp)/2) + tmp + "\n")
            else:
                f.write("T" + recode + "0" * (8-len(tmp)) + "%X" % int(len(tmp)/2) + tmp + "\n")
            break
        elif (flag == 1):
            recode = "0" * (8-len(hex(loc_copy[0]))) + "%X" % loc_copy[0]
            flag = 0
        
        while (obj_copy[0] == "000000"):
            if (len(obj_copy) == 1):
                loc_copy.pop(0)
                flag = 1
                break
            if (len(tmp) == 0):
                loc_copy.pop(0)
                obj_copy.pop(0)
            else:
                if (len(tmp) <= 30):
                    t = hex(int(len(tmp) / 2))
                    f.write("T" + recode + "0" * (4-len(t)) + "%X" % int(len(tmp)/2) + tmp + "\n")
                else:
                    f.write("T" + recode + "0" * (8-len(tmp)) + "%X" % int(len(tmp)/2) + tmp + "\n")
                flag = 1
                tmp = ""
        
        if (len(tmp) + len(obj_copy[0]) > 60):
            f.write("T" + recode + "0" * (8-len(tmp)) + "%X" % int(len(tmp)/2) + tmp + "\n")
            flag = 1
            tmp = ""
            
        if (flag == 0):
            tmp += obj_copy[0]
            loc_copy.pop(0)
            obj_copy.pop(0)
    
    end = data[-1].split()
    if (len(end) == 3):
        key = end[2]
    else:
        key = end[1]
    
    end = symtable[key]
    f.write("E" + "0" * (8-len(hex(end))) + "%X" % end)

Opcode = {
    "ADD" : "18", "AND" : "40", "COMP" : "28", "DIV" : "24", "J" : "3C",
    "JEQ" : "30", "JGT" : "34",  "JLT" : "38", "JSUB" : "48", "LDA" : "00",
    "LDCH" : "50", "LDL" : "08", "LDX" : "04", "MUL" : "20", "OR" : "44",
    "RD" : "D8", "RSUB" : "4C", "STA" : "0C", "STCH" : "54", "STL" : "14",
    "STX" : "10", "SUB" : "1C", "TD" : "E0", "TIX" : "2C", "WD" : "DC"
}

load_asm = open("source.asm", "r")
data = load_asm.readlines()

loc, symtable = PassOne(data)
obj = PassTwo(data,loc, symtable)
write(data, obj, loc)