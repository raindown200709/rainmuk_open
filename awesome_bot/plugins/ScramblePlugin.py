from random import randint,choice
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event


def three():
    TURN_333 = ("U","R","F","D","L","B","U2","R2","F2","D2","L2","B2","U'","R'","F'","D'","L'","B'")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 20
    count = 0
    while count < LENGTH:
        turn = choice(TURN_333)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F") == 0:
            continue
        elif turn.find("D") == 0 and pre_turn.find("D") == 0:
            continue
        elif turn.find("L") == 0 and pre_turn.find("L") == 0:
            continue
        elif turn.find("B") == 0 and pre_turn.find("B") == 0:
            continue
        else:
            scb += turn +' '
            pre_turn = turn
            count += 1
    return scb      


def two():
    TURN_222 = ("U", "R", "F", "U'", "R'", "F", "U2", "R2", "F2")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 11
    count =0 
    while count < LENGTH:
        turn = choice(TURN_222)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F")  == 0:
            continue
        else:
            scb += turn +' '
            pre_turn =turn
            count += 1
    return scb
  

def four():
    TURN_444 = ("U" , "U2" , "Uw" , "Uw2" ,"U'" ,"Uw'" , "R" , "R2" , "Rw" , "Rw2" ,"R'" ,"Rw'" , "F" , "F2" , "Fw" , "Fw2" ,"F'" ,"Fw'" , "B" , "B2" , "Bw" , "Bw2" ,"B'" ,"Bw'" , "L" , "L2" , "Lw" , "Lw2" ,"L'" ,"Lw'" , "D" , "D2" , "Dw" , "Dw2" ,"D'" ,"Dw'")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 50
    count =0 
    while count < LENGTH:
        turn = choice(TURN_444)
        #允许[true]w[rev]与[true]连续出现
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("F") == 0 and pre_turn.find("F")  == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("B") == 0 and pre_turn.find("B")  == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("L") == 0 and pre_turn.find("L")  == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("D") == 0 and pre_turn.find("D")  == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        else :
            scb += turn +' '
            pre_turn =turn
            count += 1
    return scb


def five():
    TURN_555 = ("U" , "U2" , "Uw" , "Uw2" ,"U'" ,"Uw'" , "R" , "R2" , "Rw" , "Rw2" ,"R'" ,"Rw'" , "F" , "F2" , "Fw" , "Fw2" ,"F'" ,"Fw'" , "B" , "B2" , "Bw" , "Bw2" ,"B'" ,"Bw'" , "L" , "L2" , "Lw" , "Lw2" ,"L'" ,"Lw'" , "D" , "D2" , "Dw" , "Dw2" ,"D'" ,"Dw'")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 60
    count =0 
    while count < LENGTH:
        turn = choice(TURN_555)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("F") == 0 and pre_turn.find("F")  == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("B") == 0 and pre_turn.find("B")  == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("L") == 0 and pre_turn.find("L")  == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("D") == 0 and pre_turn.find("D")  == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        else :
            scb += turn +' '
            pre_turn =turn
            count += 1
    return scb


def six():
    TURN_666 = ("U","U2","3Uw","Uw","3Uw2","Uw2","U'","3Uw'","Uw'","R","R'","R2","3Rw","Rw","Rw'","3Rw'","3Rw2","Rw2","F","F'","F2","3Fw","3Fw'","3Fw2","Fw","Fw'","Fw2","L","L2","L'","3Lw","3Lw2","3Lw'","L" "L2" , "Lw" , "Lw2" ,"L'" ,"Lw'" , "D" , "D2" , "Dw" , "Dw2" ,"D'" ,"Dw'")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 80
    count =0
    while count < LENGTH:
        turn = choice(TURN_666)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F") == 0:
            continue
        elif turn.find("D") == 0 and pre_turn.find("D") == 0:
            continue
        elif turn.find("L") == 0 and pre_turn.find("L") == 0:
            continue
        elif turn.find("B") == 0 and pre_turn.find("B") == 0:
            continue
        else:
            scb += turn +' '
            pre_turn = turn
            count += 1
    return scb        


def seven():
    TURN_777 = ("U","U2","3Uw","Uw","3Uw2","Uw2","U'","3Uw'","Uw'","R","R'","R2","3Rw","Rw","Rw'","3Rw'","3Rw2","Rw2","F","F'","F2","3Fw","3Fw'","3Fw2","Fw","Fw'","Fw2","L","L2","L'","3Lw","3Lw2","3Lw'","Lw","Lw'","Lw2","D","D2","D'","Dw","Dw2","Dw'","3Dw","3Dw'","3Dw2","B","B2","B'","3Bw","3Bw2","3Bw'","Bw","Bw'","Bw2")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 100
    count =0
    while count < LENGTH:
        turn = choice(TURN_777)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F") == 0:
            continue
        elif turn.find("D") == 0 and pre_turn.find("D") == 0:
            continue
        elif turn.find("L") == 0 and pre_turn.find("L") == 0:
            continue
        elif turn.find("B") == 0 and pre_turn.find("B") == 0:
            continue
        else:
            scb += turn +' '
            pre_turn = turn
            count += 1
    return scb


def eight():
    TURN_888 = ("U","U2","3Uw","4Uw","Uw","3Uw2","4Uw2","Uw2","U'","3Uw'","4Uw'","Uw'","R","R'","R2","3Rw","4Rw","Rw","Rw'","3Rw'","4Rw'","3Rw2","4Rw2","Rw2","F","F'","F2","3Fw","3Fw'","3Fw2","4Fw","4Fw'","4Fw2","Fw","Fw'","Fw2","L","L2","L'","4Lw","4Lw'","4Lw2","3Lw","3Lw2","3Lw'","Lw","Lw'","Lw2","D","D2","D'","4Dw","4Dw","4Dw2","Dw","Dw2","Dw'","3Dw","3Dw'","3Dw2","B","B2","B'","4Bw","4Bw","4Bw2","3Bw","3Bw2","3Bw'","Bw","Bw'","Bw2")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 120
    count =0
    while count < LENGTH:
        turn = choice(TURN_888)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F") == 0:
            continue
        elif turn.find("D") == 0 and pre_turn.find("D") == 0:
            continue
        elif turn.find("L") == 0 and pre_turn.find("L") == 0:
            continue
        elif turn.find("B") == 0 and pre_turn.find("B") == 0:
            continue
        else:
            scb += turn +' '
            pre_turn = turn
            count += 1
    return scb


def nine():
    TURN_999 = ("U","U2","3Uw","4Uw","Uw","3Uw2","4Uw2","Uw2","U'","3Uw'","4Uw'","Uw'","R","R'","R2","3Rw","4Rw","Rw","Rw'","3Rw'","4Rw'","3Rw2","4Rw2","Rw2","F","F'","F2","3Fw","3Fw'","3Fw2","4Fw","4Fw'","4Fw2","Fw","Fw'","Fw2","L","L2","L'","4Lw","4Lw'","4Lw2","3Lw","3Lw2","3Lw'","Lw","Lw'","Lw2","D","D2","D'","4Dw","4Dw","4Dw2","Dw","Dw2","Dw'","3Dw","3Dw'","3Dw2","B","B2","B'","4Bw","4Bw","4Bw2","3Bw","3Bw2","3Bw'","Bw","Bw'","Bw2")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 140
    count =0
    while count < LENGTH:
        turn = choice(TURN_999)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F") == 0:
            continue
        elif turn.find("D") == 0 and pre_turn.find("D") == 0:
            continue
        elif turn.find("L") == 0 and pre_turn.find("L") == 0:
            continue
        elif turn.find("B") == 0 and pre_turn.find("B") == 0:
            continue
        else:
            scb += turn +' '
            pre_turn = turn
            count += 1
    return scb


def ten():
    TURN_101010 = ("U","U2","3Uw","4Uw","5Uw","5Uw'","5UW2","Uw","3Uw2","4Uw2","Uw2","U'","3Uw'","4Uw'","Uw'","R","R'","R2","5Rw","5Rw'","5Rw2","3Rw","4Rw","Rw","Rw'","3Rw'","4Rw'","3Rw2","4Rw2","Rw2","F","F'","F2","5Fw","5Fw'","5Fw2","3Fw","3Fw'","3Fw2","4Fw","4Fw'","4Fw2","Fw","Fw'","Fw2","L","L2","L'","5Lw","5Lw'","5Lw2","4Lw","4Lw'","4Lw2","3Lw","3Lw2","3Lw'","Lw","Lw'","Lw2","D","D2","D'","5Dw","5Dw'","5Dw2","4Dw","4Dw","4Dw2","Dw","Dw2","Dw'","3Dw","3Dw'","3Dw2","B","B2","B'","5Bw","5Bw'","5Bw2","4Bw","4Bw","4Bw2","3Bw","3Bw2","3Bw'","Bw","Bw'","Bw2")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 160
    count = 0
    while count < LENGTH:
        turn = choice(TURN_101010)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F") == 0:
            continue
        elif turn.find("D") == 0 and pre_turn.find("D") == 0:
            continue
        elif turn.find("L") == 0 and pre_turn.find("L") == 0:
            continue
        elif turn.find("B") == 0 and pre_turn.find("B") == 0:
            continue
        else:
            scb += turn +' '
            pre_turn = turn
            count += 1
    return scb


