from time import sleep
import random
from colorama import Fore, Back, Style

o= Style.BRIGHT+Fore.LIGHTRED_EX + 'o'+ Style.RESET_ALL
r= Fore.RED + 'r'+ Style.RESET_ALL
g= Fore.GREEN + 'g'+ Style.RESET_ALL
y= Fore.YELLOW + 'y'+ Style.RESET_ALL
b= Fore.BLUE + 'b'+ Style.RESET_ALL
w= 'w'


space='       '

g,o,w,r,y,b='g','o','w','r','y','b'
print(g,o,w,r,y,b)
G,O,W,R,Y,B=[],[],[],[],[],[]
for i in range(9):
    G.append(g)
    O.append(o)
    W.append(w)
    R.append(r)
    Y.append(y)
    B.append(b)


def WCW():
    # W_clockwise
    temp= W[1]
    W[1],W[3],W[7]=W[3],W[7],W[5]
    W[5]=temp

    temp = W[0]
    W[0], W[6], W[8] = W[6], W[8], W[2]
    W[2]=temp

    temp = G[8]
    G[8],R[2],B[0] = R[2],B[0],O[6]
    O[6] = temp

    temp = G[7]
    G[7],R[5],B[1] = R[5],B[1],O[3]
    O[3] = temp

    temp = G[6]
    G[6],R[8],B[2] = R[8],B[2],O[0]
    O[0] = temp
def WCCW():
    # W_counterclockwise


    temp = W[5]
    W[3], W[7], W[5]= W[1], W[3], W[7]
    W[1] = temp

    temp = W[2]
    W[6], W[8], W[2] = W[0], W[6], W[8]
    W[0]=temp

    temp = O[6]
    R[2],B[0],O[6]= G[8],R[2],B[0]
    G[8] = temp

    temp = O[3]
    R[5],B[1],O[3] = G[7],R[5],B[1]
    G[7] = temp

    temp = O[0]
    R[8],B[2],O[0] = G[6],R[8],B[2]
    G[6] = temp
def YCW():
    # Y_clockwise
    temp= Y[1]
    Y[1],Y[3],Y[7]=Y[3],Y[7],Y[5]
    Y[5]=temp

    temp = Y[0]
    Y[0], Y[6], Y[8] = Y[6], Y[8], Y[2]
    Y[2]=temp

    temp = G[2]
    G[2],O[8],B[6] = O[8],B[6],R[0]
    R[0] = temp

    temp = G[1]
    G[1], O[5], B[7] = O[5], B[7], R[3]
    R[3] = temp

    temp = G[0]
    G[0], O[2], B[8] = O[2], B[8], R[6]
    R[6] = temp
def YCCW():
    # Y_counterclockwise

    temp = Y[5]
    Y[3], Y[7], Y[5] = Y[1], Y[3], Y[7]
    Y[1] = temp

    temp = Y[2]
    Y[6], Y[8], Y[2]= Y[0], Y[6], Y[8]
    Y[0] = temp

    temp = R[0]
    O[8], B[6], R[0]= G[2], O[8], B[6]
    G[2] = temp

    temp = R[3]
    O[5], B[7], R[3]= G[1], O[5], B[7]
    G[1] = temp

    temp = R[6]
    O[2], B[8], R[6]=G[0], O[2], B[8]
    G[0] = temp
def OCW():
    # W_clockwise
    temp = O[1]
    O[1], O[3], O[7] = O[3], O[7], O[5]
    O[5] = temp

    temp = O[0]
    O[0], O[6], O[8] = O[6], O[8], O[2]
    O[2] = temp

    temp = W[2]
    Y[6], B[2], W[2] =G[2], Y[6], B[2]
    G[2] = temp

    temp = W[8]
    Y[0], B[8], W[8]= G[8], Y[0], B[8]
    G[8] = temp

    temp = W[5]
    Y[3], B[5], W[5]= G[5], Y[3], B[5]
    G[5] = temp
