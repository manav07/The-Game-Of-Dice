def takeInput():
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
    return (n,m)