district={'kerala':'trivandrum','tamilnadu':'chennai','bihar':'Patna','assam':'Dispur','arunachal Pradesh':'itanagar','andhra Pradesh':'Amaravati'}
valu=input('  enter a state  ')
for i in district:
    if i==valu:
        print('captical of',i,'is',district[i])
    else:
        print('not found')    
        break