def eleven():
    TURN_111111 = ("U","U2","3Uw","4Uw","5Uw","5Uw'","5UW2","Uw","3Uw2","4Uw2","Uw2","U'","3Uw'","4Uw'","Uw'","R","R'","R2","5Rw","5Rw'","5Rw2","3Rw","4Rw","Rw","Rw'","3Rw'","4Rw'","3Rw2","4Rw2","Rw2","F","F'","F2","5Fw","5Fw'","5Fw2","3Fw","3Fw'","3Fw2","4Fw","4Fw'","4Fw2","Fw","Fw'","Fw2","L","L2","L'","5Lw","5Lw'","5Lw2","4Lw","4Lw'","4Lw2","3Lw","3Lw2","3Lw'","Lw","Lw'","Lw2","D","D2","D'","5Dw","5Dw'","5Dw2","4Dw","4Dw","4Dw2","Dw","Dw2","Dw'","3Dw","3Dw'","3Dw2","B","B2","B'","5Bw","5Bw'","5Bw2","4Bw","4Bw","4Bw2","3Bw","3Bw2","3Bw'","Bw","Bw'","Bw2")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 180
    count = 0
    while count < LENGTH:
        turn = choice(TURN_111111)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F") == 0:
            continue
        elif turn.find("D") == 0 and pre_turn.find("D") == 0:
            continue
        elif turn.find("L") == 0 and pre_turn.find("L") == 0:
            continue
        elif turn.find("B") == 0 and pre_turn.find("B") == 0:
            continue
        else:
            scb += turn +' '
            pre_turn = turn
            count += 1
    return scb


def twelve():
    TURN_121212 = ("U","U2","3Uw","4Uw","5Uw","5Uw'","5UW2","6Uw","6Uw'","6Uw'","Uw","3Uw2","4Uw2","Uw2","U'","3Uw'","4Uw'","Uw'","R","R'","R2","5Rw","5Rw'","5Rw2","6Rw","6Rw'","6Rw2","3Rw","4Rw","Rw","Rw'","3Rw'","4Rw'","3Rw2","4Rw2","Rw2","F","F'","F2","5Fw","5Fw'","5Fw2","6Fw","6Fw'","6Fw2","3Fw","3Fw'","3Fw2","4Fw","4Fw'","4Fw2","Fw","Fw'","Fw2","L","L2","L'","5Lw","5Lw'","5Lw2","6Lw","6Lw'","6Lw2","4Lw","4Lw'","4Lw2","3Lw","3Lw2","3Lw'","Lw","Lw'","Lw2","D","D2","D'","5Dw","5Dw'","5Dw2","6Dw","6Dw'","6Dw2","4Dw","4Dw","4Dw2","Dw","Dw2","Dw'","3Dw","3Dw'","3Dw2","B","B2","B'","6Bw","6Bw'","6Bw2","5Bw","5Bw'","5Bw2","4Bw","4Bw","4Bw2","3Bw","3Bw2","3Bw'","Bw","Bw'","Bw2")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 200
    count = 0
    while count < LENGTH:
        turn = choice(TURN_121212)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F") == 0:
            continue
        elif turn.find("D") == 0 and pre_turn.find("D") == 0:
            continue
        elif turn.find("L") == 0 and pre_turn.find("L") == 0:
            continue
        elif turn.find("B") == 0 and pre_turn.find("B") == 0:
            continue
        else:
            scb += turn +' '
            pre_turn = turn
            count += 1
    return scb


def thirteen():
    TURN_131313 = ("U","U2","3Uw","4Uw","5Uw","5Uw'","5UW2","6Uw","6Uw'","6Uw'","Uw","3Uw2","4Uw2","Uw2","U'","3Uw'","4Uw'","Uw'","R","R'","R2","5Rw","5Rw'","5Rw2","6Rw","6Rw'","6Rw2","3Rw","4Rw","Rw","Rw'","3Rw'","4Rw'","3Rw2","4Rw2","Rw2","F","F'","F2","5Fw","5Fw'","5Fw2","6Fw","6Fw'","6Fw2","3Fw","3Fw'","3Fw2","4Fw","4Fw'","4Fw2","Fw","Fw'","Fw2","L","L2","L'","5Lw","5Lw'","5Lw2","6Lw","6Lw'","6Lw2","4Lw","4Lw'","4Lw2","3Lw","3Lw2","3Lw'","Lw","Lw'","Lw2","D","D2","D'","5Dw","5Dw'","5Dw2","6Dw","6Dw'","6Dw2","4Dw","4Dw","4Dw2","Dw","Dw2","Dw'","3Dw","3Dw'","3Dw2","B","B2","B'","6Bw","6Bw'","6Bw2","5Bw","5Bw'","5Bw2","4Bw","4Bw","4Bw2","3Bw","3Bw2","3Bw'","Bw","Bw'","Bw2")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 220
    count = 0
    while count < LENGTH:
        turn = choice(TURN_131313)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F") == 0:
            continue
        elif turn.find("D") == 0 and pre_turn.find("D") == 0:
            continue
        elif turn.find("L") == 0 and pre_turn.find("L") == 0:
            continue
        elif turn.find("B") == 0 and pre_turn.find("B") == 0:
            continue
        else:
            scb += turn +' '
            pre_turn = turn
            count += 1
    return scb


def fourteen():
    TURN_141414 = ("U","U2","3Uw","4Uw","5Uw","5Uw'","5UW2","6Uw","6Uw'","6Uw'","7Uw","7Uw'","7Uw2","Uw","3Uw2","4Uw2","Uw2","U'","3Uw'","4Uw'","Uw'","R","R'","R2","5Rw","5Rw'","5Rw2","6Rw","6Rw'","6Rw2","7Rw","7Rw'","7Rw2","3Rw","4Rw","Rw","Rw'","3Rw'","4Rw'","3Rw2","4Rw2","Rw2","F","F'","F2","5Fw","5Fw'","5Fw2","6Fw","6Fw'","6Fw2","7Fw","7Fw'","7Fw2","3Fw","3Fw'","3Fw2","4Fw","4Fw'","4Fw2","Fw","Fw'","Fw2","L","L2","L'","5Lw","5Lw'","5Lw2","6Lw","6Lw'","6Lw2","7Lw","7Lw'","7Lw2","4Lw","4Lw'","4Lw2","3Lw","3Lw2","3Lw'","Lw","Lw'","Lw2","D","D2","D'","5Dw","5Dw'","5Dw2","6Dw","6Dw'","6Dw2","7Dw","7Dw'","7Dw2","4Dw","4Dw","4Dw2","Dw","Dw2","Dw'","3Dw","3Dw'","3Dw2","B","B2","B'","6Bw","6Bw'","6Bw2","7Bw","7Bw'","7Bw2","5Bw","5Bw'","5Bw2","4Bw","4Bw","4Bw2","3Bw","3Bw2","3Bw'","Bw","Bw'","Bw2")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 240
    count = 0
    while count < LENGTH:
        turn = choice(TURN_141414)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F") == 0:
            continue
        elif turn.find("D") == 0 and pre_turn.find("D") == 0:
            continue
        elif turn.find("L") == 0 and pre_turn.find("L") == 0:
            continue
        elif turn.find("B") == 0 and pre_turn.find("B") == 0:
            continue
        else:
            scb += turn +' '
            pre_turn = turn
            count += 1
    return scb    


def fifteen():
    TURN_151515 = ("U","U2","3Uw","4Uw","5Uw","5Uw'","5UW2","6Uw","6Uw'","6Uw'","7Uw","7Uw'","7Uw2","Uw","3Uw2","4Uw2","Uw2","U'","3Uw'","4Uw'","Uw'","R","R'","R2","5Rw","5Rw'","5Rw2","6Rw","6Rw'","6Rw2","7Rw","7Rw'","7Rw2","3Rw","4Rw","Rw","Rw'","3Rw'","4Rw'","3Rw2","4Rw2","Rw2","F","F'","F2","5Fw","5Fw'","5Fw2","6Fw","6Fw'","6Fw2","7Fw","7Fw'","7Fw2","3Fw","3Fw'","3Fw2","4Fw","4Fw'","4Fw2","Fw","Fw'","Fw2","L","L2","L'","5Lw","5Lw'","5Lw2","6Lw","6Lw'","6Lw2","7Lw","7Lw'","7Lw2","4Lw","4Lw'","4Lw2","3Lw","3Lw2","3Lw'","Lw","Lw'","Lw2","D","D2","D'","5Dw","5Dw'","5Dw2","6Dw","6Dw'","6Dw2","7Dw","7Dw'","7Dw2","4Dw","4Dw","4Dw2","Dw","Dw2","Dw'","3Dw","3Dw'","3Dw2","B","B2","B'","6Bw","6Bw'","6Bw2","7Bw","7Bw'","7Bw2","5Bw","5Bw'","5Bw2","4Bw","4Bw","4Bw2","3Bw","3Bw2","3Bw'","Bw","Bw'","Bw2")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 240
    count = 0
    while count < LENGTH:
        turn = choice(TURN_151515)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F") == 0:
            continue
        elif turn.find("D") == 0 and pre_turn.find("D") == 0:
            continue
        elif turn.find("L") == 0 and pre_turn.find("L") == 0:
            continue
        elif turn.find("B") == 0 and pre_turn.find("B") == 0:
            continue
        else:
            scb += turn +' '
            pre_turn = turn
            count += 1
    return scb    