def OCCW():
    # W_clockwise
    temp= O[5]
    O[3],O[7],O[5]=O[1],O[3],O[7]
    O[1]=temp

    temp = O[2]
    O[6], O[8], O[2]= O[0], O[6], O[8]
    O[0]=temp

    temp = G[2]
    G[2], Y[6], B[2] = Y[6], B[2], W[2]
    W[2] = temp

    temp = G[8]
    G[8],Y[0],B[8] = Y[0],B[8],W[8]
    W[8] = temp

    temp = G[5]
    G[5], Y[3], B[5] = Y[3], B[5], W[5]
    W[5] = temp
def RCW():
    # R_clockwise
    temp = R[1]
    R[1], R[3], R[7] = R[3], R[7], R[5]
    R[5] = temp

    temp = R[0]
    R[0], R[6], R[8] =R[6], R[8], R[2]
    R[2] = temp

    temp = G[0]
    G[0], Y[8], B[0] =Y[8], B[0], W[0]
    W[0] = temp

    temp = G[3]
    G[3], Y[5], B[3] = Y[5], B[3], W[3]
    W[3] = temp

    temp = G[6]
    G[6], Y[2], B[6] = Y[2], B[6], W[6]
    W[6] = temp
def RCCW():
    # R_counterclockwise
    temp = R[5]
    R[3], R[7], R[5] = R[1], R[3], R[7]
    R[1] = temp

    temp = R[2]
    R[6], R[8], R[2] = R[0], R[6], R[8]
    R[0] = temp

    temp = W[0]
    Y[8], B[0], W[0] = G[0], Y[8], B[0]
    G[0] = temp

    temp =  W[3]
    Y[5], B[3], W[3] = G[3], Y[5], B[3]
    G[3] = temp

    temp =  W[6]
    Y[2], B[6], W[6] = G[6], Y[2], B[6]
    G[6] = temp
def BCW():
    # B_clockwise
    temp = B[1]
    B[1], B[3], B[7] = B[3], B[7], B[5]
    B[5] = temp

    temp = B[0]
    B[0], B[6], B[8] =B[6], B[8], B[2]
    B[2] = temp

    temp = Y[6]
    W[6], O[6], Y[6] =R[6], W[6], O[6]
    R[6] = temp

    temp = Y[7]
    W[7], O[7], Y[7] = R[7], W[7], O[7]
    R[7] = temp

    temp = Y[8]
    W[8], O[8], Y[8] = R[8], W[8], O[8]
    R[8] = temp
def BCCW():
    # B_counterclockwise
    temp = B[5]
    B[3], B[7], B[5] = B[1], B[3], B[7]
    B[1] = temp

    temp = B[2]
    B[6], B[8], B[2]= B[0], B[6], B[8]
    B[0] = temp


    temp = R[6]
    R[6], W[6], O[6] = W[6], O[6], Y[6]
    Y[6] = temp

    temp = R[7]
    R[7], W[7], O[7] = W[7], O[7], Y[7]
    Y[7] = temp

    temp = R[8]
    R[8], W[8], O[8] = W[8], O[8], Y[8]
    Y[8] = temp
def GCW():
    # G_clockwise
    temp = G[1]
    G[1], G[3], G[7] = G[3], G[7], G[5]
    G[5] = temp

    temp = G[0]
    G[0], G[6], G[8] = G[6], G[8], G[2]
    G[2] = temp

    temp = R[0]
    R[0], W[0], O[0] = W[0], O[0], Y[0]
    Y[0] = temp

    temp = R[1]
    R[1], W[1], O[1] = W[1], O[1], Y[1]
    Y[1] = temp

    temp = R[2]
    R[2], W[2], O[2] = W[2], O[2], Y[2]
    Y[2] = temp
