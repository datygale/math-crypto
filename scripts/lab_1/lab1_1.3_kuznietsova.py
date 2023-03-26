Alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dict_letter_to_num={}
dict_num_to_letter={}
n=len(Alphabet)

for i in range (len (Alphabet)):#створюємо ловники: перший - якій букві відповідає який номер, другий - навпаки, якому номеру відповідає яка буква
    dict_letter_to_num.update({Alphabet[i]:i})
    dict_num_to_letter.update({i:Alphabet[i]})
def decrypt (text, key):# розкодування. Працює аналогічно, тілки від номеру букви закодованого слова віднімаємо номер відповідної букви ключа
    text=text.lower()
    key=key.lower()
    
    text_filtered=''
    for i in text:
        if i in Alphabet:
            text_filtered+=i
    key_filtered=''
    for i in key:
        if i in Alphabet:
            key_filtered+=i
    key=key_filtered
    n1=len(key)
    new_text=''
    for i in range (len(text_filtered)):
        new_text+=dict_num_to_letter[(dict_letter_to_num[text_filtered[i]]-dict_letter_to_num[key[i%n1]])%n]
    decrypted=new_text
    if __name__=='__main__':
        print(decrypted)
    return(decrypted)
LETTER_FREQUENCES = {'e' : 12.0,
't' : 9.10,
'a' : 8.12,
'o' : 7.68,
'i' : 7.31,
'n' : 6.95,
's' : 6.28,
'r' : 6.02,
'h' : 5.92,
'd' : 4.32,
'l' : 3.98,
'u' : 2.88,
'c' : 2.71,
'm' : 2.61,
'f' : 2.30,
'y' : 2.11,
'w' : 2.09,
'g' : 2.03,
'p' : 1.82,
'b' : 1.49,
'v' : 1.11,
'k' : 0.69,
'x' : 0.17,
'q' : 0.11,
'j' : 0.10,
'z' : 0.07 }

def found_key (len_of_key, text):
    len1=len(text)
    real_key=''
    for i in range (len_of_key):#розшифровуєм для підпослідовності її ключ
        the_text=''
        dict3={}
        for k in range (i, len1, len_of_key):
            the_text+=text[k]
        for j in range (n):
            d_text=decrypt (the_text, Alphabet[j])
            d_len=len(d_text)
            d_len1=1/d_len
            dict1={'e' : 0,
't' : 0,
'a' : 0,
'o' : 0,
'i' : 0,
'n' : 0,
's' : 0,
'r' : 0,
'h' : 0,
'd' : 0,
'l' : 0,
'u' : 0,
'c' : 0,
'm' : 0,
'f' : 0,
'y' : 0,
'w' : 0,
'g' : 0,
'p' : 0,
'b' : 0,
'v' : 0,
'k' : 0,
'x' : 0,
'q' : 0,
'j' : 0,
'z' : 0}

            for j2 in d_text:
                if j2 in dict1:
                    dict1[j2] += 1
                else:
                    pass
            xi2_index = 0
            
            for j3, j4 in dict1.items():
                xi2_index += ((LETTER_FREQUENCES[j3] * d_len1 - j4) ** 2) / (LETTER_FREQUENCES[j3] * d_len1)
            dict3.update({j: xi2_index})
            
        min_value=(-1, float('inf'))
        for i5, j5 in dict3.items():
            if j5 < min_value[1]:
                min_value = (i5, j5)
        
        real_key += Alphabet[min_value[0]]
    print(real_key)
    return(real_key)


def analyze_encrypted_text(text):
    len1 = len(text)
    dict2 = {}
    for i in range(5, 27):
        suma0 = 0
        
        for j in range(i):
            flag = 0
            dict1 = {}
            for k in range(j, len1, i):
                flag += 1
                if text[k] in dict1:
                    dict1[text[k]] += 1
                else:
                    dict1.update({text[k]: 1})
                    
            suma = 0
            
            for k1 in dict1.values():
                suma += k1 * (k1 - 1)
                
            suma0 += suma/(flag * (flag - 1))

        suma0 /= i
        print(i, suma0)
        dict2.update({i:suma0})
    max_value = (0, 0)
    for i, j in dict2.items():
        if j > max_value[1]:
            max_value = (i, j)
    print(max_value)
    found_key(max_value[0], text)
    proposed = decrypt (text, found_key(max_value[0], text))
    
    return proposed


if __name__ == '__main__':
    text = input('text: ')
    print(analyze_encrypted_text(text))
