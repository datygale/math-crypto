import math
def dlog(b, base, n):
    #повертає x - дискретний логарифм за основою base: base**x=b(mod n)
    m=int(math.sqrt(n))+1
    print('m=', m)
    y_=pow(base, m, n)
    y=y_
    table=dict()
    for i in range(1, m+1):
        table.update({y:i})# {a**(m*i): i}
        y=(y*y_)%n
    print(table)
    for  j in range (m):
        bb=b*pow(base, j)%n
        if bb in table: #b*(a**j)=a**mi => b= a**(mi-j)
            print(j, bb)
            return(m*table[bb]-j) #i=table[bb]
        
        


print('log10(22) (mod 47)=', dlog(22, 10, 47))
print('log3(37) (mod 101)=', dlog(37, 3, 101)) 
    