def GCCW():
    # G_counterclockwise
    temp = G[5]
    G[3], G[7], G[5] = G[1], G[3], G[7]
    G[1] = temp

    temp = G[2]
    G[6], G[8], G[2] = G[0], G[6], G[8]
    G[0] = temp

    temp = Y[0]
    W[0], O[0], Y[0] = R[0], W[0], O[0]
    R[0] = temp

    temp = Y[1]
    W[1], O[1], Y[1] = R[1], W[1], O[1]
    R[1] = temp

    temp = Y[2]
    W[2], O[2], Y[2] = R[2], W[2], O[2]
    R[2] = temp
def GreenDaisy(green_postion):
    if green_postion == 0:
        GCW();OCW();GCCW()
        #print('GCW();OCW();GCCW()')
    if green_postion == 1:
        RCCW()
        #print('RCCW()')
    if green_postion == 2:
        OCW()
        #print('OCW()')
    if green_postion == 3:
        GCW();RCCW();GCCW()
        #print('GCW();RCCW();GCCW()')
def OrangeDaisy(orange_postion):
    if orange_postion == 2:
        OCW();BCW();OCCW()
        #print('OCW();BCW();OCCW()')
    if orange_postion == 0:
        GCCW()
        #print('GCCW()')
    if orange_postion == 3:
        BCW()
        #print('BCW()')
    if orange_postion == 1:
        OCW();GCCW();OCCW()
        #print('OCW();GCCW();OCCW()')
def BlueDaisy(blue_postion):
    if blue_postion == 3:
        BCW();RCW();BCCW()
        #print('BCW();RCW();BCCW()')
    if blue_postion == 2:
        OCCW()
        #print('OCCW()')
    if blue_postion == 1:
        RCW()
        #print('RCW()')
    if blue_postion == 0:
        BCW();OCCW();BCCW()
        #print('BCW();OCCW();BCCW()')
def RedDaisy(red_postion):
    if red_postion == 1:
        RCW();GCW();RCCW()
        #print('BCW();RCW();BCCW()')
    if red_postion == 3:
        BCCW()
        #print('OCCW()')
    if red_postion == 0:
        GCW()
        #print('RCW()')
    if red_postion == 2:
        RCW();BCCW();RCCW()
        #print('BCW();OCCW();BCCW()')
def Oll(cross):
    if cross ==0:
        BCW();RCW();YCW();RCCW();YCCW();RCW();YCW();RCCW();YCCW();BCCW();YCW();BCW();RCW();YCW();RCCW();YCCW();BCCW()
def Cube():
    print(space)
    print(space, sides, G[0], G[1], G[2], sides)
    print(space, sides, G[3], G[4], G[5], sides)
    print(space, sides, G[6], G[7], G[8], sides)
    print(sides, R[0], R[1], R[2], sides, W[0], W[1], W[2], sides, O[0], O[1], O[2], sides, Y[0], Y[1], Y[2], sides)
    print(sides, R[3], R[4], R[5], sides, W[3], W[4], W[5], sides, O[3], O[4], O[5], sides, Y[3], Y[4], Y[5], sides)
    print(sides, R[6], R[7], R[8], sides, W[6], W[7], W[8], sides, O[6], O[7], O[8], sides, Y[6], Y[7], Y[8], sides)
    print(space, sides, B[0], B[1], B[2], sides)
    print(space, sides, B[3], B[4], B[5], sides)
    print(space, sides, B[6], B[7], B[8], sides)
def sexymove():
    OCW()

    WCW()

    OCCW()

    WCW()

    OCW()
    WCW()
    WCW()
    OCCW()
def centers():
    GCCW()
    BCW()
    WCW()
    YCCW()