def leaves():
    TURN_leaves = ("U","R","F","D","L","B","U2","R2","F2","D2","L2","B2","U'","R'","F'","D'","L'","B'")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 6
    count = 0
    while count < LENGTH:
        turn = choice(TURN_leaves)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F") == 0:
            continue
        elif turn.find("D") == 0 and pre_turn.find("D") == 0:
            continue
        elif turn.find("L") == 0 and pre_turn.find("L") == 0:
            continue
        elif turn.find("B") == 0 and pre_turn.find("B") == 0:
            continue
        else:
            scb += turn +' '
            pre_turn = turn
            count += 1
    return scb  


def skewb():
    TURN_skewb = ("U","R","F","D","L","B","U2","R2","F2","D2","L2","B2","U'","R'","F'","D'","L'","B'")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 9
    count = 0
    while count < LENGTH:
        turn = choice(TURN_skewb)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F") == 0:
            continue
        elif turn.find("D") == 0 and pre_turn.find("D") == 0:
            continue
        elif turn.find("L") == 0 and pre_turn.find("L") == 0:
            continue
        elif turn.find("B") == 0 and pre_turn.find("B") == 0:
            continue
        else:
            scb += turn +' '
            pre_turn = turn
            count += 1
    return scb 


def minx():
    e = ['R++ ','R-- ']
    f = ['D++ ','D-- ']
    g = ['D++ U ','D-- U’']
    minx = e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+g[randint(0,1)]+'\n'+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+g[randint(0,1)]+'\n'+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+g[randint(0,1)]+'\n'+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+g[randint(0,1)]+'\n'+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+g[randint(0,1)]+'\n'+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+g[randint(0,1)]+'\n'+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+f[randint(0,1)]+e[randint(0,1)]+g[randint(0,1)]
    return minx


def clock():
    a = ['1','2','3','4','5','6']
    b = ['+','-']
    c = ['0','1','2','3','4','5','6']
    d = ['DR''DL','UR','UL','DR DL','DR UR','DR UL','DL DR','DL UR','DL UL','UR DR','UR DL','UR UL','UL DR','UL DL','UL UR']
    clock = 'UR'+a[randint(0,5)]+b[randint(0,1)]+' DR'+a[randint(0,5)]+b[randint(0,1)]+' DL'+a[randint(0,5)]+b[randint(0,1)]+' UL'+a[randint(0,5)]+b[randint(0,1)]+' U'+a[randint(0,5)]+b[randint(0,1)]+' R'+a[randint(0,5)]+b[randint(0,1)]+' D'+a[randint(0,5)]+b[randint(0,1)]+' L'+a[randint(0,5)]+b[randint(0,1)]+' ALL'+a[randint(0,5)]+b[randint(0,1)]+' y2'+' U'+c[randint(0,6)]+b[randint(0,1)]+' R'+c[randint(0,6)]+b[randint(0,1)]+' D'+c[randint(0,6)]+b[randint(0,1)]+' L'+c[randint(0,6)]+b[randint(0,1)]+' ALL'+a[randint(0,5)]+b[randint(0,1)]+d[randint(0,13)]
    return clock


