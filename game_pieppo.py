import sys,time,os
def typewriter(message):
    for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            
            if char != "\n":
                time.sleep(0.1)
            else:
                time.sleep(1)
os.system("clear") #clear
def start_game():
    os.system("clear")
    print("""
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNNNNNNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXK00OkkkxxxxxkkOO0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0OxxxxxxxxxxxxddddddxkO0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKkxxxxxxxxxxo:,''......';coxOKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkxxkOkOkxxxc'. ';:lodool:. .,lxkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOxxkkkkO0kxo, .:ONMMMMMMMMWXk; .;dxOXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkxxOKOxxkkxo. .xNNWMMMMMMMMMNWNo. ,dxkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMXkxxkOO0kxxxo'  oWXk0WWMMMMMMN0ONNc  ,dxkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMN0xkOOkxkxxxd,  '0W0x0NWMMMMMMNOx0WO.  :xxONMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMXkxkKK0Okxxxc.  :KOdoxOXMMMMMWKxod00,  .lxkXMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMWKxxkkkkxxxxd'   :0c..':xWMMMMNd...o0;   ;xxKWMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMW0xxkOOOkxxxc.   :XNOkKWWMMMMMMW0k0NK,   .ox0WMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMW0xxOKOOOxxx,    ;XNOOXMMMMMMMMWKO0N0'    :x0WMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMXkxkkxkkxxo.    .ONOxKMMMMMMMMW0x0Wk.    'xXMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMWOxxxxxxxxc.     oWXkKMMMMMMMMMKkXWl     .xWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMXkxxxxxxx,      '0WXNMMMMMMMMMNXWO.     .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXkxxxxxo.       :XMMMNOkkkk0WMMK;     .xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOxxxx:         :KMMNklccoONW0;     'kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkxd'          'x0XWWNNWWXd.    .lKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKo.            ..;cccc;.    .l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXx:.                    .:xXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdc,...      ...,coOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNK0OOOOOO0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        \n""")
    time.sleep(3)
    start()
    os.system("clear") #clear
def start():
    os.system("clear")
    name = input("Welcome! What is your name? \n")
    time.sleep(1)
    typewriter("Hello {}\n".format(name))
    time.sleep(1)
    response = input("Would you like to play a game? [Y/N]\n>>> ")
    if response.upper() == "Y" or response.upper() == "YES":
        typewriter("Lets begin!\n")
        start_sequence()
    elif response.upper() == "N" or response.upper() == "NO":
        print ("Ok, see you later!\n")
        time.sleep(2)
        end_game()
    else:
        print("Hmm, I didn't recognise that.")
        time.sleep(3)
        start()        
