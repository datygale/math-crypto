Alphabet=['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
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
LETTER_FREQUENCES = {'а': 0.074, 'б': 0.018, 'в': 0.054, 'г': 0.016, 'ґ': 0.001, 'д': 0.036, 'е': 0.017, 'є': 0.008, 'ж': 0.009, 'з': 0.024, 'и': 0.063,
                               'і': 0.059, 'ї': 0.006, 'й': 0.009, 'к': 0.036, 'л': 0.037, 'м': 0.032, 'н': 0.067, 'о': 0.097, 'п': 0.023, 'р': 0.049, 'с': 0.042,
                               'т': 0.057, 'у': 0.041, 'ф': 0.001, 'х': 0.012, 'ц': 0.006, 'ч': 0.019, 'ш': 0.012, 'щ': 0.001, 'ь': 0.030, 'ю': 0.004, 'я': 0.030, }

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
            dict1={'а': 0, 'б': 0, 'в': 0, 'г': 0, 'ґ': 0, 'д': 0, 'е': 0, 'є': 0, 'ж': 0, 'з': 0, 'и': 0,
                               'і': 0, 'ї': 0, 'й': 0, 'к': 0, 'л': 0, 'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0,
                               'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0, 'ь': 0, 'ю': 0, 'я': 0}

            for j2 in d_text:
                if j2 in dict1:
                    dict1[j2]+=1
                else:
                    pass
            xi2_index=0
            
            for j3, j4 in dict1.items():
                xi2_index+=((LETTER_FREQUENCES[j3]*d_len1-j4)**2)/(LETTER_FREQUENCES[j3]*d_len1)
            dict3.update({j:xi2_index})
            
        min_value=(-1, float('inf'))
        for i5, j5 in dict3.items():
            if j5<min_value[1]:
                min_value=(i5, j5)
        
        real_key+=Alphabet[min_value[0]]
    print(real_key)
    return (real_key)
def analyze_encrypted_text(text):
    len1=len(text)
    dict2={}
    for i in range (5, 27):
        suma0=0
        
        for j in range (i):
            flag=0
            dict1={}
            for k in range (j, len1, i):
                flag+=1
                if text[k] in dict1:
                    dict1[text[k]]+=1
                else:
                    dict1.update({text[k]: 1})
                    
            suma=0
            
            for k1 in dict1.values():
                suma+=k1*(k1-1)
                
            suma0+=suma/((flag)*(flag-1))

        suma0/=i
        print(i, suma0)
        dict2.update({i:suma0})
    max_value=(0, 0)
    for i, j in dict2.items():
        if j>max_value[1]:
            max_value=(i, j)
    print(max_value)
    found_key (max_value[0], text)
    proposed = decrypt (text, found_key (max_value[0], text))
    
    return proposed
if __name__=='__main__':
    text=input('text:')
    print(analyze_encrypted_text(text))