def sq():
    sq_list = ['(1,-3)/ (5,-1)/ (0,-3)/ (1,-2)/ (3,-3)/ (2,0)`/` (0,-3)/ (6,-3)/ (0,-2)/ (-4,0)/ (0,-2)/ (-2,-4)/',
          '(-5,0)/ (-3,0)/ (2,5)/ (-2,-2)/ (3,0)/ (-3,0)/ (-3,-1)`/` (-3,-3)/ (1,0)/ (2,-2)/ (2,-4)/ (4,0)/',
          '(0,-4)/ (-2,-5)/ (2,5)/ (1,-5)/ (6,-3)/ (-4,-3)`/` (-3,-3)/ (0,-5)/ (-2,-2)/ (5,0) ',
          '(-5,-3)/ (0,3)/ (-1,5)/ (-3,0)/ (4,-2)/ (3,0)/ (0,-1)`/` (-3,0)/ (-1,-3)/ (1,-3)/ (6,-2)/ (4,0)/',
          '(0,2)/ (3,-3)/ (-5,1)/ (0,-3)/ (0,-3)/ (6,0)/ (5,0)`/` (3,0)/ (3,0)/ (-2,-3)/ (-2,0)/ (-4,-5)/ (2,-2)',
          '(1,0)/ (-1,5)/ (6,-3)/ (1,-2)/ (2,-4)/ (-3,-5)`/` (3,0)/ (3,0)/ (4,0)/ (-2,0)/ (6,-3)/ (-1,-4)',
          '(0,2)/ (-5,-5)/ (5,-4)/ (0,-3)/ (4,-2)/ (-3,0)/ (0,-4)`/` (6,0)/ (-3,0)/ (3,0)/ (-5,0)/ (2,-2)/ (2,0)/',
          '(4,0)/ (0,3)/ (3,0)/ (-4,-1)/ (-3,0)/ (1,-2)/ (-4,0)`/` (3,0)/ (-5,0)/ (-4,0)/ (4,-3)/ (2,0)/ (-4,0)/ (6,0)/',
          '(0,-4)/ (1,4)/ (5,2)/ (6,0)/ (-5,-5)/ (-4,0)`/` (-3,0)/ (0,-1)/ (0,-5)/ (-4,0)/ (0,-4)/ (-5,-4)',
          '(4,-3)/ (2,-1)/ (0,-3)/ (0,-3)/ (3,0)/ (0,-3)/ (3,-5)`/` (0,-3)/ (4,-3)/ (0,-3)/ (5,0)/ (2,-1)/ (-2,0)/',
          '(1,-3)/ (6,0)/ (-4,5)/ (0,-3)/ (1,-5)/ (0,-4)`/` (-3,0)/ (-1,0)/ (-4,0)/ (1,-2)/ (-2,-4)/ (-3,-5)',
          '(0,-4)/ (-3,0)/ (-3,0)/ (3,0)/ (4,-5)/ (-4,-1)/ (-2,-3)`/` (-3,-3)/ (0,-3)/ (1,-1)/ (0,-2)/ (6,-4) ',
          '(0,-1)/ (1,4)/ (0,3)/ (3,0)/ (5,-1)/ (3,0)/ (-5,-3)`/` (0,-3)/ (-1,0)/ (0,-4)/ (-2,0)/ (-3,-4)/ (4,0)/',
          '(0,2)/ (-2,1)/ (5,-4)/ (0,-3)/ (-3,0)/ (-3,0)/ (4,0)`/` (3,0)/ (3,0)/ (5,0)/ (2,-5)/ (0,-3)/ (-4,0)/ (0,-4)/',
          '(-3,2)/ (-5,1)/ (-3,-3)/ (-4,-1)/ (3,0)/ (-2,0)`/` (3,0)/ (3,-3)/ (-5,0)/ (0,-2)/ (0,-1)/ (-3,-4)',
          '(4,3)/ (-1,2)/ (4,-2)/ (-3,0)/ (-1,-4)/ (-3,-5)`/` (-3,-3)/ (2,0)/ (1,0)/ (0,-1)/ (-1,-4)/ (0,-4)/',
          '(-2,-3)/ (0,-3)/ (-1,2)/ (0,-3)/ (-3,0)/ (-3,0)/ (4,0)`/` (0,-3)/ (-1,0)/ (-2,0)/ (2,-3)/ (3,0)/ (0,-4)',
          '(3,-4)/ (1,4)/ (-3,0)/ (-3,-3)/ (-4,-1)/ (1,-3)`/` (-3,-3)/ (-3,0)/ (2,-2)/ (-2,0)/ (1,0)/ (2,0)/',
          '(1,0)/ (3,0)/ (-4,5)/ (0,-3)/ (1,-2)/ (0,-3)/ (-3,-4)`/` (3,0)/ (2,0)/ (-5,0)/ (4,-5)/ (2,0)/ (-2,0)/ (6,0) ',
          '(-5,0)/ (-3,6)/ (-3,0)/ (0,-3)/ (-4,-4)/ (6,-3)/ (-5,0)`/` (-3,0)/ (-1,0)/ (0,-3)/ (0,-2)/ (-4,-3)/ (6,0)/',
          '(-2,-3)/ (0,-3)/ (-4,2)/ (3,0)/ (0,-3)/ (-3,-3)/ (4,0)`/` (3,0)/ (-4,0)/ (-5,0)/ (2,0)/ (5,0)/ (-2,-3)/',
          '(-3,2)/ (3,0)/ (0,-3)/ (0,-3)/ (-5,-5)/ (-4,-1)/ (-2,0)`/` (-3,0)/ (-3,-2)/ (4,-1)/ (0,-5)/ (2,0)/ (-2,-2) ',
          '(-5,0)/ (3,0)/ (-1,5)/ (-3,0)/ (0,-3)/ (1,-5)/ (0,-4)`/` (-3,-3)/ (0,-4)/ (-5,0)/ (3,0)/ (6,0)',
          '(-2,0)/ (3,0)/ (-4,2)/ (0,-3)/ (-5,-5)/ (-3,0)/ (6,-1)`/` (-3,-3)/ (-5,0)/ (4,-4)/ (6,-4)/ (2,0)/',
          '(0,5)/ (-3,0)/ (1,-5)/ (-3,-3)/ (0,-3)/ (6,-1)`/` (3,0)/ (0,-5)/ (2,0)/ (-4,0)/ (-2,-4)/ (-3,0)/',
          '(-3,-1)/ (1,4)/ (-3,0)/ (0,-3)/ (3,0)/ (0,-4)`/` (3,0)/ (-4,0)/ (-3,0)/ (-4,-2)/ (6,-1)',
          '(1,-3)/ (0,3)/ (-4,-4)/ (-3,-3)/ (0,-3)/ (0,-3)/ (0,-5)`/` (-3,-3)/ (2,0)/ (-5,0)/ (-4,-1)/ (6,-4)',
          '(4,0)/ (-3,3)/ (2,-1)/ (-3,0)/ (4,-5)/ (3,0)/ (-4,0)`/` (-3,0)/ (6,-1)/ (0,-2)/ (0,-4)/ (6,-2)',
          '(0,5)/ (-3,3)/ (-2,-5)/ (6,0)/ (-4,-1)/ (0,-3)/ (-5,0)`/` (0,-3)/ (5,-2)/ (-4,-2)/ (3,0)/ (0,-2)/ (-1,-4)',
          '(0,5)/ (4,-2)/ (5,5)/ (0,-3)/ (1,-5)/ (0,-3)/ (-1,0)`/` (0,-3)/ (0,-3)/ (-3,-4)/ (-2,-5)/ (-1,-2)',
          '(0,-1)/ (-5,-2)/ (-3,0)/ (-1,-1)/ (6,-3)/ (1,0)`/` (0,-3)/ (0,-3)/ (-3,-5)/ (-1,-2)/ (-4,0)',
          '(0,5)/ (1,1)/ (3,0)/ (5,-1)/ (3,0)/ (0,-3)/ (6,-2)`/` (-3,0)/ (-2,-1)/ (-4,-3)/ (0,-2)/ (-4,-1)',
          '(4,-3)/ (0,-3)/ (-4,-4)/ (6,-3)/ (1,-5)/ (-1,0)`/` (0,-3)/ (0,-1)/ (-2,-4)/ (-4,0)/ (2,-2)/ (2,0)/',
          '(1,0)/ (3,0)/ (-3,6)/ (-4,-4)/ (0,-3)/ (-5,-2)/ (0,-1)`/` (-3,-3)/ (5,-2)/ (-2,-2)/ (1,0)/ (6,0)/',
          '(-3,-4)/ (1,-2)/ (3,0)/ (-3,0)/ (3,0)/ (-3,-3)/ (-4,0)`/` (3,0)/ (1,0)/ (-2,-4)/ (6,-5)/ (-3,0)/ (6,0)/',
          ' (-5,0)/ (3,0)/ (-3,0)/ (0,-3)/ (-4,-1)/ (1,-2)/ (3,-1)`/` (0,-3)/ (0,-3)/ (0,-1)/ (2,0)/ (4,-4)/ (2,-4) ',
          '(4,3)/ (-4,-1)/ (-2,-5)/ (2,-1)/ (4,-2)/ (0,-1)`/` (6,0)/ (-3,0)/ (-4,0)/ (-5,0)/ (4,-3)/ (-5,0)/',
          '(0,-4)/ (-2,-2)/ (3,0)/ (2,-4)/ (0,-3)/ (4,-5)/ (5,0)`/` (-3,0)/ (0,-3)/ (-2,0)/ (-2,0)/ (0,-1)/ (0,-2)/ (0,-3)',
          '(4,0)/ (6,0)/ (0,3)/ (-1,-4)/ (-2,-5)/ (2,-1)/ (4,0)`/` (-3,-3)/ (1,0)/ (-2,-2)/ (0,-2)/ (0,-2)/',
          '(-5,0)/ (-3,6)/ (5,-4)/ (-5,-2)/ (5,-1)/ (1,-3)`/` (-3,-3)/ (-1,0)/ (0,-4)/ (-5,-2)/ (-1,0)/ (5,0)/',
          '(1,0)/ (0,3)/ (2,2)/ (6,0)/ (-2,-2)/ (0,-4)`/` (-3,0)/ (3,0)/ (-4,0)/ (4,0)/ (-2,0)/ (-4,-3)/ (0,-4)',
          '(0,-1)/ (0,-3)/ (3,0)/ (0,-3)/ (-3,-3)/ (6,0)/ (-2,0)`/` (0,-3)/ (-1,0)/ (4,0)/ (0,-3)/ (0,-4)/ (-1,0)/ (6,0) ',
          '(-2,-3)/ (3,0)/ (-3,0)/ (-4,-1)/ (-5,-3)`/` (3,0)/ (2,-5)/ (6,-2)/ (0,-4)/ (-1,0)/ (1,0)/ (3,-2)/',
          '(0,-1)/ (3,0)/ (4,4)/ (6,0)/ (5,-4)/ (0,-3)/ (-3,-2)`/` (3,0)/ (3,0)/ (4,0)/ (4,-1)/ (-5,0)/ (-2,0)/',
          '(4,0)/ (6,3)/ (2,2)/ (0,-3)/ (3,0)/ (-3,-3)/ (-5,0)`/` (3,0)/ (3,-5)/ (3,0)/ (5,0)/ (0,-2)/ (-5,-4) ',
          '(3,2)/ (3,0)/ (-5,-2)/ (3,0)/ (2,-4)/ (3,-5)`/` (0,-3)/ (0,-1)/ (0,-4)/ (4,0)/ (6,0)/ (0,-2)/ (-5,-3)',
          '(-2,3)/ (5,-1)/ (3,0)/ (1,-2)/ (2,-4)/ (0,-5)`/` (0,-3)/ (0,-1)/ (1,0)/ (-3,0)/ (-1,-4)/ (2,-2)',
          '(0,-4)/ (0,3)/ (-2,-2)/ (0,-3)/ (-3,0)/ (-1,-1)/ (3,-2)`/` (0,-3)/ (4,-1)/ (4,0)/ (-3,0)/ (-2,0)/',
          '(0,-1)/ (6,3)/ (-3,6)/ (-2,-2)/ (3,0)/ (6,-1)`/` (3,0)/ (-4,-3)/ (0,-4)/ (1,0)/ (0,-2)/ (-4,-5)/',
          '(0,-4)/ (-3,0)/ (4,4)/ (0,-3)/ (-4,-4)/ (-5,0)`/` (0,-3)/ (-3,-2)/ (-1,0)/ (0,-2)/ (-5,-4)/ (-4,0)/',
          '(0,-1)/ (-2,4)/ (0,3)/ (-3,0)/ (5,-1)/ (-3,-5)`/` (6,-3)/ (-4,-5)/ (-2,-3)/ (4,0)/ (-2,0)/ (-2,0)/',
          '(4,3)/ (5,-1)/ (6,-3)/ (-2,-5)/ (2,-4)/ (0,-2)`/` (-3,0)/ (0,-1)/ (-4,0)/ (-2,0)/ (2,0)/ (5,-2) ',
          '(1,0)/ (-1,-4)/ (4,-5)/ (5,-1)/ (3,0)/ (-3,-5)`/` (0,-3)/ (6,0)/ (0,-5)/ (4,-1)/ (0,-5)/ (-4,0)/ (0,-2)/',
          '(-2,3)/ (0,3)/ (0,-3)/ (-3,0)/ (-1,-1)/ (0,-3)/ (-3,-5)`/` (0,-3)/ (4,-1)/ (4,0)/ (-1,0)/ (4,0)/ (0,-4)/ (4,0)',
          '(0,-1)/ (-3,0)/ (-5,-2)/ (0,-3)/ (-3,0)/ (2,-1)/ (-2,-3)`/` (0,-3)/ (5,-2)/ (0,-2)/ (1,0)/ (6,-2)/ (3,0)/',
          '(1,0)/ (5,2)/ (4,-5)/ (-1,-4)/ (1,-2)/ (0,-4)`/` (0,-3)/ (-3,0)/ (3,0)/ (-4,0)/ (1,-4)/ (6,-4)/ (4,0) ',
          '(-5,3)/ (-4,-1)/ (3,-3)/ (4,-5)/ (3,-3)/ (0,-4)`/` (-3,0)/ (0,-3)/ (0,-3)/ (-5,-3)/',
          '(-5,0)/ (5,2)/ (3,0)/ (3,-3)/ (-2,-5)/ (5,0)`/` (0,-3)/ (0,-1)/ (1,-4)/ (2,0)/ (3,-2)/ (1,-3)/',
          '(1,-3)/ (-1,-4)/ (4,-2)/ (0,-3)/ (-4,-1)/ (4,0)`/` (-3,0)/ (-1,0)/ (4,-5)/ (-4,0)/ (4,-4)/',
          '(3,2)/ (-2,1)/ (3,0)/ (3,0)/ (5,-1)/ (6,-2)`/` (3,0)/ (0,-4)/ (-5,0)/ (0,-2)/ (2,-3)/ (-3,-2)/ (-5,0)',
          '(0,-4)/ (-2,-2)/ (0,3)/ (-3,0)/ (-1,-1)/ (3,-3)/ (4,0)`/` (-3,-3)/ (3,0)/ (-2,0)/ (4,0)/ (-1,-2)/ (-4,-1)',
          '(-3,-4)/ (-5,4)/ (2,-1)/ (3,-3)/ (-5,-3)`/` (0,-3)/ (5,0)/ (0,-2)/ (-4,0)/ (1,-2)/ (-2,0)/ (0,-4)/',
          '(0,5)/ (3,3)/ (0,-3)/ (1,-2)/ (-3,0)/ (6,-3)/ (0,-4)`/` (-3,-3)/ (-5,-4)/ (0,-2)/ (-2,-5)/ (0,-5) ',
          '(-2,3)/ (3,0)/ (-1,-1)/ (-5,-2)/ (2,-4)/ (1,0)`/` (3,0)/ (-3,0)/ (-3,-5)/ (-1,-2)/ (0,-2)/ (6,-2)/',
          '(1,0)/ (5,5)/ (4,-2)/ (-4,-1)/ (0,-3)/ (3,0)/ (0,-2)`/` (0,-3)/ (-2,-1)/ (3,-4)/ (4,-3)/ (4,-4) ',
          '(-2,0)/ (0,-3)/ (5,-1)/ (4,-2)/ (-1,-4)/ (-3,0)/ (0,-5)`/` (-3,0)/ (-2,0)/ (0,-3)/ (0,-1)/ (4,0)/ (2,-2)/',
          '(-2,0)/ (-3,0)/ (-1,-4)/ (-3,0)/ (-2,-2)/ (-1,-1)/ (0,-2)`/` (-3,-3)/ (-4,-5)/ (-4,-2)/ (3,0)/ (4,0)/ (6,0) ',
          '(1,0)/ (-1,2)/ (4,4)/ (-3,0)/ (2,-4)/ (-3,0)/ (0,-5)`/` (-3,-3)/ (-3,0)/ (5,-3)/ (-4,-4)/ (5,0)/',
          '(1,0)/ (5,-4)/ (1,-2)/ (2,-4)/ (4,-5)/ (2,-3)`/` (-3,0)/ (-2,0)/ (5,0)/ (2,-1)/ (6,-5)/ (-4,-2) ',
          '(1,0)/ (5,-4)/ (-5,4)/ (0,-3)/ (-4,-1)/ (3,0)/ (-5,0)`/` (0,-3)/ (-3,0)/ (6,-4)/ (0,-4)/ (-2,-5) ',
          '(0,5)/ (3,0)/ (-3,6)/ (-3,0)/ (-5,-2)/ (3,0)/ (-1,0)`/` (3,0)/ (-5,-3)/ (-4,0)/ (4,0)/ (-2,0)/ (-4,0)/ (3,0)/',
          '(-5,0)/ (-1,5)/ (4,-2)/ (-1,-1)/ (-3,0)/ (0,-3)/ (0,-2)`/` (-3,-3)/ (-2,-1)/ (0,-4)/ (-4,-2)',
          '(0,2)/ (4,-5)/ (-3,0)/ (-1,-1)/ (-5,-2)/ (0,-3)/ (-4,0)`/` (6,-3)/ (2,-5)/ (-2,0)/ (1,0)',
          '(-3,-1)/ (-5,-2)/ (2,-1)/ (4,-5)/ (6,-3)/ (0,-4)`/` (-3,0)/ (5,0)/ (-2,0)/ (-4,0)/ (0,-5)/ (-4,0)/ (6,-2) ',
          '(-3,-1)/ (0,3)/ (-2,-5)/ (-3,0)/ (-1,-1)/ (-3,0)/ (4,0)`/` (3,0)/ (3,-3)/ (1,-4)/ (-2,0)',
          '(0,5)/ (-3,0)/ (3,0)/ (3,0)/ (-3,-3)/ (-2,-5)/ (0,-1)`/` (0,-3)/ (-3,-2)/ (5,-2)/ (0,-2)/ (3,-4)/ (5,0)/',
          '(-5,3)/ (-1,2)/ (-5,-2)/ (3,0)/ (6,0)/ (-3,0)/ (-4,0)`/` (6,-3)/ (2,0)/ (3,-5)/ (4,0)/ (-2,0)/ (-4,0)/',
          '(-3,-4)/ (-3,0)/ (-5,4)/ (2,-4)/ (-2,-5)/ (-1,-3)`/` (-3,-3)/ (0,-5)/ (0,-2)/ (6,-2)/ (-2,0)/ (0,-5)',
          '(-5,0)/ (3,0)/ (-3,0)/ (5,-1)/ (-2,-2)/ (3,0)/ (0,-1)`/` (3,0)/ (-4,-5)/ (-3,-4)/ (3,0)/ (6,-4)/ (6,0)/',
          '(0,5)/ (0,3)/ (1,-5)/ (0,-3)/ (-3,0)/ (-1,-1)/ (-5,0)`/` (0,-3)/ (-1,-2)/ (0,-2)/ (0,-4)/ (0,-5)/ (0,-4)/ (-5,-4)',
          '(4,0)/ (5,2)/ (0,-3)/ (4,-5)/ (0,-3)/ (3,0)/ (0,-4)`/` (-3,0)/ (3,-3)/ (5,0)/ (2,0)/ (-2,0)/ (2,0)/',
          '(1,0)/ (-4,2)/ (0,3)/ (-3,0)/ (3,0)/ (4,-5)/ (3,-1)`/` (-3,-3)/ (-5,0)/ (4,0)/ (0,-4)/ (-5,-4)/ (0,-3)',
          '(0,2)/ (0,3)/ (6,3)/ (4,-5)/ (-3,-3)/ (-3,0)/ (-4,0)`/` (0,-3)/ (4,-1)/ (4,0)/ (0,-2)/ (0,-3)/',
          '(0,2)/ (0,3)/ (6,3)/ (4,-5)/ (-3,-3)/ (-3,0)/ (-4,0)`/` (0,-3)/ (4,-1)/ (4,0)/ (0,-2)/ (0,-3)/',
          '(1,0)/ (-3,3)/ (-1,2)/ (-3,-3)/ (-2,-5)/ (3,-4)`/` (3,0)/ (6,-5)/ (0,-4)/ (3,-4)/ (6,-3)/ (-4,0)',
          '(-2,-3)/ (5,2)/ (4,-2)/ (-3,0)/ (-1,-4)/ (-2,-3)`/` (-3,-3)/ (-1,-4)/ (6,-4)/ (0,-2)',
          '(-2,3)/ (3,-3)/ (2,-4)/ (-3,0)/ (-5,0)`/` (-3,0)/ (0,-2)/ (0,-1)/ (3,-2)/ (-2,0)/',
          '(4,-3)/ (6,-3)/ (5,-4)/ (-3,-3)/ (-2,0)`/` (0,-3)/ (3,0)/ (4,0)/ (0,-2)/ (6,-1)/ (4,0)/ (-3,-4)/ (0,-4)',
          '(4,0)/ (0,3)/ (-1,-4)/ (-5,-5)/ (0,-3)/ (-3,-3)/ (5,0)`/` (3,-3)/ (-3,0)/ (-2,-1)/ (6,-4)/ (0,-1)/',
          '(4,0)/ (0,6)/ (2,2)/ (0,-3)/ (-5,-5)/ (-1,-4)/ (-5,0)`/` (0,-3)/ (0,-2)/ (6,-1)/ (-4,0)/ (6,-5)/ (0,-2)',
          '(0,5)/ (-3,0)/ (1,1)/ (0,-3)/ (6,0)/ (-4,-1)/ (-2,0)`/` (-3,-3)/ (-1,0)/ (4,-4)/ (0,-2)/ (0,-4)/ (-1,0)/',
          '(-5,-3)/ (-1,2)/ (-3,0)/ (0,-3)/ (-2,-5)/ (-3,0)/ (-1,0)`/` (-3,0)/ (4,-3)/ (2,0)/ (4,0)/ (-4,-3)/ (4,0)',
          '(0,-4)/ (1,-2)/ (5,2)/ (4,-5)/ (3,0)/ (-3,-1)`/` (0,-3)/ (-1,0)/ (0,-4)/ (-2,0)/ (-5,-4)/ (0,-2)/ (-3,0)',
          '(0,-1)/ (-5,-2)/ (-3,0)/ (-4,-1)/ (1,-2)/ (-1,0)`/` (0,-3)/ (4,-1)/ (4,0)/ (-1,-2)/ (2,0)/ (-2,0)/ (6,0)',
          '(-2,0)/ (-1,2)/ (1,4)/ (-1,-4)/ (-5,-2)/ (-4,0)`/` (0,-3)/ (0,-1)/ (0,-4)/ (0,-5)/ (4,0)/ (2,0)/ (-5,0)',
          '(0,-1)/ (3,0)/ (1,-5)/ (6,-3)/ (-4,-1)/ (-3,0)/ (1,0)`/` (0,-3)/ (-3,-2)/ (-3,-2)/ (0,-4)/ (-4,0)',
          '(0,-4)/ (-2,1)/ (5,2)/ (-2,-5)/ (3,0)/ (0,-4)`/` (-3,0)/ (-1,-2)/ (-2,0)/ (-5,0)/ (-4,0)/ (-4,0)/ (6,-4)',
          '(0,-1)/ (-3,0)/ (1,-2)/ (3,-3)/ (0,-3)/ (3,0)/ (-1,-3)`/` (-3,-3)/ (2,-5)/ (-4,-2)/ (3,-4)/ (2,0)/',
          '(-2,3)/ (-1,2)/ (1,-2)/ (3,0)/ (-4,-4)/ (0,-2)`/` (-3,-3)/ (-2,-1)/ (-2,0)/ (0,-5)/ (0,-1)/ (0,-5)/ (2,0)',
          '(-2,-3)/ (-3,0)/ (-1,2)/ (-3,-3)/ (0,-3)/ (-2,0)`/` (0,-3)/ (5,-2)/ (-4,0)/ (0,-2)/ (-5,0)/ (0,-2)/ (6,-5)']
    sq_turn = sq_list[randint(0,99)]
    return sq_turn


