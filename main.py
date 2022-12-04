from watermark import File, Watermark, apply_watermark, Position
from PIL import Image
import os
r_image = Image.open('watermark.png')
r_image.thumbnail((300, 300))
r_image.save('new.png')




photo = File('jadon.jpeg')
watermark = Watermark(File("new.png"), pos=Position.bottom_right)
apply_watermark(photo, watermark)

# video = File("jh.mp4")
# watermark = Watermark(File('new.png'), pos=Position.bottom_right)

# apply_watermark(video, watermark)

# Bulk watermark
# def bulkWaterMark(srcFolder: str) -> str:
#     images = os.listdir(srcFolder)
#     for img in images:
#         watermark = Watermark(File('watermark.png'), pos=Position.bottom_right)
#         print(apply_watermark(File(img), watermark))
        
# bulkWaterMark('images')
# /home/bontusmayor/Documents/watermark/watermarked
