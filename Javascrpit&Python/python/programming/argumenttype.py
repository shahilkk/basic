

# name
# ---------------------------------------
def det(name,age,gender):
    print('name is',name)
    print('age is',age)
    print('gender is',gender)

det('shahil',21,'male')
det(age=21,gender='male',name='harshin')  

# multiplication without using argument
# ---------------------------
def mul(q,w,e):
    t=q*w*e
    print(t)

mul(3,4,4)  



# multiplication using argument
# ---------------------------
def mu(*args):
    res=1
    for i in args:
        res=res*i
    print(res)
mu(8,9,5,4,7,10)    


# arbitory keyword argument
# -----------------------------
def deta(**kwa):
    print('name is',kwa['name'])
    print('gender is',kwa['gender'])
    print('age is',kwa['age'])
    print('place is',kwa['place'])


deta(age=21,gender='male',name='harshin',place='kondotty')
deta(age=22,gender='male',name='shahil',place='arimbra')



# arbitory keyword argument 2nd method
# -----------------------------
def deta(**kwa):
  for i in kwa:
        print(i,kwa[i])


deta(age=21,gen='male',username='harshin',place='arimbra')
    