from PIL import Image
img = Image.open("earth.jpg")
# img.show()

r,g,b = img.split() #na ciernobielo
r.save("bwearth.jpg")
r.show()