def start_sequence():
    os.system("clear")
    typewriter("You awaken in a strange place, it's dark and everywhere seems deserted. This is most unusual!\nThere should be people here!\nInstead you notice a restaurant, there is food cooking but no-one is around...\n")
    time.sleep(1)
    typewriter("You notice a delicious bowl of Ramen!!\n")
    time.sleep(1)
    os.system("clear")
    print ("""
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOkKWMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOxooxKWMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0kddk0NWMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWN0kxkOKNWMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOxdx0XWMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0kdodOXWWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXOxoldkKNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOxolok0NWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0kkdodk0XWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXOkkxxkOkOKWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKOkkkxxxk0KXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN000Okkk0NWNXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWN0OKKXNWWWNXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNXXWWXXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXXXWWWXXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXXNWWWMWNXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXNWWNXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNXNWWXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXNNWMWNNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXNWMWWNXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNWWWNXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNNNNNNNWWWWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNXKKKKKKKKKKKKXNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWNXK000KKKKKKKKKKK00KXNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNXXXXK00KKKKKK00KKKK0KKKKKKKKXXXNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMWNXKKKKKKK00KKK00KKKKKKKKKKKKKKKKKKKKKKKXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWWXK0KKKKKK0KKK0KKK00KKKKKKKKKKKKKKKKKKKKKKKKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWXKKKK0KKK00KK0KK00KKK0KKKKKKKKKKKKKKKKKKKKKKKXWMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMWX0000KKKK000K00K00KK00KKK000K00K00000000KK0000KNWWWMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMW0dlllllllllllllllllllllllllllllllllllllllllllllllodKWMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMWx;,;,,,,,,,,,,,,,,;,,;;,,,;,,,;,,,,,,,,,,,,,;,,,,,:OWWMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMWO:,,;;;,,;;;;;,,;,,;,,;;,;;,,,;,;;,,,,,,,;,,;,,;;,lKWWWMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMXo,;,;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,,,;,;xNWMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMWO:,;;,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,;,,lKWMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMWk:,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;,,;c0WMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMNk:,;;,;;;;,,,;;;;;;;;,,,;,,,;;,,,;,,,,;,,;,;l0WMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMN0l;,;;;;;;;;;;;;,,;;;;;;;;;;;;;,;;,,,;,;,;oKWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMWWXx:;,;;;,,,,;;;;,;;;;;;;;;;;;;,,,,,,,;;cONWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWWWWWKxc;,;;,;;;;;;;;;,,;,;;;;;,,;;,;;;;lkXWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXkoc;,,;;;;,,;;;;;,,,;;;,,;;,;cd0NWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXOdl:,,,,,,,;;,,,,;;;,;:ox0XWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMWKl,,;;;;;;;;;;;;;;,;dNWMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKOOOOOOOOOOOOOOOOO0XWWMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """)
    time.sleep(3)
    os.system("clear")
    level_one()
def level_one():
    typewriter("You're super hungry and it looks great!\nBut this is all very suspicious...\n")
    response = input ("Do you eat the Ramen?\n[Y/N]>>>\n")
    if response.upper() == "Y" or response.upper() == "YES":
        print("Oh no! It was a trap!\nYou greedy thing!\nYou've been turned into a Pig!""")
        print("""                           
                                             )\   /|
                                          .-/'-|_/ |
                       __            __,-' (   / \/          
                   .-'"  "'-..__,-'""          -o.`-._   
                  /                                   '/
          *--._ ./                                 _.-- 
                |                              _.-' 
                :                           .-/   
                 \                       )_ /
                  \                _)   / \(
                    `.   /-.___.---'(  /   \\
                     (  /   \\       \(     L\\
                      \(     L\       \\
                       \\              \\
                        L\              L\\
                            """)
        time.sleep(3)
        game_over() 
    elif response.upper() == "N" or response.upper() == "NO":
        typewriter("This is no time for Ramen! This is all too spooky!\n")
        time.sleep(1)
        level_two()
    else: 
        typewriter("Hmm maybe i do want the Ramen..?\n")
        time.sleep(1)
        level_one()
#start_game()
def level_two():
    os.system("clear") #clear previous text
    typewriter("You see a bridge with a castle at the end! Maybe someone knows what's going on?!\n")
    time.sleep(1)
    print("""
       ______________________________________________________
       [[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]
       .-.`| `-/-.__/.-'\_.-._,'/`-._'\_.-._`-'_/-._.'|/.-'\-
       \_.-`./`-._'\__.-`-.__.-`--._/--.`-._\`-._\__.-)`-'._/
       `._-'.\_.---._-.\_`-..`\_.---._`-.__.-`'._.--./`-'._,'
       __/`.-/       `.'_`./`.'       '.\__.-`.'    (_.-\_,-.
       `._-/'          |._.-|           |.'`.|       `(_.`-._
       .-',`)          | /`.|           |`-/`|         ;.-'_/
       `\,-/           |\.-'|           |\-'`|          ;\_,-
        -./`._        [[[[[[[[         [[[[[[[[         .',-'
        `.`--.~~-^_~-/.`-._`-.\^~-_~-^/`-.'-,.'\^~-~_^"'`-.'_
        -,.'"-"~^-~_~- - - _- -~^-_.~ - -_ - - -~- . "'"-"-""
        ""-'"-""-"~- _~.^-~-^.-^_.- .^~.-  ~-. ~^_-""-""-"'-"
           ""-'"-"    ~- ^. - ~ -~^ - ~  ^~- ~     ""-"'-'
    """)
    typewriter("Ghosts start to appear on the bridge! What is happening here??\n")
    time.sleep(4)
    level_three()
