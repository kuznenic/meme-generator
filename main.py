from PIL import Image, ImageDraw, ImageFont

print('генератор мемов запущен')

text_type = int(input("Введите 1 если нужно вывести только нижнею натпись или введите 2 если и сверху и снизу надо вывести натпись: "))

if text_type == 1:
    top_text = ""
    bottom_text = input("Введите нижний текст: ")
elif text_type == 2:
    top_text = input('Введите верхний текст: ')
    bottom_text = input("Введите нижний текст: ")

else:
    print("Введина неправелный режим. Перезапустите программу")
    quit()

print(top_text, bottom_text)

memes = ['cat cool.png', 'cat eat.png']
print("Выберете картинку")
for i in range (len(memes)):
    print(i, memes[i])

meme_nembers = int(input("Введите номер картинки: "))