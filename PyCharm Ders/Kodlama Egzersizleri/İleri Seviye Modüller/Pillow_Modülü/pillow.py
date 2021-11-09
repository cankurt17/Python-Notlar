


from  PIL import Image,ImageFilter

image =Image.open("kuş.jpg")

# image.show()
# image.save("kuş2.jpg")
# image.rotate(180).save("kuş3.jpg")
#image.convert(mode = "L").save("kuş4.jpg")

"""
degistir=(960,600)
image.thumbnail(degistir)
image.save("kuş5.jpg")
"""
#image.filter(ImageFilter.GaussianBlur(10)).save("kuş8.jpg")

kırp =(340,0,950,600)
image2=Image.open("atatürk.jpg")
image2.crop(kırp).save("atatürk2.jpg")














