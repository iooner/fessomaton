from PIL import Image, ImageEnhance
import time, datetime, random
outname = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S'))

alpha = 0.7
hover_list = ['hover_1.jpg']
i = random.randint(0, len(hover_list) - 1)  
hover_file = hover_list[i] 


camera_source = Image.open("testface.jpg")
watermark = Image.open("watermark.png")
source_width, source_height = camera_source.size
watermark_width, watermark_height = watermark.size

scan_hover = Image.open(hover_file)
camera_source = ImageEnhance.Contrast(camera_source).enhance(1.5)
camera_source = ImageEnhance.Brightness(camera_source).enhance(1.5)


out = Image.blend(camera_source,scan_hover,alpha)
out = out.convert('1')
out.paste(watermark, (source_width - watermark_width - 25, source_height - watermark_height - 25))
out.show()
#imprimer ici avec cups
out.save('allfiles/%s.jpg' % outname, format="JPEG")
out.save('batch/%s.jpg' % outname, format="JPEG")