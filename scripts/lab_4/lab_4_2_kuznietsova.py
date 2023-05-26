

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



def gcd_(a, b):#ШУКАЄМО НСД a та b. Повертаємо g=gcd(a, b), x, y такі, що g=x*a+y*b
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = gcd_(b % a, a)
        return (g, y - (b // a) * x, x)
 


def multiplicative_inverse(e, phi):#шукаємо обернений по модулю phi.
    g, x, _ = gcd_(e, phi)#якщо по алгоритму Евклыда отримуємо, що числа взаємопрості, то a*x дає остачу 1 по модулю фі, а отже х - обернене до e по модулю фі.
    if g == 1:
        return x % phi



def rsa_initialize(bit_length):#ініцівлізація для RSA. Генеруємо випадкове число q та перевіряємо, чи є воно простим за алгоритмом Мілера-Рабіна.
    q=random.randrange(2**bit_length)
    while miller_rabin_test(q, 100)!=True:
        q=random.randrange(2**bit_length)#Якщо  ні - генеруємо нове випадкове число q та перевіряємо, чи є воно простим за алгоритмом Мілера-Рабіна.

    #аналогічно генерцємо друге число, p.
        

    p=random.randrange(2**bit_length)
    while (miller_rabin_test(p, 100)!=True) or (p==q):
        p=random.randrange(2**bit_length)

    #обчислюємо n, phi    
    n=p*q
    phi=(p-1)*(q-1)
    e = random.randrange(2, phi-1)#генеруємо випадкове число е.
    while (gcd_(e, phi)[0] != 1): #допоки е не буде взаємопростим з phi, збільшуємо e на 1.
        e+=1
        if e>phi-1: #якщо це не допомогло і e стало рівне phi, генеруємо нове e.
            e = random.randrange(2, e)
       
    d = multiplicative_inverse(e, phi)#оскільки ми знаємо e та phi, ми можемо знайти обернене до e секретне d.
    return e, n, d, p, q
    
def rsa_encrypt(msg, n, e):  #щоб зашифрувати повідомлення, ми його підносимо до степеня е за модулем n.
    encrypted=pow(msg, e,n)
    return encrypted


def rsa_decrypt(msg, n, d): #щоб розшифрувати повідомлення, знаючи d, ми його підносимо до степеня d за модулем n.
    decrypted=pow(msg, d,n)
    return decrypted

def rsa_decrypt_crt(msg, p, q, d): #розшифрцвання з використанням китайської теореми про лишки
    mp=pow(msg, d%(p-1), p)
    mq=pow(msg, d%(q-1), q)
    decrypted=(mp*q*multiplicative_inverse(q, p)+mq*p*multiplicative_inverse(p, q))%(p*q)
    return decrypted

e, n, d, p, q=rsa_initialize(8)
print(e, n, d, p, q)
enc=rsa_encrypt(47, n, e)
print('47 зашифровано як:', enc)
dec=rsa_decrypt(enc, n, d)
print('розшифровано:', dec)
dec_=rsa_decrypt_crt(enc, p, q, d)
print('розшифровано за китайською теоремою:', dec_)


