from PIL import Image,  ImageDraw, ImageFont

print("Генератор мемов запущен!")
top_text = input("Введите верхний текст:")
bottom_text = input("Введите нижний текст:")
print("Список картинок:")
list_mem = ["Кот в очках.png","Кот в ресторане.png"]
for i in range(len(list_mem)):
    print(i,list_mem[i])
image_number = int(input("Введите номер картинки:"))
image=list_mem[image_number]

image = Image.open(list_mem[i])  #открыть файл для редактирования
width, height = image.size


draw =  ImageDraw.Draw(image) #создаем пространство на котором будем рисовать
font = ImageFont.truetype("arial.ttf", size=70) #создаем шрифт

text = draw.textbbox((0,0), top_text, font)
text_width = text[2]


draw.text(((width - text_width)/2,10), top_text, font=font , fill="black")   #координаты и свойства верхнего текста

text = draw.textbbox((0,0), top_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width)/2,height - text_height - 10), bottom_text, font=font , fill="black") #координаты и свойства нижнего текста


image.save("newmeme.jpg")