# search
# -----------------------------------
my_list=[20,40,7,9,6,20]
search_element=int( input('enter an element'))
flag=0
for i in my_list:
    if i==search_element:
        flag=1
        break
if flag==1:
    print(search_element,'found')
else:
    print(search_element,'not found')                
# end search
# ------------------------------------