def scramble(moves):
    scramble=[]
    for i in range(moves):
        x=random.randint(1, 12)
        if len(scramble) > 0:
            #print(x,scramble[i-1])
            if x % 2 != 0 and scramble[i-1] == x+1:
                #print(x,scramble[i-1])
                x+=1
            elif x % 2 == 0 and scramble[i-1] == x-1:
                #print(x,scramble[i-1])
                x-=1
        if len(scramble) > 1:
            if x == scramble[i-1] and scramble[i-1] == scramble[i-2]:
                x+=1

        if x ==0:
            x=12
        if x==13:
            x=1

        scramble.append(x)
    for i in range(len(scramble)):

        if scramble[i]==1:
            WCW()
            scramble[i]="F"
        elif scramble[i]==2:
            WCCW()
            scramble[i]="F'"
        elif scramble[i]==3:
            YCW()
            scramble[i]="B"
        elif scramble[i]==4:
            YCCW()
            scramble[i]="B'"
        elif scramble[i]==5:
            GCW()
            scramble[i]="U"
        elif scramble[i]==6:
            GCCW()
            scramble[i]="U'"

        elif scramble[i]==7:
            BCW()
            scramble[i]="D"
        elif scramble[i]==8:
            BCCW()
            scramble[i]="D'"

        elif scramble[i]==9:
            OCW()
            scramble[i]="R"
        elif scramble[i]==10:
            OCCW()
            scramble[i]="R'"

        elif scramble[i]==11:
            RCW()
            scramble[i]="L"
        elif scramble[i]==12:
            RCCW()
            scramble[i]="L'"
    print(*scramble)
    return scramble
def controls():
    user_move = input('move? ').upper()

    if user_move in move_set:

        move_set[user_move]()
    else:
        print('doesnt exist')
def edges(G,O,W,R,Y,B):
    edges=[G[1]+Y[1], G[3]+R[1], G[5]+O[1], G[7]+W[1],
           R[3]+Y[5], Y[3]+O[5], O[3]+W[5], W[3]+R[5],
           B[1]+W[7], B[3]+R[7], B[5]+O[7], B[7]+Y[7],]
    for i in range(len(edges)):
        if 'w' in edges[i]:
            edges[i]=Fore.GREEN + edges[i]+ Style.RESET_ALL
    print(*edges)

def daisy(G,O,W,R,Y,B):
    Daisy = False
    trials=1
    while Daisy == False:

        white_edge, green_edge, orange_edge, red_edge, blue_edge=(W[1],W[3],W[5],W[7]), (G[1],G[3],G[5],G[7]), (O[1],O[3],O[5],O[7]), (R[1],R[3],R[5],R[7]), (B[1],B[3],B[5],B[7])

        whiteedgemove = {0: GCW, 1: RCW, 2: OCW, 3: BCW}
        greenedgemove = {0: GreenDaisy, 1: GreenDaisy, 2: GreenDaisy, 3: GreenDaisy}
        orangeedgemove = {0: OrangeDaisy, 1: OrangeDaisy, 2: OrangeDaisy, 3: OrangeDaisy}
        blueedgemove = {0: BlueDaisy, 1: BlueDaisy, 2: BlueDaisy, 3: BlueDaisy}
        rededgemove = {0: RedDaisy, 1: RedDaisy, 2: RedDaisy, 3: RedDaisy}
        if 'w' in white_edge:
            for i in range(len(white_edge)):
                if 'w' in white_edge[i]:
                    whiteedgemove[i]();whiteedgemove[i]()
                    #print('2x'+str(whiteedgemove[i]))


        if 'w' in green_edge:
            for i in range(len(green_edge)):
                if 'w' in green_edge[i]:
                    greenedgemove[i](i)


        if 'w' in orange_edge:
            for i in range(len(orange_edge)):
                if 'w' in orange_edge[i]:
                    orangeedgemove[i](i)

        for i in range(random.randrange(1, 3)):
            YCCW()
        if 'w' in blue_edge:
            for i in range(len(blue_edge)):
                if 'w' in blue_edge[i]:
                    blueedgemove[i](i)

        if 'w' in red_edge:
            for i in range(len(red_edge)):
                if 'w' in red_edge[i]:
                    rededgemove[i](i)


        if Y[1] == 'w' and Y[3] == 'w' and Y[5] == 'w' and Y[7] == 'w':
            print(trials,'done')
            #Cube()
            Daisy = True
        else:
            trials+=1
            #print('one more!')
        sleep(0)
