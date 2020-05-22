from PIL import Image, ImageDraw
import os
import random


class MemeEngine:

    def __init__(self, dst_folder):
        self.dst_folder = dst_folder

    def resize_image(self, img, width=500):
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        return img

    def draw_text(self, img, text, author):
        draw = ImageDraw.Draw(img)
        text = text.encode("utf-8")
        text = str(text, "latin-1")
        x = random.randint(0, 200)
        y = random.randint(0, x)
        draw.text((x, y), f'{text} {author}', fill='white')
        return img

    def make_meme(self, img_path, text, author, width=500):
        img = self.resize_image(Image.open(img_path), width)

        img = self.draw_text(img, text, author)

        out_path = os.path.basename(img_path)
        img.save(out_path)
        return out_path
