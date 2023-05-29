def find_tvir(n):
    tvirni=[]
    for a in range (2, n):
        a_=a
        for i in range (2, n):
            a_=a_*a%n
            if a_==1:
                if i==n-1:
                    print(a, 'твірний')
                    tvirni.append(a)
                    break
                else:
                    
                    print('порядок елемента', a, ":", i)
                    break


find_tvir(5)
#{ 2, 3, 4}