def White_Cross(G,O,W,R,Y,B):

    green, orange, blue, red = False, False, False, False
    while True:
        #print('test')
        if G[1]=='g' and Y[1] == 'w':
            GCW();GCW()
            break

        else:

            YCW()

    while True:
        if O[5]=='o' and Y[3] == 'w':
            OCW();OCW()
            break


        else:
            YCW()
    while True:
        if B[7]=='b' and Y[7] == 'w':
            BCW();BCW()
            break
        else:
            YCW()
    while True:
        if R[3]=='r' and Y[5] == 'w':
            RCW();RCW()
            break
        else:
            YCW()
    #Cube()
def White_Face(G,O,W,R,Y,B):

    while True:
        GOY_corner, GOW_corner = (G[2], O[2], Y[0]), (G[8], O[0], W[2])
        if 'w' in GOW_corner or 'w' in GOY_corner:
            if W[2] == 'w':
                break
            else:
                while W[2]!='w':
                    OCW();YCW();OCCW();YCCW()
        else:
            YCW()
    while True:
        OBY_corner, OBW_corner = (O[8], B[8], Y[6]), (O[6], B[2], W[8])
        if 'w' in OBY_corner or 'w' in OBW_corner:
            if W[8] == 'w':
                break
            else:
                while W[8]!='w':
                    BCW();YCW();BCCW();YCCW()
        else:
            YCW()
    while True:
        BRY_corner, BRW_corner = (B[6], R[6], Y[8]), (B[0], R[8], W[6])
        if 'w' in BRY_corner or 'w' in BRW_corner:
            if W[6] == 'w':
                break
            else:
                while W[6]!='w':
                    RCW();YCW();RCCW();YCCW()
        else:
            YCW()
    while True:
        RGY_corner, RGW_corner = (R[0], G[0], Y[2]), (R[2], G[6], W[0])
        if 'w' in RGY_corner or 'w' in RGW_corner:
            if W[0] == 'w':
                break
            else:
                while W[0]!='w':
                    GCW();YCW();GCCW();YCCW()
        else:
            YCW()
    while True:
        if G[8]=="g":
            break
        elif O[6]=="g":
            BCW();YCW();BCCW();OCCW();GCW();OCW();GCCW();YCCW();OCW();BCCW();OCCW();BCW()
            break
        elif B[0] == "g":
            OCW();RCW();YCW();YCW();OCCW();RCCW()
            break
        elif R[2] == "g":
            OCW();YCW();OCCW();GCCW();RCW();GCW();RCCW();YCCW();GCW();OCCW();GCCW();OCW()
            break
    while True:
        if O[6] == "o":
            break
        elif B[0]=="o":
            RCW();YCW();RCCW();BCCW();OCW();BCW();OCCW();YCCW();BCW();RCCW();BCCW();RCW()
            break
        elif R[2] == "o":
            BCW();GCW();YCW();YCW();BCCW();GCCW()
            break
    while True:
        if B[0] == "b":
            break
        else:
            GCW();YCW();GCCW();RCCW();BCW();RCW();BCCW();YCCW();RCW();GCCW();RCCW();GCW()