def redi():
    redi_list = ["L' R L' R x L R L' R x R L' R' x L R L x L R' L R L' x L R L x R L' R' x R' L' R'",
                 "L R L' R' L x R' L R L' x L' R L' x L R' L' R' L' x R' L R L x R' L' R' x R L' R' L' R x L R' L R L'",
                 "L' R L R L' x R L R' L' R' x R L R L' R x L' R L' R' L x R' L' R x R' L' R' L' x L' R L' R x L' R L' R",
                 "L' R L R' x R L' R' x R' L' R x R' L' R L' x R L' R' L' x L R L x L' R' L x R' L' R' L'",
                 "L' R' L' x R L R x L R L R x L' R' L' R x L' R L' R' x R L' R x R' L R' x R L R L'",
                 "L R' L' R x L R L R' L x L R' L R' x L R' L R x R' L' R' x L R L' R x L R L' x R' L' R",
                 "R' L R' L x L R' L R x R' L' R' L' x L' R L R' x R' L' R' L' R' x R' L' R' L' x R' L' R' L' R' x R L' R' L R'",
                 "R' L R' x R L' R' x R' L R x R' L' R L' R' x R L R' L' x L' R' L' x R L R x R L R' L R'",
                 "R L R' L x L' R' L R L' x R L R' L' x R' L' R x R' L' R x L' R L R' x L R' L' R' x L' R L' R'",
                 "R' L' R x L R L' R' L' x R L R L R x R' L R' x L' R L R' L' x L' R L' R' L' x R L' R' L R x L R L' R' L",
                 "L' R' L R x R' L R' L' x L R' L R x R' L' R' x L' R' L R' L x L R' L R L x R' L' R' L' x R L R' L'",
                 "L R' L x R' L R L' x R L' R L x R L R' L R x L R' L' x R' L' R x R' L R' x L' R' L",
                 "R L' R' L x R L R' L R x R' L R' L R' x R' L R' L' R x R' L' R L' R x R L R' L' x L' R L R' x R' L' R' L",
                 "L R L' R' x L' R' L' R L' x R L' R L x R L' R L' R' x L' R' L' R' L' x L R' L' R x R L R' L' x R' L R L",
                 "L' R' L R' L' x L R' L R' L x R' L R L' R x R L' R L' R x R L R L R x R L R L' x L' R' L' R x L R' L' R' L",
                 "L' R L R L x L' R L' x L R' L x L R' L x R' L' R L' R x L R L x L' R L x L R L R'",
                 "L R' L x L R L' R L' x R' L R L x L R L' R L x L' R' L' x R L R x L' R' L R x L R L'",
                 "R' L R' L' x L' R L' R' x L R' L' x L' R' L R x L R' L' x R L R x L' R' L x R L' R' L R'",
                 "L' R' L R x L R L R L x L' R' L R L x L R L x L R L' R' L' x R' L R x L R' L' R' x R L R' L' R'",
                 "R L' R L R' x R L R' L' R x L R' L' R L' x R' L' R' x L' R' L' x R' L' R' x R L R x L R L' R",
                 "R L R' L x R L' R L' R x L' R' L' R' L x L' R L' x R' L' R' L' x R L' R L x R' L' R' L' R x L' R L'",
                 "R' L R L R x L' R' L R L' x R' L R' L R' x L R' L' x R' L' R' L' R x L' R' L' x R' L R' x R' L R L",
                 "L R L' x R L' R L x L R' L x R L' R x R L R' L R x L' R' L x R' L R L' R' x R' L' R L'",
                 "L R L' x R L' R' L R' x R L R' L R' x R L' R L x L' R L' x L' R L x R' L' R' L R x R L R",
                 "R' L R' L x L R' L x L R' L' R L x R L' R L' x R L' R L R' x L R' L R' x R' L' R x L' R L R",
                 "R' L' R L x L' R L' x L R' L' R x R L' R L' R x R L' R' x R L' R L' R x L' R L x L' R' L'",
                 "R L R L' x R' L R x L R L R' x R' L' R L' R x R' L' R L' R' x L' R L' x R' L' R x R' L R'",
                 "L' R' L x R L R L' x R L R L x L R L x R L R' L' x L R' L' x R L' R L' R x R' L' R'",
                 "L' R L' R L' x L' R' L x R L' R' L' R' x R L R L' R x L' R' L R' x R L' R x L' R L R L' x L' R L",
                 "R L R L x L' R L' R x L R L x L R' L R L' x R' L' R' x R L' R' x L R' L R' x R' L R'",
                 "R' L' R L x L R' L' x L R L' R L x R L R' x R L' R' x R' L' R' L' R x L R L R' x R L R",
                 "L' R L R L x R' L' R' L x R L R' x L' R L' x R L R' L' R x R L R L' x R' L' R L R x L' R L",
                 "L' R L' R' L' x R' L' R L R' x L' R' L R L x L R L' x L R' L R' L x L R L' R x R' L R' x R L R L",
                 "L' R L x L R L' x L R L' x R' L R L x L R' L R' x R' L' R L R x R' L' R x R L R",
                 "L R L' x L' R L R' L' x R' L R' L x R L' R L x R L' R' L' R x R' L R' x L' R' L R x R L' R L' R'",
                 "L R' L R L x R L' R L' x R' L R L' R x L R' L' R' L x R' L R L R x R' L' R' L x R L R' L R x R' L' R' L R",
                 "R' L R L' R x L R L R x R' L R x R' L R' L' R' x L' R' L' R x R' L R' x L' R' L x L R' L R'",
                 "R L R' x L' R L' R' x R L' R L x R' L R L x R L R' x R' L' R L' R x R L' R L R' x L R L'",
                 "L R' L' R' L' x L R L' x L' R' L R L x L R' L' x R L R L x L' R' L R' L' x L' R' L x R L R L R",
                 "L' R L' x R L' R L' x R L R L R x L' R' L x R' L' R x R L R' x L' R' L' R' L x R' L' R' L R",
                 "R L R' L x R' L R L x L R L' x R' L R' L' R x R' L' R L' x R L' R' L R x R L R' x R L' R",
                 "L R L' R' L x R' L R' L' x L' R L' x R L R x L' R' L' R' L x R' L' R L' x L' R L' R' x L R L R'",
                 "R' L R L' R x L R L' R L x R' L' R x R L' R L' x L' R' L' x L' R' L R' x R L' R L x L' R L R L",
                 "R' L R' L R x R L R L' R x R L R L R' x L R L x L R L' x R L R' x L R' L' R x R L' R L' R",
                 "L' R' L' x L R' L R' x L R' L R L x R' L R x R L R L' x L R L R' L' x R L' R' L R' x R' L' R'",
                 "L R' L x R L R' L' R x R L R L R x L R' L' x L' R' L x L R' L x R L' R L R x L R L R'",
                 "R' L R L R x L R L' R' x L R' L' R' x L' R' L R' L x L R L' R' x L R L R' x R L' R' L' x L' R L'",
                 "R' L' R' L' x L R' L R' L' x L' R' L x R' L R' x R' L R x L R' L' x R' L' R L x R' L' R'",
                 "L' R L R L x R' L R L' R x L R' L' R x L R' L' R' L x R L R x R L' R L' x L R L R' L' x R L R' L' R",
                 "L R' L' R x R L R L' x L R' L R' x L R' L' R L x R L' R L' R x L' R' L' R' x L' R' L R x R' L R' L",
                 "R L R' L R x L' R L R' L' x R L' R x R L' R L x L R' L x R' L' R L R' x R L' R' L' R x L' R' L R L",
                 "R' L' R' L x R L' R' L R x L R' L R x R' L R' L' x L R L' R x L' R' L' R L' x R' L R x L R L' R' L",
                 "R L' R x R' L R' L R x L' R L' R' L' x L R' L R L' x L' R' L' R x R L' R L' R x L R L R' x L' R' L'",
                 "L R' L x R L' R x L' R' L R x R L' R x R' L R x R L' R' x L R L R x R' L R' L' R",
                 "R' L' R L' x R' L' R x L R' L R' L' x R L R' L R x L' R L R x L' R L' x R' L' R' L R x L R' L'",
                 "L' R L' R x L R' L R' x L' R' L R' L x R L R x L' R' L R x L R' L R' L x R' L R L' R x L' R' L' R'",
                 "L' R' L' R' L' x R' L R' L R x R L R' x R' L' R' x L R' L' x R' L' R L' R x L R L x R L R' L",
                 "R L R L' R x R' L R' L x R' L R L' R x L' R' L R' L' x R L' R L x L R' L R x L' R' L R' L' x R' L' R' L'",
                 "R' L' R L R' x L' R L R L' x L' R L R L x L' R L R' x L R' L' R' L' x L R L x R' L' R L' R x R L' R'",
                 "R L R' x R L' R' L R x R' L' R L x L R' L R x R' L' R' L R' x L' R L' R x R L R' L R' x L' R' L' R",
                 "R' L' R x L R L R L x R' L' R L' x L R L' R x R L' R x R' L R L R x R L' R L x R' L R' L",
                 "R' L' R' L' R x L' R' L R' L' x L R' L R x R L' R L x R L' R L' x L R L R' L' x R' L' R L x L' R' L",
                 "L R L' R' L x L R L' R' x L R' L R' L x R' L' R' L' x L' R L x R' L R' L' x L R' L' R L' x L' R L' R' L",
                 "R L' R' L x R' L R L R' x R L' R' L' R x L R' L' R L' x L R' L' x L R' L' R' x L R' L R x L R L R L'",
                 "R' L' R L x R' L R' x L R' L R' x L' R' L' x L' R L x L R' L' x R' L' R L' R' x R' L' R",
                 "R L' R' L R x R L' R' L x L' R' L' R' L' x L R L' x L R' L' R x L R' L' R' x R' L R x R' L R L",
                 "L R' L' R L x R L' R' x L' R' L' x L R' L x R' L' R' x L' R' L' x R L R' x L R' L' R L",
                 "R' L R' x L R' L x L R L' R x L' R' L' R x L R' L x R L R' L x L' R L' R' x R' L R' L R",
                 "L R L R' x L' R L x R' L R' x L' R L R x L' R' L x L' R L R x L R L x R' L' R'",
                 "R' L R' L' x L R' L' R L' x L' R L' R' L x R L R L R' x L' R' L' R L x L R' L x L R' L x R' L R L'",
                 "L R L' R x R L' R x R' L' R x L R L x L' R L R L x L' R L R x L' R' L x L R L",
                 "R L R' L R' x L' R L x L R L R' x R L R x L R L R' x R L' R' x R L' R L' x R' L R L",
                 "R' L' R' L R' x R L' R x L R L' x R L' R x L' R' L R' x R L R x L R L R' L x L' R L R",
                 "L R L' R' x R L' R L x L R' L R' L x L R L R x L' R L' x R' L' R L R x R L R' L x R' L' R'",
                 "L R' L' R x R L' R L' R' x L' R' L' x L' R L R L' x R' L R L' R x R L' R' L R x L' R' L x L R L R",
                 "R' L R' x L R L' R L' x L R L' R' x L' R' L' x L R' L R' L' x L' R L R x R L' R' L' x R L R' L' R'",
                 "R' L R x R L' R' L' x R L' R' L' x R L' R L R' x L' R' L x L R L' R' x R' L' R' L' R x R L' R L",
                 "L R L x R L' R x R' L R' x R L R' L' x R' L R L' x L' R' L' R' x L' R L' x R L' R' L",
                 "R' L R' L' x R L' R x L R' L' R' L x R' L' R' L x L' R' L' x L R L' x R' L R' L R' x L' R' L' R",
                 "R L' R' L R' x R' L' R' L R' x L' R' L' R' L' x L R L' R L' x L R L' R L x L' R L x R' L R L' x L R L' R'",
                 "R L R L' x L' R L' x R' L R L' R x L R L R L' x L R L R L' x R L R L R' x L R L x R L' R L R",
                 "R L R L x R L R' x L' R' L R x L R L R' L x L R L' R' x L R L x L R L' R L x L' R L",
                 "R' L' R' x L' R L R x R L R L x R L R' L R' x R L' R L R x L' R L x L' R L' R' x R' L R' L'",
                 "R L' R L R' x R' L R L x R' L' R' x R L' R' L R x R L' R' x R' L' R' L' R' x L R L' R' x L R' L R L",
                 "R L R x R L' R L' R' x L R L' x L' R' L' R x R L R x R L R L x R L R' L' x R' L' R L",
                 "L' R L' R x L' R L x L R' L' x R' L R' L R x L R L R L' x R L' R L R x L' R L R' L' x R' L R L'",
                 "L R' L' R x L R' L R' L' x R' L R' x R' L' R L' R x L R L' x L R L R' x L R' L' R' x R L R' L'",
                 "R' L' R L' R' x R L' R L' x L R L' R' x L' R L' R L x L R L x R L R x L R L R L' x L R L R",
                 "L' R' L' x R' L' R x L' R L' x R' L' R L' x R' L' R' L' R x L' R L' x L' R' L' R x L R' L'",
                 "R L' R L R x R L' R x L R' L x R' L R' x L' R' L R' x R' L R' x L R' L' x L' R L R' L",
                 "L' R' L' x L' R' L' x L' R L x R' L R x R L R L x R' L R' x R' L R' L' x L R L'",
                 "R L' R L x L' R' L R x L R' L R x L R' L' x R' L R' L x L R L' R' L x R' L R' L R x L' R' L' R' L'",
                 "R L' R L' R' x R' L R' x L' R L' R' L x R L R' L x R' L' R L' x R' L R' L R' x L' R L' x L R L R'",
                 "R' L R x R' L' R' L R x R L R' x R' L R x L R L R x R' L' R' L' x L R L x L' R' L R L",
                 "L' R' L' R L x L R L x R L' R x L R L R' x L' R L' R' x L R L' R' L' x R L' R' L x L R L' R L",
                 "R' L R x R L' R' L' R x R' L R' x L R L R x R L R' L x R' L R L x R L R' L' R x L' R' L",
                 "L' R' L R' L' x L' R' L R L x L' R L R' L x L R L' R' x R' L R x L R' L x L' R' L R' x L' R L R L'",
                 "R L' R L' x L' R L' R' x L' R' L R x R' L' R' L x L' R L' x R L R L x L R' L R L' x L R' L' R L",
                 "L R L R' L' x R' L R' x L R' L x L R' L' R' x L' R' L R x R' L R L' x R L R L' R x R' L' R' L' R'",
                 "L R L' R' L x L' R L R x L R L x R L' R' L x R' L R L' x R L R L x L R L x L R L'",
                 "R L' R' L R' x L' R' L R' x L' R' L R L x R' L R x L R L x L R' L' x R L R L x R' L R'"]
    redi_turn = redi_list[randint(0,99)]
    return redi_turn

