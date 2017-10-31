_author_='dev'
_title_='Ip Address program'
ip_address='127.0.0.1'
#ip_address=input('Enter your IP address : ')
segment=0
a=[]
for x in ip_address:
    if x == '.':
        a.append(x)
        
    elif x!='.':
        a.append(x)

    else x=='.':
        segment+=1
        


print(''.join(a))
print(segment)

