from PIL import Image, ImageEnhance

alpha = 0.8

# Conversion de la photo en NB
camera_source = Image.open("testface.jpg")
scan_hover = Image.open("hover_1.jpg")
camera_source= vintage.vintage_colors(camera_source)
camera_source = ImageEnhance.Contrast(camera_source).enhance(1.5)
camera_source = ImageEnhance.Brightness(camera_source).enhance(1.5)

#out = Image.blend(camera_source,scan_hover,alpha)
#out = out.convert('1')
out.show()
out.save('testfaceNB.jpg')
