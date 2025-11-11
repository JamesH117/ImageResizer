from PIL import Image
import os, sys

cwd = os.getcwd()
items_inside_dir = [os.path.join(cwd, f) for f in os.listdir(cwd) if (f.endswith(".jpg") or f.endswith(".png") or f.endswith(".webp"))]
target_width = 1280

def resize():
    for item in items_inside_dir:
        if os.path.isfile(item):
            im = Image.open(item).convert('RGB')
            f, e = os.path.splitext(item)

            # target_width * original_height / original_width
            new_height = int(target_width * im.size[1] / float(im.size[0]))
            imResize = im.resize((target_width,new_height), Image.LANCZOS)

            imResize.save(f + '_alt.jpg', 'JPEG', quality=95)
            os.remove(item)
resize()

