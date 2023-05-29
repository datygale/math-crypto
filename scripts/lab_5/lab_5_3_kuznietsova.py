import random

def miller_rabin_test(n, k): #алгоритм Мілера-Рабіна перевірки, чи є число n ймовірно простим
    if n<=1:#якщо n менше або рівне 1, то воно не є простим, повертаємо False.
        return False
    if n==2:# 2 - просте число
        return True
    

    elif n % 2 == 0: #якщо n парне і не 2, то воно не є простим, повертаємо False.
        return False

    #вводимо допоміжні змінні r та s, щоб подивитись, яким степенем двійки є число n-1.  

    r=0
    s=n - 1
    while s % 2 == 0:#поки ділиться, ділимо на 2 та збільшуємо степінь на 1.
        r += 1
        s //= 2
    for i in range(k):# генерумо k разів випадкові числа від 2 до n-1.
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)#підносимо a до степеня s за модулем n
        if x == 1 or x == n - 1:#якщо число виявилось 1 або n-1, це не суперечить припцщенню про простоту, однак точно сказати не можемо, генеруємо наступне а.
            continue
        for j in range(r - 1):#інакше підносимо r - 1 раз 
            x = pow(x, 2, n)# х до квадрату по модулю n.
            if x == 1: #якщо на якомусь кроці отримуємо 1, то число складене
                return False
            
            if x == n - 1:#якщо n-1, це не суперечить припцщенню про простоту, однак точно сказати не можемо, генеруємо наступне a.
              break
        else:
            return False
    return True#якщо для всіх k чисел суперечності немає, то припускаємо, що число просте.

def df_helman(p, g):#g=5
    if miller_rabin_test(p, min(p, 100))==False:
        print(' помилка. Модуль має бути простим ')
        return(None)
    sA=int(input('Aлісо, введи свій секретний ключ'))%p
    while sA==0 or sA==1 or sA==p-1:
        print('Алісо, введений секретний ключ небезпечний')
        sA=int(input('Aлісо введи свій секретний ключ'))%p #7. g=5. 5**7=...
    pA=pow(g, sA, p)#5**7
    print('Бобе, публічний ключ Аліси:', pA)
    sB=int(input('Бобе, введи свій секретний ключ'))%p#3.  
    while sB==0 or sB==1 or sB==p-1:
        print('Бобе, введений секретний ключ небезпечний')
        sB=int(input('Бобе, введи свій секретний ключ'))%p
    Spilnij_secretB=pow(pA, sB, p)#(5**7)**3=5**21 - спільний секрет
    print('Бобе, ваш з Алісою спільний секрет:', Spilnij_secretB)#5**21
    pB=pow(g, sB, p)#5**3=125
    print('Алісо, публічний ключ Боба:', pB)#5**3
    Spilnij_secretA=pow(pB, sA, p)#(5**3)**7=5**21
    print('Алісо, ваш з Бобом спільний секрет:', Spilnij_secretA)
    return(pA, pB)

    
    
              
    
        
p=int(input('p='))
g=int(input('g='))
print(df_helman(p, g))
    
    