def level_three():
    os.system("clear")
    typewriter("As you cross the bridge a spirit sentinel appears!\n")
    print("""
    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0000000000000000000OOOOOOOOOOOkkxkO0KKKKK000OOkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOOOOOOOOOOOO000000KKKKKKKKKKKKKKKKK00000OOOOOkxxxk0XNNNNNNNNNNX0kkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOOOOOOOOOOO0000KKKKKXXXXXXKKKKKKKKKKKK0000OOkxxkkOXNNNNNNNNNNNNNXOkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOOOOOOOOOO00KKKKKKKXXXXXXXXXXXXXXKKKKK0000OkxxkkOKNNNNNNNNNNNNNNNX0kOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOOOOOOOOOO0KKKKKKXXXXXXXXXXXXXXXXKKKKKK00OkdxkkkOKNNNNNNNNNNNNNNNNXOxOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOOOOOOOOOO00KKKKKXXXXXXXXXXXXXXXXXKKKKKK0xllxkkxdONNNNNNNNXX0OXNNNN0ooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOOOOOOOOOO000KKKXXXXXXXXXXXXXXXXXXXXXXKKk;'lkkkdlxKNNNNNNNXKkdOXNNNKc,oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOO0000000000000000KKXXXXXXXXXXXXXXXXXXXXXXXXXO:.'okkkxx0XNNNNNNNNXKOKNNNNXl.,xOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    0000000000000KKKKKK0000000KKKKKXXXXXXXXXXXXXXXXXXXXXXX0c. 'dkxddkKNNNNNNNNNNNXK0KXNXl..lOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    0KK00KKKK0KKKKKKXXXXXKKKKKKKKKKXXXXXXXXXXXXXXXXXXXXXXKd.  ,dxc,.'cONNNNNNNNNOc,'':kKl. ;xOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    KKKKKKKKKKKXXXXXXXXXXXXXXXXXXXKKKXXXXXXXXXXXXXXXXXXNXO;.  ,dkdl:cxKNNNNNNNNNKxcclx0Kc. 'dOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    KKKKKXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKKKKXXXXXXXXXXXXNKl.   'dkxookXNNNNNNNNNNNKOk0XN0:  .lO0OOOOOOOOOOOOOOOOOOOOOOOOOOO
    KKXXXXXXXXXXXXXXXXNNNNNNXXXKKKKKKKKKKKKKXXXXXXXXXNNXk,.   .oko:ckNNNNNNNNNNNNXkoxKNO,  .cOK00000000000000000000000OOOO
    KXXXXXXXXXXXXXXXXXXNNNNNNXXXKKKKKKKKKKKKXXXXXXNXNNXOc.    .lko:cONNNNNNNNNNNNXkoxXNk'  .:OKKKKKKKKKKKKKKKKKKKKKKKK000O
    XXXXXXXXXXXXXXXXXXXXXXNNNNXXXXKKKKKKKKKXXXXXXXNNNX0l.     .ckdcl0NNNNNNNNNNNNNOdOXNd.  .:OXXXXXXXXXXXXXXXXXXXXXXXKKK00
    XXXXXXXXXXXXXXXXXXXXXXXXXNNNXXXXXXXKKKKXXXXXXNNNNKo..     .;xkod0NNNNNNNNNNNNNKOKNXl.  .;OXXXXXXXXXXXXXXXXXXXXXXXKKK00
    XXXXXXXXKKKKKKKKKKKKKKXXXXXNNXXXXXXKKKXXXXXNNNNNKd'.       'okkkKNNNNNNNNNNNNNNNNN0;   .;OXXXXXXXXXXXXXXXXXXXXXXKKK000
    XXXXXKKKKKKKKKKKKKKKKKKKXXXXXNXXXXKKKXXXXXXNXXNXx;.        .ckkk0XNNNNNNNNNNNNNNNNx.   .;kXNNXXXXXXNNXXXXXXXXXXXKK0000
    KKKKKKKKKKKKKKKKKKKKKKKKXXXXXXXKKKKKKKKKXXXXXXX0c..        .;dkkOXNNNNNNNNNNNNNNNKl.  ..:OXNNNNNXXNNNXXXNNNNXXXXXXKK00
    KKKKKK000KKKKKKKKKKKKKKKKKKKKK000000KKKKKKKXXXKd,.          .lkkxoolllllllllldONNO,   ..:ONNNNNNNNNNNNNNNNNNNNNNNNXXK0
    0000000000KKK00KKKKKKKKKKKK00000000000KKKKKKKKk:..          .,dkxl:;,,,,,;::coONXo.   ..;kNNNNNNNNNNNNNNNNNNNNNNNNNXXK
    0000000000000KK0000KKKK00000000000000000KKKKK0o,..           .:xkOKXKOkO0KXNNNNNO,    ..;kXNNNNNNNNNNNNNNNNNNNNNNNNXXK
    000000000000000000000000000000000000000KKKKK0Ol'..            .;ok0XNXKKXNNNNNXO:.   ...;kXNNNNNNNNNNNNNNNNNNNNNNNNXXX
    OOO00000000000O00000000000000O000000KKKKKKKKKk:...             ..,cok00K00OOkdc'.    ...;kXNNNNNNNNNNNNNNNNNNNNNNNXXXX
    xxxkkOO00OxxxxxkkOOOOOOOOOOOOOO00000KKKKXXXXXk:...                 ....'......       ...,xKXXXXXXXXXXXXXXXXXXXXXXXXXXX
    """)
    time.sleep(3)
    level_four()
