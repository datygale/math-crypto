import matplotlib.pyplot as plt

Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
dict_letter = {}

for i in range(len(
        Alphabet)):  # створюємо ловники: перший - якій букві відповідає який номер, другий - навпаки, якому номеру відповідає яка буква
    dict_letter.update({Alphabet[i]: 0})

n = (len(Alphabet))  # запам'ятовуємо, скільки всього букв в алфавіті


def calculate_freequency(text):  # функція для шифрування повідомлення
    text = text.lower()  # переводемо всі літери в маленькі

    # фільтруємо текст і ключ від зайіих символів, яких нема в алфавіті
    text_filtered = ''

    for i in text:
        if i in Alphabet:
            text_filtered += i

    n1 = len(text_filtered)  # кількість літер в відфільтрованому тексті
    if n1 != 0:  # якщо в текстіє хоч одна літера, рахуємо частоту
        for i in text_filtered:  # для кожної літери, як тільки її зустрічаємо,  збільшуємо її частоту на 1/n1
            dict_letter[i] += 1 / n1

    fig, ax = plt.subplots()
    print(dict_letter.values())
    ax.bar(dict_letter.keys(), dict_letter.values())
    plt.show()


calculate_freequency(
    "In number theory, Fermat's Last Theorem (sometimes called Fermat's conjecture, especially in older texts) states that no three positive integers a, b, and c satisfy the equation an + bn = cn for any integer value of n greater than 2. The cases n = 1 and n = 2 have been known since antiquity to have infinitely many solutions.The proposition was first stated as a theorem by Pierre de Fermat around 1637 in the margin of a copy of Arithmetica. Fermat added that he had a proof that was too large to fit in the margin. Although other statements claimed by Fermat without proof were subsequently proven by others and credited as theorems of Fermat (for example, Fermat's theorem on sums of two squares), Fermat's Last Theorem resisted proof, leading to doubt that Fermat ever had a correct proof. Consequently the proposition became known as a conjecture rather than a theorem. After 358 years of effort by mathematicians, the first successful proof was released in 1994 by Andrew Wiles and formally published in 1995. It was described as a 'stunning advance' in the citation for Wiles's Abel Prize award in 2016.[2] It also proved much of the Taniyama–Shimura conjecture, subsequently known as the modularity theorem, and opened up entire new approaches to numerous other problems and mathematically powerful modularity lifting techniques.")