def pyram():
    pyram_list = ["R B' U R' L R B' L' R r b u ",
                  "L' U L' B' R U' B L' l' r' b u ",
                  "R U R L B' L' B R r u' ",
                  "L B R' L B R B R B' l' r' ",
                  "R U' B L' R' L B' U' l' b u ",
                  "B L B' U L U' R' U r u ",
                  "L B L' U' R' B' L' U l' b u' ",
                  "U L' R B' L R' L R' l r b'",
                  "U L' R U' B' R U B l' r' b u ",
                  "R U' R B U' L' R U' R' l u ",
                  "U L R B R' B R' U' l' ",
                  "B' L' U B' L U' B R l' r b ",
                  "L B' U R L U' B' R U' r ",
                  "L B' U' R L' B' L' R' B l' ",
                  "R' L B' R' U L U L B' l r b u' ",
                  "L' U' R' L R' B' R' L B' l u' ",
                  "U' R U R' L' R L' B' l' r b u' ",
                  "R' B' R' L' R B' L' U r b ",
                  "R' L' B U B' R B R l' r' b u' ",
                  "L B' L' B' L R' B' L l' r' u ",
                  "R B L' B R U B' R L' l' r' ",
                  "B' U B' R B' U L' U r b' u ",
                  "R' B L U' B' R U' R l' r' b' u' ",
                  "R' U' L B R U L' B' l' u ",
                  "B' L R' L B' L' U' L r ",
                  "U' R B U R U L' R l' r' u ",
                  "R' U B' U R' B' R' B' l r' b u' ",
                  "B' U' R B' R B' U' L' l r b u' ",
                  "L R L U' L' R' B' R' l u ",
                  "L' U R' B' U L B R' L' l u'" ,
                  "R' B U' R B R B' U r b' ",
                  "R B' R U B L' U' B' L r' b u ",
                  "L R U' R' B' U L R' r' u ",
                  "U' R' L B L R' U' B' r' b' u' ",
                  "B' L' R U L' B R U' l' r b' u ",
                  "B' R L' R' B U' R' B l b' u ",
                  "L' R' L U' L' U L R l' r b' u",
                  "L R' L R U' B L R' l' ",
                  "U R B' U L' U L' B l r b' u' ",
                  "U' R' B' R' L' U B L' l r' u ",
                  "R' L B L R' L R' B L' l r' b u' ",
                  "B' R' B' L' R L' B U' l' b' ",
                  "R U' L B' U B R' B R' l' b u ",
                  "B' L' B U' L' R' B R' ",
                  "B' R' U R' L' R B L l' r b u ",
                  "L' B R' L' R' B R' B' l' b u' ",
                  "R L' U L B' L U' R' l b u ",
                  "R' L U' R' B' R B' U' l' r' b u' ",
                  "U' L' R' L U R U R r u' ",
                  "B R' B' L B U' L U' l' r' u ",
                  "B U' R L B R' L' B l u ",
                  "B R L' B' U R B L' l' ",
                  "L' U' L B' U' R L B' l' r u ",
                  "B' L R L R' U B' R' r b' ",
                  "R' B R L' U L' B U l' r' b u' ",
                  "R' L' U' L' U' L' R' L b u ",
                  "L' U' R L' R' B' U L' l' u ",
                  "R L' R B' U B' L U' l' r b u' ",
                  "R U L B R U R' U l r' b u' ",
                  "U L' B' R' B U' R' B' l' b' u'",
                  "B L' B R' L R' L U' R' r b u ",
                  "B' L' U' R B' L' R B L l' r' b u ",
                  "R' L' B R B R B R b' ",
                  "U L' R B L' U L' U' l r b u ",
                  "U L' U R' L' B L' B' l' u ",
                  "U R' B' R B R' L R r u ",
                  "L' U B' L B L' R B r b ",
                  "R' U L U R' B R L l' r' b' u ",
                  "U B' L U' R U B' L r b' ",
                  "R L R' L U B' L' U' r u' ",
                  "R' B' U R L' B' U B l' r ",
                  "R L U' R U L' B R' l' r' b u ",
                  "L R' B U' B U' B' L' r b' u ",
                  "U' R' U' R L R' B L u' ",
                  "R U L' B L' R U R' r' b ",
                  "R' B L B' R' U R U' l r u ",
                  "U B U L' R B L' B' R' r b' u ",
                  "U R U B' R' B' L U l' b' u ",
                  "U' B U' R' L B' U' L' U' r u' ",
                  "L' U' R' B U' R B R r' u' ",
                  "R' B' R B' L B' R' L r' b' u' ",
                  "B U R B R B' L R' l' r ",
                  "B' U B' U L' B' U B' L' l' r' b' u ",
                  "L U' B' U R' U' L U' l r' b' ",
                  "B' R' U R' U' B R' B' l b' u' ",
                  "U' R L' B U' B' U' L l r' b' u' ",
                  "B' L' R' L' B' L B L' l' ",
                  "R' L R' L B' R B L l r b' u ",
                  "U' B L B' L R' B U u ",
                  "U' R' B U L' R' U L U r b' u ",
                  "U' B' U' L' R' B' R' U l' r' b ",
                  "R B' L U R L' R' U l' r' b' u ",
                  "R L U B' L' U' R B' l r' b' ",
                  "U' B' L B U L' U' B' ",
                  "R U L' R' U' L R' B l b u' ",
                  "U' B' R L' R U' B' U' b' u ",
                  "U' L' R' B' R' U' B R l' r b u ",
                  "B' L B' R B' U B' U' r b' u' ",
                  "B' U' L R' L' U B R' l' b u' ",
                  "L' R U B' R U L' B' L' l' r' b u' ",
                  "B U L' B' U' L' U L' R B' U' u' l r b"]
    pyram_turn = pyram_list[randint(0,99)]
    return pyram_turn


