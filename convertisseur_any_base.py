base = int(input("Which base? "))
nbaconv = int(input("Which number should converted to base-{}? ".format(base)))
lst = []
while nbaconv > 0:
    q = nbaconv // base
    r = nbaconv % base
    if r >= 10 and r <= 20:
        if r == 10:
            prt = "A"
        elif r == 11:
            prt = "B"
        elif r == 12:
           prt = "C"
        elif r == 13:
           prt = "D"
        elif r == 14:
           prt = "E"
        elif r == 15:
           prt = "F"
        elif r == 16:
           prt = "G"
        elif r == 17:
            prt = "H"
        elif r == 18:
            prt = "I"
        elif r == 19:
            prt = "J"
        elif r == 20:
            prt = "K"
    elif r >= 21 and r <= 30:    
        if r == 21:
            prt = "L"
        elif r == 22:
            prt = "M"
        elif r == 23:
            prt = "N"
        elif r == 24:
            prt = "O"
        elif r == 25:
            prt = "P"
        elif r == 26:
            prt = "Q"
        elif r == 27:
            prt = "R"
        elif r == 28:
            prt = "S"
        elif r == 29:
            prt = "T"
    elif r >= 30:
        if r == 30:
            prt = "U"
        elif r == 31:
            prt = "V"
        elif r == 32:
            prt = "W"
        elif r == 33:
            prt = "X"
        elif r == 34:
            prt = "Y"
        elif r == 35:
           prt = "Z"
    else:
        prt = r
    lst.append(prt)
    nbaconv = q
lst.reverse()
print("".join(map(str, lst)))
