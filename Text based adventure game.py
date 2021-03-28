def start():
    global key
    global current
    print ('What would you like to do, go to door? go to window? or check out the lamp?')
    user = input ('(Door(d)/window(w)/lamp(l)')

    if user == 'd' :
        check_door()
    elif user == 'w' :
        check_window()
    elif user == 'l' :
        check_lamp()
    else :
        print ('You are not still little sleepy and sleep again')
        start()


def check_door():
    global key
    global current
    if key == 'y' :
        print ('You open the door and escape')
    else :
        print ('Door is locked. Find another way')
        search = input ('Check window(w) or lamp (l)')

        if search == 'w':
            check_window()
        elif search == 'l':
            check_lamp()
        else:
            print ('You are still dizzy!')
            check_door()


def check_window():
    global key
    global current
    if current == 'y':
        print ('You see a ledge and hop on to it. After many bruises, you climb down safely and escape!')
    else :
        win_check = input ('It is pitch dark. Try to climb down (d) or check room again(r)?')

        if win_check == 'd':
            print ('You try to climb down in pitch dark and you lose your balance and fall down. You are dead')
        elif win_check == 'r':
            start()
        else :
            print ('You are still dizzy')
            start()


def check_lamp():
    global key
    global current
    print ('You go near the lamp and find a wire. You trace the wire and see a switch and turn it on')
    current = 'y'

    check2 = input ('Check the door(d) or window (w)')
    
    if check2 == 'd' :
        check_door()
    elif check2 == 'w' :
        check_window()
    else :
        print ('You are still dizzy and you knock out the lamp. However you kind a key')
        current = 'n'
        key = 'y'
        start()

print ('===============================================Escape the Room========================================================' )
print ('You wake up in a room with no lights! Your eyes gets adjusted to darkness. But you can see only a door, a window and a electric lamp')
key = 'n'
current = 'n'
start()
    
    
