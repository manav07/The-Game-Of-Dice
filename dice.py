import random
def chance(player,scores,target,dice=0,total=0):
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
                total+=chance(player=player,scores=scores,target=target,dice=6,total=total)
    return total


count_check=False
target_check=False
while count_check==False or target_check==False:
    if count_check == False:
        n=(input('Enter the number of players : '))
        if(n.isnumeric()):
            count_check=True
            n=int(n)
        else:
            print('Please enter numeric value')
            continue
    if target_check == False:
        m=(input('Enter the number of points to accumulate : '))
        if(m.isnumeric()):
            target_check=True
            m=int(m)
        else:
            print('Please enter numeric value')
a=[i for i in range(1,n+1)]
sequence=[]
for i in range(n-1,0,-1):
    tmp=random.randint(1,i)
    sequence.append(a[tmp])
    del a[tmp]
sequence.append(a[0])
print('Sequence for this round is : ')
for i in sequence:
    print(f'Player-{i}')
a=[0]*(n)
count=0
check={i:'' for i in range(1,n+1)}
rank=1
position=sequence
while len(check)>1:
    player=sequence[(count%n)]
    if player not in check:
        count+=1
        continue
    if check[player]=='skip':
        check[player]=''
        print(f'Sorry player-{player} your chance is skipped for this round')
        count+=1
        continue
    total=chance(player,a,m)
    a[player-1]=a[player-1]+total
    print(f'Player-{player} score : {a[player-1]}')
    for i in range(len(position)-1):
        if position[i] not in check:
            continue
        if position[i]==player:
            break
        if a[position[i]-1]<a[player-1]:
            position.remove(player)
            position.insert(i,player)
            break
    print('\nCurrent rankings are:')
    for i in range(len(position)):
        print(f'Rank {i+1} : Player-{position[i]}, Points : {a[position[i]-1]} ' )

    if a[player-1] > m-1:
        print(f'\nCongrats Player-{player}, Your rank is {rank}')
        #a[player-1]=m
        rank+=1
        del check[player]
    count+=1
print(f'\nBad luck Player-{list(check.keys())[0]}, you lost the game')

    
    
        

        
    
        
    