def level_four():
    os.system("clear")
    typewriter("The spirit hands you some paper, it's a riddle!\nYou must answer before you cross!\n")
    response = input ("What tastes better than it smells?\n>>> ")
    if response.upper() == "TONGUE":
        typewriter("He nods silently with approval, you have answered correctly!\nPhew! That was scary!\nYou may pass!\n")
        time.sleep(1)
        level_five()
    else:
        typewriter("Noo! The Sentinel sweeps his arm and turns you into a ghost!\nNow you'll never escape! You're doomed to wander here evermore!\n")
        time.sleep(1)
        game_over()
#end of section
#begining section2
def level_five():
    typewriter("You've met Haku!\nHaku tells you about the spell the bad witch has cast on the land!\nHe needs your help freeing the Kingdom from the witch's spell!\nHelp him and he will promise to help you get home.\nYou agree to help\nAs a test, Haku asks you a question\n")
    level_six()
    time.sleep(3)
def level_six():
    response = input  ("What is the largest Ocean in the World?\nA- Atlantic Ocean\nB- Indian Ocean\nC- Pacific Ocean\n>>> ")
    if response.upper() == "C":
        print(" Great! You have entered the castle")
        print("""                   .
                          |~~
                          |~~
                         /L\\
                  ,.---./LLL\. _.--.
                .'(|~~`/LLLLL\` )  )`.,
              .(`  |~~/LLLLLLL\   )  )-. .
             (  ( /L\/LLLLLLLLL\ )  )   `|~~
            ((`_./LLL\LLLLLLLLLL\`.)_),.)|~~
                /LLLLL\.=.=.=.=|        /L\\
                 |.=.| .-._.-. |       /LLL\   ~'~
                 |  [| | | | | |      /LLLLL\\
                 |   | | | | | | _   _|] _=.|
        ~'~      |  [| |_|_|_| || |_| |_| | |
                 |  |~~        |=.=.=.=.=.| |       .
                 |  |~~        |    |~~   | |       |~~
                 | /L\ .-._.-. |    |~~   | |       |~~
                 |/LLL\| | | | |   /L\    |/       /L\\
                 |].=.|_ | _ | _  /LLL\   |       /LLL\\
           ,- _--|]] [| |_| |_| |/LLLLL\  |      /LLLLL\\
          (|_| |_|]---|.=.=.=.=./LLLLLLL\ _   _ /LLLLLLL\\
           \.=.=.=|\_/           |.=.=.|_| |_| |_|.=.=.|
           /|[]   |              | []  |.=.=.=.=.|  [] |
           ||     |    .-._.-.   |     | .-----. |     |
           \|     |    | | | |   |     |/|||||||\|     |
            |  [] |    | | | |   |     ]|||||||||[     |
            |  __ |    |_|_|_|   |  [] ]|||| ||||[ []  |
            | /<_\_    ____      |     ]|||| ||||[     |
            |/ |  "\__/  ) \.-.  |     ]|?=||||||[     |_
           /"  )\_ >  ) >\__ ")`\_     ]|||||||||[ ,_./`.\\
        __/ _/ _ ,| \  __  "|_  ) |_   ]|||||||||[/("_ -">\_
       /> )"__/ \___  "  \__  _) \_ -\_.==___===/.<  \__(\_ \\
      /  __/ )___   > \_ ) \  \_ "  ).==_____==( <."/ (_<  \)|
     lc_/>.=__.._\"__\_  >_)___\-_/.=________=/___/.__>__"(__/          
""")
        time.sleep(2)
        os.system("clear")
        level_seven()
    else:
        typewriter("Haku is shamed by your answer.\nHe summons the Spirit Sentinel from the bridge and points at you.\nThe Spirit Sentinel advances towards you and gobbles you up!\n")
        game_over()
