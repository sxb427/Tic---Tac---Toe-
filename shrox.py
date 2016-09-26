import random
print "WELCOME"
print "RULES"
print "1.You play as x and i play as o"
print "2.you start"
print "The first one to get 3 in a row, coloumn or diagonal wins"
print "following are the index positions"
index=[['1','2','3'],['4','5','6'],['7','8','9']]#A matrix indicating the number associated to each position in the game  
for i in index:
    print i
print "Good luck !!! smile emoticon"
r1=[[0,0],[0,1],[0,2]]#row 1 index positios 
r2=[[1,0],[1,1],[1,2]]#row 2 index positios
r3=[[2,0],[2,1],[2,2]]#row 3 index positios 
c1=[[0,0],[1,0],[2,0]]#coloumn 1 index positios 
c2=[[0,1],[1,1],[2,1]]#coloumn 2 index positios 
c3=[[0,2],[1,2],[2,2]]#coloumn 3 index positios 
d1=[[0,0],[1,1],[2,2]]#diagonal 1 index positios 
d2=[[0,2],[1,1],[2,0]]#diagonal 2 index positios 
a1=[r1,r2,r3,c1,c2,c3,d1,d2]#List cointaining all the possible rows coloumns and diagonals
while True:
    l=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]#GAME MATRIX
    while True:
        for i in a1:#check weather x(user) has already won
            b1=0
            for j in i:
                if l[j[0]][j[1]]=='x':
                    b1=b1+1
                else:
                    break
            if b1==3:#If b1 is 3 then there exists a row, coloumn or diagonal in which all the elements are occupied by 'x'
                break
        if b1==3:
            print "game over you win"
            break
        for i in a1:#check weather o(computer) has already won
            b2=0
            for j in i:
                if l[j[0]][j[1]]=='o':
                    b2=b2+1
                else:
                    break
            if b2==3:#If b2 is 3 then there exists a row, coloumn or diagonal in which all the elements are occupied by 'o'
                break
        if b2==3:
            print "game over i win"
            break
        def emptyplace(l):#Returns a list named 'e' cointaining the index values of all vacant positions 
            e=[]
            for i in range(3):
                for j in range(3):
                    if l[i][j]==' ':
                        e.append([i,j])
            return e
        while True:#loop keeps running until user enters a valid entry (i.e a number from 1 to 9 and the position associated with the number isn't occupied"
            dic={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}#dictionary that maps the numbers to the index values
            while True:#loop keeps running till the user enters a number from 1 to 9
                try:
                    x=int(raw_input('enter index'))
                    x1=dic[x]
                    break
                except:
                    print "invalid entry"
            if l[x1[0]][x1[1]]==' ':
                l[x1[0]][x1[1]]='x'
                break
            else:
                print 'position preoccupied'
        def dup(l):#Creates a duplicate of the matrix given as the arguement and returns it
            d=[]
            for i in range(3):
                x=[]
                for j in range(3):
                    x.append(l[i][j])
                d.append(x)
            return d# d is the duplicate of l
        def check1(t,l):#Returns a list- p, of all the winning positions for t in l, l=GAME MATRIX, t='x' or 'o' 
            p=[]
            for i in a1:
                if l[i[0][0]][i[0][1]]==t and l[i[1][0]][i[1][1]]==t and l[i[2][0]][i[2][1]]==' ':
                    p.append(i[2])
                elif l[i[0][0]][i[0][1]]==t and l[i[1][0]][i[1][1]]==' ' and l[i[2][0]][i[2][1]]==t:
                    p.append(i[1])
                elif l[i[0][0]][i[0][1]]==' ' and l[i[1][0]][i[1][1]]==t and l[i[2][0]][i[2][1]]==t:
                    p.append(i[0])
            return p
        def check2(s,l):#check weather there is a move for s(s=='x'or s=='o') in l(GAME MATRIX) such that s gets two winning positions
            p=[]
            for i in emptyplace(l):
                b=dup(l)
                b[i[0]][i[1]]=s
                if len(check1(s,b))>1:
                    p.append(i)
            return p
        def check3(s1,s2,l):#Find all positions in the game where s1 makes a move such that s1 gets a winning position and s2 is forced to mark that winning position, and next move is game move(check2(d1,l)!=[])
            p=[]
            for i in emptyplace(l):
                b=dup(l)
                b[i[0]][i[1]]=s1
                if check1(s1,b)!=[]:
                    c=dup(b)
                    a=check1(s1,b)[0]
                    c[a[0]][a[1]]=s2
                    if check2(s1,c)!=[] and check1(s2,c)==[]:
                        p.append(i)
                    elif check2(s1,c)!=[]and check1(s2,c)!=[]:
                        a=check1(s2,c)[0]
                        c[a[0]][a[1]]=s1
                        if len(check1(s1,c))>1 and check1(s2,c)==[]:
                            p.append(i)
            return p
        def danger1(l):#find all positions where o makes a move and x gets two winning positions after the next move
            p=[]
            for i in emptyplace(l):
                b=dup(l)
                b[i[0]][i[1]]='o'
                if check1('o',b)!=[]:
                    a=check1('o',b)[0]
                    b[a[0]][a[1]]='x'
                    if len(check1('x',b))>1:
                        p.append(i)
                elif check1('o',b)==[]:#len(emptyplace(b))<=5
                    for z7 in emptyplace(b):
                        q1=dup(b)
                        q1[z7[0]][z7[1]]='x'
                        if len(check1('x',q1))>1: #and check1('o',q1)==[]:
                            p.append(i)
            return p
        def danger2(l):# computer makes a move and check3('x','o',game matrix) is not an empty list 
            d=[]
            for i in emptyplace(l):
                b=dup(l)
                b[i[0]][i[1]]='o'
                if check3('x','o',b)!=[]:
                    d.append(i)
            return d
        #calling of functions (computer makes the move)
        if check1('o',l)!=[]:#check whether computer has a winning position 
            a=random.choice(check1('o',l))
            l[a[0]][a[1]]='o'
        elif check1('x',l)!=[]:#check whether player has a winning position, block it
            a=random.choice(check1('x',l))
            l[a[0]][a[1]]='o'
        elif check2('o',l)!=[]:#check2 for computer
            a=random.choice(check2('o',l))
            l[a[0]][a[1]]='o'
        elif check3('o','x',l)!=[]:#check3 for computer
            a=random.choice(check3('o','x',l))
            l[a[0]][a[1]]='o'
        elif danger1(l)!=[] or danger2(l)!=[]:#prevent the dangerous positions
            z=[]
            for i in emptyplace(l):
                if i not in danger1(l) and i not in danger2(l):
                    z.append(i)
            a=random.choice(z)
            l[a[0]][a[1]]='o'
        elif emptyplace(l)==[]:#end loop if game is draw
            print "game is a draw"
            break
        else:
            a=random.choice(emptyplace(l))#play random move 
            l[a[0]][a[1]]='o'
        for i in l:
            print i
    w=str(raw_input('do u want to play another game?'))
    if w=='no':
        break
    else:
        pass
print "Thank you for playing"
