# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def zip(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count >= 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def unzip(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if txt[i].isdigit():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


text = input("Введите текст для архивации: ")
zip_text = zip(text)
print(f"Текст после архивации: {zip_text}")
unzip_text = unzip(zip_text)
print(f"Текст после разархивации: {unzip_text}")