def level_seven():
    typewriter("As soon as you walk into the castle, you encounter a slime monster! The smell is terrible!\n")
    response = input("Do you want to give the stinky monster a bath?\n>>>[Y/N] ")
    if response.upper() == "YES" or response.upper() == "Y":
        print("Amazing! It was a River Spirit all along! He is so grateful for a good bath")
        time.sleep(2)
        level_eight()
    elif response.upper() == "NO" or response.upper() == "N":
        print("No way! The monster is so stinky! You wish you were a pig now! You turn and run away!")
        time.sleep(2)
        game_over()
    else:
        typewriter("Hmm...he he stinks, but he wont go away!\n")
        time.sleep(1)
        level_seven()
#end of section 2
#begining of section 3
def level_eight():
    typewriter("The River Spirit offers you an item as thanks if you can complete his riddle!\n")
    response = input("What do computer programmers sing in the shower?\n>>> ")
    if response.upper() == "DISC-O" or response.upper() == "DISCO":
        witch()
    else:
        print("Hmm, that dosent seem right...programmers like to boogie!")
        level_eight
def witch():
    typewriter("The river spirit gifts you a Gold Necklace!\nThe spirit disappears through an open window off into the night!\nHaku and yourself progress to the top of the castle.\nThis where the Witch is!\n")
    time.sleep(2)
    print ("""
                        "     "        _/ /
                     (   *  )    ___/   |
                       )   "     _ o)'-./__
                      *  _ )    (_, . $$$
                      (  )   __ __ 7_ $$$$
                       ( :  { _)  '---  $\\
                  ______'___//__\   ____, \\
                   )           ( \_/ _____\_
                 .'             \   \------''.
                 |='           '=|  |         )
                 |               |  |  .    _/
                  \    (. ) ,   /  /__I_____\\
              snd  '._/_)_(\__.'   (__,(__,_]
                  @---()_.'---@
    """)
    time.sleep(3)
    os.system("clear") #clear
    level_nine()