def Second_Layer(G,O,W,R,Y,B):

    while True:
        Gtop = (G[1], Y[1])

        if G[5] == 'g' and O[1] == 'o':
            break
        if G[5] == 'y' or O[1] == 'y':
            break
        if 'y' in Gtop:
            YCW();OCW();YCW();OCCW();YCCW();GCCW();YCCW();GCW()
        YCW()

    while True:
        Otop = (O[5], Y[3])

        if O[7]== 'o' and B[5] == 'b':
            break
        if O[7]== 'y' or B[5] == 'y':
            break
        if 'y' in Otop:
            YCW();BCW();YCW();BCCW();YCCW();OCCW();YCCW();OCW()
        YCW()

    while True:
        Btop = (B[7], Y[7])

        if B[3]== 'b' and R[7] == 'r':
            break
        if B[3]== 'y' or R[7] == 'y':
            break
        if 'y' in Btop:
            YCW();RCW();YCW();RCCW();YCCW();BCCW();YCCW();BCW()
        YCW()

    while True:
        Rtop = (R[3], Y[5])

        if R[1]== 'r' and G[3] == 'g':
            break
        if R[1]== 'y' or G[3] == 'y':
            break
        if 'y' in Rtop:
            YCW();GCW();YCW();GCCW();YCCW();RCCW();YCCW();RCW()
        YCW()
    #Cube()

    while True:
        if G[5] == 'g' and O[1] == 'o':
            break
        if G[1] =='g' and Y[1] == 'o':
            YCW();OCW();YCW();OCCW();YCCW();GCCW();YCCW();GCW()
            break
        if O[5] =="o" and Y[3]=='g':
            YCCW();GCCW();YCW();GCW();OCCW();GCW();OCW();GCCW()
            break
        YCW()

    while True:
        if O[7] == 'o' and B[5] == 'b':
            break
        if O[5] =="o" and Y[3]=='b':
            YCW();BCW();YCW();BCCW();YCCW();OCCW();YCCW();OCW()
            break
        if B[7] =="b" and Y[7]=='o':
            YCCW();OCCW();YCW();OCW();BCCW();OCW();BCW();OCCW()
            break
        YCW()
    while True:
        if B[3] == 'b' and R[7] == 'r':
            break
        if B[7] =="b" and Y[7]=='r':
            YCW();RCW();YCW();RCCW();YCCW();BCCW();YCCW();BCW()
            break
        if R[3] =="r" and Y[5]=='b':
            YCCW();BCCW();YCW();BCW();RCCW();BCW();RCW();BCCW()
            break
        YCW()
    while True:
        if R[1] == 'r' and G[3] == 'g':
            break
        if R[3] == "r" and Y[5]=='g':
            YCW();GCW();YCW();GCCW();YCCW();RCCW();YCCW();RCW()
            break
        if G[1] =="g" and Y[1]=='r':
            YCCW();RCCW();YCW();RCW();GCCW();RCW();GCW();RCCW()
            break
        YCW()
    Cube()
    pass
def Yellow_Face(G,O,W,R,Y,B):
    while True:
        print('test')
        if Y[1:8:2] == ['y', 'y', 'y', 'y']:
            Cube()
            break
        rev=1
        Y_cross = ''
        Ycrosslist = {'0000':Oll}

        for i in range(4):
            if Y[rev]=='y': Y_cross+='y'
            else: Y_cross+='0'
            rev+=2
        if Y_cross in Ycrosslist:
            print(Ycrosslist[Y_cross])
            Ycrosslist[Y_cross](0)
            Cube()
            break



        sleep(2)


sides='|'
move_set = {"F": WCW, "F'": WCCW, "B": YCW, "B'": YCCW, "U": GCW, "U'": GCCW, "D": BCW, "D'": BCCW, "R": OCW, "R'": OCCW, "L": RCW, "L'": RCCW}
#options = {"F": 1, "F'": 2, "B": 3, "B'": 4, "U": 5, "U'": 6, "D": 7, "D'": 8, "R": 9, "R'": 10, "L": 11, "L'": 12}
#move_set = {1: WCW, 2: WCCW, 3: YCW, 4: YCCW, 5: GCW, 6: GCCW, 7: BCW, 8: BCCW, 9: OCW, 10: OCCW, 11: RCW, 12: RCCW}
mixed=False
#mixed=True

#r b r' b r b b r'
#r' u r' d d r u' r' d d r r
#u u b l r' u u l' r b u u

while True:

    if mixed is False:
        scramble(20)
        mixed = True
        Cube()
    #edges(G, O, W, R, Y, B)
    daisy(G, O, W, R, Y, B)
    White_Cross(G, O, W, R, Y, B)
    White_Face(G, O, W, R, Y, B)
    Second_Layer(G, O, W, R, Y, B)
    Yellow_Face(G, O, W, R, Y, B)
    input()

