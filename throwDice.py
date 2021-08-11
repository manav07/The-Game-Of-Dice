import random

def chance(check,player,scores,target,dice=0,total=0):
    print(f'\nPlayer-{player} its your turn, press any key to roll dice')
    side=random.randint(1,6)
    input()
    print(f'your dice rolled to {side}')
    if (scores[player-1]+side) > (target-1):
        return (side)
    if side==1:
        total=side
        if check[player]=='warn':
            check[player]='skip'
            print('Oops chance skipped')
        else:
            check[player]='warn'
            print('If in next chance you get 1, your chance will be skipped')
    else:
        total=side
        check[player]=''
        if side==6:
            if dice!=6:
                print('Congrats play again')
                total+=chance(check=check,player=player,scores=scores,target=target,dice=6,total=total)
    return total