from PIL import Image, ImageDraw # , ImageFont
import os

class MemeEngine:

    def __init__(self, dst_folder):
        self.dst_folder = dst_folder


    def make_meme(self, img_path, text, author, width=500):
        img = Image.open(img_path)
        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        text = text.encode("utf-8")
        text = str(text, "latin-1")
        draw.text((10, 30), f'{text} {author}', fill='white')
        img.save(img_path)
        out_path = os.path.basename(img_path)
        img.save(out_path)
        return  out_path