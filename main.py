from PIL import Image, ImageDraw, ImageFont
img = Image.open("ot.jpg")
img.show()
sizee = img.size
r = img.crop((30, 35, 1570, 1025))
r.show()
r.save('new.jpg')
#print(sizee)

def z2():
    prazdn = input("Какой праздник хотите?")
    prazdniki = {"новый год": "hny.jpg", "рождество" : "pojd.jpg", "день рождения" : "hb.jpg"}
    for i in prazdniki:
        if i == prazdn:
            img = Image.open(prazdniki[i])
            img.show()

def z3():
    name = input("Кого хотите поздравить?")
    text = name + ", поздравляю! "
    img = Image.open("ot.jpg")
    img = img.crop((30, 35, 1570, 1025))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Roboto-Bold.ttf", 40)
    #draw.text((900, 100), text, font=font, fill='#000000')
    draw.text((800, 700), text, font=font, fill='#C42C2C')
    img.show()
    img.save("new.png")
#z2()
z3()