def level_nine():
    typewriter("The Witch is not happy to see you, in fact she seems unhappy full stop!\nHaku demands that the witch frees the kingdom from her evil spell!!\nThe Witch says she will not do so because something was lost long ago, and unless she gets it back, she will keep the entire kingdom in darkness!\nThe Witch wont tell you what she lost but offers a riddle.\nIf you can solve it maybe you can save the kingdom!\n")
    response = input("I am usually shiny\nIn a jeweller’s I am sold\nI sometimes hold a pendant\nI am a chain that is old\n>>> ")
    if response.upper() == "NECKLACE" or response.upper() == "GOLD NECKLACE":
        print("""
        MMMMMMMMMMMMMMMMMMMMMMMMMWX0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKXWMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMWKKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKKWMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMW0KWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKKWMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMW0KWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX0NMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX0NMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0XMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX0XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWK0NMMMMMMMMMMMMMMMMMMMMMMMMMMMWK0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWK0NMMMMMMMMMMMMMMMMMMMMMMMMMMX0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW00WMMMMMMMMMMMMMMMMMMMMMMMMX0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0KWMMMMMMMMMMMMMMMMMMMMMMX0XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0KWMMMMMMMMMMMMMMMMMMMMN0XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0KWMMMMMMMMMMMMMMMMMMN0KWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOKWMMMMMMMMMMMMMMMMN0KWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXOXMMMMMMMMMMMMMMMW00WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXOXMMMMMMMMMMMMMWK0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXOXMMMMMMMMMMMWK0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKOXMMMMMMMMMWK0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKONMMMMMMMMK0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKONMMMMMMXOXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW00NMMMMXOXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0ONMMNOKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNxd0XkxWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXdcco0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdlllddllolldolld0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo' ..''. .;:'  .....'lKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX: .oKNNNKd;'.'lOXNX0d. '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx. dMMMMMMMWNNNMMMMMMMx. lWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk. dWMMMMMMMMMMMMMMMMMx. lWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX: '0MMMMMMMMMMMMMMMMX; .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO' ,0WMMMMMMMMMMMMMK: .oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO, .dXMMMMMMMMMMNx' .dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKl. 'dXWMMMMWXd,  ;OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l'..ck00xc. .:kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXx:. .  .,o0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c,,:kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        """)
        time.sleep(2)
        os.system("clear")
        print("Yes! The answer is the Gold Necklace!\nThe Witch must have lost it!\nYou think for a moment and reach into your pocket and give her the Gold Necklace you received from the River Spirit!")
        time.sleep(3)
        typewriter("The Witch is shocked and touched by this act of kindness!\nIt melts her heart and she agrees to lift the spell from the Kingdom!\nEverything is good again!\nAnd in addition she agrees to give you your freedom!\nYou can finally return Home! Horray!!\n")
        time.sleep(4)
        end_sequence()
    else: 
        print("The Witch cracks an evil grin.\n'Wrong!' she cries!\n")
        time.sleep(2)
        print("She waves her hand and turns you into a hamster!\nYou are doomed to spend the rest of your life as her pet!\n")
        time.sleep(2)
        print("""
             .     .
            (>\---/<)
            ,'     `.
           /  q   p  \\
          (  >(_Y_)<  )
           >-' `-' `-<-.
          /  _.== ,=.,- \\
         /,    )`  '(    )
        ; `._.'      `--<
       :     \        |  )
       \      )       ;_/  
        `._ _/_  ___.'-\\\\
           `--\\\\
               """)
        game_over()
        #End Game!
def end_sequence():
    print("Thankyou for playing!\nThis has been a game for Code Nation made by:\nNadir, Raissa and Tim\nWith thanks to Liam and Mike.")
    time.sleep(6)
def game_over():
    print("""  
    #####                          #######                      ### 
   #     #   ##   #    # ######    #     # #    # ###### #####  ### 
   #        #  #  ##  ## #         #     # #    # #      #    # ### 
   #  #### #    # # ## # #####     #     # #    # #####  #    #  #  
   #     # ###### #    # #         #     # #    # #      #####      
   #     # #    # #    # #         #     #  #  #  #      #   #  ### 
    #####  #    # #    # ######    #######   ##   ###### #    # ### 
    """)
    time.sleep(2)
    end_game()
def end_game(): 
    print ("Come back soon! :)\n")
    time.sleep(3)
start_game()