def one():
    TURN_111 = ("x","y","z","x'","y'","z'","x2","y2","z2")
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 10
    count =0 
    while count < LENGTH:
        turn = choice(TURN_111)
        if turn.find("x") == 0 and pre_turn.find("x") == 0:
            continue
        elif turn.find("y") == 0 and pre_turn.find("y") == 0:
            continue
        elif turn.find("z") == 0 and pre_turn.find("z")  == 0:
            continue
        else:
            scb += turn +' '
            pre_turn =turn
            count += 1
    return scb


cuberandomthree = on_command("3", priority=5)
@cuberandomthree.handle()
async def threesend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '3*3*3\n'+three()
    )


cuberandomtwo = on_command("2", priority=5)
@cuberandomtwo.handle()
async def twosend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '2*2*2\n'+two()
    )


cuberandomfour = on_command("4", priority=5)
@cuberandomfour.handle()
async def foursend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '4*4*4\n'+four()
    )


cuberandomfive = on_command("5", priority=5)
@cuberandomfive.handle()
async def fivesend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '5*5*5\n'+five()
    )


cuberandomsix = on_command("6", priority=5)
@cuberandomsix.handle()
async def sixsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '6*6*6\n'+six()
    )


cuberandomseven = on_command("7", priority=5)
@cuberandomseven.handle()
async def sevensend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '7*7*7\n'+seven()
    )


