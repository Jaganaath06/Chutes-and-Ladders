
import random
import time

DICE_TOTAL=6
WIN_VALUE=100
TIME=1

snakes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}

ladders = {
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}

turns_text=[
    "Come on..",
    "Yeah! Proceed..",
    "Your turn..",
    "Make it fast.."
]

cmt_snakes=[
    "Oh no! ",
    "Awwww! ",
    "Shroov! "
]

cmt_ladders=[
    "Yayy ",
    "Booyah ",
    "Jumpoo "
]


def rules():
    print('''
Paramapatham --- Text-based-Snakes-and-Ladders-game-using-python
Built by: Jaganaath 

Rules:
    1.Initially both will be at position 0
    2.You will be moved ahead according to the number on the dice
    3.Landing at the foot of ladder takes you to thetop of the ladder
    4.Landing at the head of snake takes you to the tail of the ladder
    5.Person reaching Final position first will win the match
    6.Happy Gaming!!! \n'''
          
        )

def get_player_names():
    name1=input("Enter the name of Person 1: ")
    name2=input("Enter the name of Person 2: ")
    
    return name1.capitalize(),name2.capitalize()

def value_in_dice():
    time.sleep(TIME)
    val=random.randint(1,DICE_TOTAL)
    return val

def got_snake_bite(position,ended_in,player_name):
    print("\n"+random.choice(cmt_snakes)+player_name+",You got a snake bite")
    print("\n"+player_name+"'s Coin got down from "+str(position)+" to ",str(ended_in))

def ladder_jump(position,ended_in,player_name):
    print("\n"+random.choice(cmt_ladders)+player_name+",You got a ladder jump")
    print("\n"+player_name+"'s Coin jumped from "+str(position)+" to ",str(ended_in))

def snake_and_ladder(position,player_name):
    time.sleep(TIME)

    if position in snakes:
        ended_in=snakes.get(position)
        got_snake_bite(position,ended_in,player_name)
    elif position in ladders:
        ended_in=ladders.get(position)
        ladder_jump(position,ended_in,player_name)
    else:
        ended_in=position

    return ended_in
        

def start_game():
    
    player1,player2=get_player_names()
    print("\nGet ready folks!!")
    time.sleep(TIME)
    print("\n---------"+player1+"--VS--"+player2+"---------")
    flag=0
    present_position_1=0
    present_position_2=0

    
    while flag==0:
        tem_value_1=0
        player1_enter=input("\n"+player1+" "+random.choice(turns_text)+"Hit enter to roll the dice ")
        time.sleep(TIME)
        print("\nRolling dice....")
        time.sleep(TIME)
        dice_val=value_in_dice()
        print("\nIt's "+str(dice_val))
        print("\n"+player1+"'s Coin moved from "+str(present_position_1)+" to "+str(present_position_1+dice_val))
        temp_value_1=present_position_1+dice_val

        present_position_1=snake_and_ladder(temp_value_1,player1)
        
        if present_position_1>=100:
            flag=1
            print(player1+" Won the match!!")
        
        
        temp_value_2=0
        player2_enter=input("\n"+player2+" "+random.choice(turns_text)+"Hit enter to roll the dice ")
        time.sleep(TIME)
        print("\nRolling dice....")
        time.sleep(TIME)
        dice_val=value_in_dice()
        print("\nIt's "+str(dice_val))
        print("\n"+player2+"'s Coin moved from "+str(present_position_2)+" to "+str(present_position_2+dice_val))
        temp_value_2=present_position_2+dice_val
        present_position_2=snake_and_ladder(temp_value_2,player2)
        

        print("-"*60)
        if present_position_2>=100:
            flag=1
            print("And at last "+player2+" Won the match!!")




if __name__=="__main__":
    rules()
    
    start_game()
    
