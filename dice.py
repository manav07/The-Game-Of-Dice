
from genSequence import genSequence
from defineInput import takeInput
from throwDice import chance


n,m=takeInput()
sequence=genSequence(n)
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

    #Filter users who have finished the game
    if player not in check:
        count+=1
        continue

    #check if user's chance is to be skipped
    if check[player]=='skip':
        check[player]=''
        print(f'Sorry player-{player} your chance is skipped for this round')
        count+=1
        continue

    total=chance(check,player,a,m)
    a[player-1]=a[player-1]+total #add dice value to total tally of user
    print(f'Player-{player} score : {a[player-1]}')

    #Below for loop is to sort rank after each throw
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

    #Below for loop is to diplay rank and points
    for i in range(len(position)):
        print(f'Rank {i+1} : Player-{position[i]}, Points : {a[position[i]-1]} ' )

    #Check if user has surpassed the target points
    if a[player-1] > m-1:
        print(f'\nCongrats Player-{player}, Your rank is {rank}')
        rank+=1
        del check[player]
    count+=1

print(f'\nBad luck Player-{list(check.keys())[0]}, you lost the game')

    
    
        

        
    
        
    