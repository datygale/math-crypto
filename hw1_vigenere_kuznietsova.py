Alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dict_letter_to_num={}
dict_num_to_letter={}

for i in range (len (Alphabet)): #створюємо словники: перший - якій букві відповідає який номер, другий - навпаки, якому номеру відповідає яка буква
    dict_letter_to_num.update({Alphabet[i]:i})
    dict_num_to_letter.update({i:Alphabet[i]})


n=(len(Alphabet))#запам'ятовуємо, скільки всього букв в алфавіті
def encrypt (text, key):#функція для шифрування повідомлення
    text=text.lower()#переводемо всі літери в маленькі
    key=key.lower()

    #фільтруємо текст і ключ від зайіих символів, яких нема в алфавіті
    text_filtered=''
    for i in text:
        if i in Alphabet:
            text_filtered+=i
    key_filtered=''
    for i in key:
        if i in Alphabet:
            key_filtered+=i
    key=key_filtered

    #запам'ятовуємо довжину ключа
    n1=len(key)
    new_text=''

    #основні розрахунки. до номера і-ої букви слова додаємо номер i(mod n1) букви ключа. Отримане число може виявитись быльшим, ніж кількість букв в алфавіті, тому беремо по модулю n.  
    for i in range (len(text_filtered)):
        new_text+=dict_num_to_letter[(dict_letter_to_num[text_filtered[i]]+dict_letter_to_num[key[i%n1]])%n]
    encrypted=new_text
    print(encrypted)
    return(encrypted)# повертаємо закодоване слово

def decrypt (text, key):#розкодування. працює аналогічно, тілки від номеру букви закодованого слова віднімаємо номер відповідної букви ключа
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
if __name__=='__main__':
    test_text=input('text:  ')
    test_key=input('key: ')
    test_encrypted=encrypt(test_text, test_key)
    rez=decrypt(test_encrypted, test_key)
    print('decrypted', rez)