cuberandomeight = on_command("8", priority=5)
@cuberandomeight.handle()
async def eightsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '8*8*8\n'+eight()
    )


cuberandomnine = on_command("9", priority=5)
@cuberandomnine.handle()
async def ninesend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '9*9*9\n'+nine()
    )


cuberandomten = on_command("10", priority=5)
@cuberandomten.handle()
async def tensend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '10*10*10\n'+ten()
    )


cuberandomeleven = on_command("11", priority=5)
@cuberandomeleven.handle()
async def elevensend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '11*11*11\n'+eleven()
    )


cuberandomtwelve = on_command("12", priority=5)
@cuberandomtwelve.handle()
async def twelvesend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '12*12*12\n'+twelve()
    )


cuberandomthirteen = on_command("13", priority=5)
@cuberandomthirteen.handle()
async def thirteensend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '13*13*13\n'+thirteen()
    )


cuberandomfourteen = on_command("14", priority=5)
@cuberandomfourteen.handle()
async def tourteensend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '14*14*14\n'+fourteen()
    )


cuberandomfifteen = on_command("15", priority=5)
@cuberandomfifteen.handle()
async def fifteensend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '15*15*15\n'+fifteen()
    )


cuberandommapleleaves = on_command("fy", priority=5)
@cuberandommapleleaves.handle()
async def mapleleavessend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = 'maple leaves\n'+leaves()
    )


cuberandompyram = on_command("py", priority=5)
@cuberandompyram.handle()
async def pyramsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = 'pyram\n'+pyram()
    )


cuberandomskewb = on_command("sk", priority=5)
@cuberandomskewb.handle()
async def skewbsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = 'skewb\n'+skewb()
    )


cuberandomclock = on_command("cl", priority=5)
@cuberandomclock.handle()
async def clocksend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = 'clock\n'+clock()
    )


cuberandomminx = on_command("mx", priority=5)
@cuberandomminx.handle()
async def minxsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = 'minx\n'+minx()
    )


cuberandomsq = on_command("sq", priority=5)
@cuberandomsq.handle()
async def sqsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = 'sq1\n'+sq()
    )


cuberandomredi = on_command("re", priority=5)
@cuberandomredi.handle()
async def redisend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = 'redi\n'+redi()
    )