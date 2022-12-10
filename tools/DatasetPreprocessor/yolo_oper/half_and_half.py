import os
import random

for path, _, images in os.walk("./images"):
    for filename in images:
        stem, ext = os.path.splitext(filename)

        if random.random() < 0.8:
            os.rename(os.path.join(path, filename),
                      os.path.join('./train/images', filename))
            os.rename(os.path.join('./labels', stem + ".txt"),
                      os.path.join('./train/labels', stem + ".txt"))
        else:
            os.rename(os.path.join(path, filename),
                      os.path.join('./test/images', filename))
            os.rename(os.path.join('./labels', stem + ".txt"),
                      os.path.join('./test/labels', stem + ".txt"))
