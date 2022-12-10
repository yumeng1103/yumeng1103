import os
import random
import cv2

for path, _, images in os.walk("./images"):
    for filename in images:
        stem, ext = os.path.splitext(filename)
        img = cv2.imread(os.path.join(path, filename))
        start = random.randint(0, 1280 - 720)
        end = start + 720
        square = img[0:720, start:720 + start]
        square = cv2.resize(square,
                            dsize=(640, 640),
                            interpolation=cv2.INTER_AREA)
        new_txt = ""
        with open(os.path.join('./labels', stem + ".txt"), 'r') as f:
            for line in f.readlines():
                line_data = line.split(" ")
                index, x, y = line_data

                max_l = 60
                max_r = 60
                max_t = 120
                max_b = 30

                y -= 22

                w = random.randint(80, max_l + max_r)
                h = random.randint(100, max_t + max_b)

                if x + max_r < start or x - max_l > end:
                    continue
                if x - w / 2.0 < start:
                    r = x + w / 2.0
                    if r < start:
                        continue
                    x = (r - start) / 2.0 + start
                    w = r - start
                if x + w / 2.0 > end:
                    l = x - w / 2.0
                    if l > end:
                        continue
                    x = (end - l) / 2.0 + l
                    w = end - l

                # cv2.rectangle(img, (int(x - w / 2.0), int(y - h / 2.0)),
                #              (int(x + w / 2.0), int(y + h / 2.0)), (255, 0, 0), 2)
                # cv2.rectangle(img, (start, 0),
                #              (end, 720), (0, 0, 255), 2)

                # cv2.imshow("draw", img)
                # cv2.waitKey()

                x -= start
                x /= 720.0
                y /= 720.0
                w /= 720.0
                h /= 720.0

                new_txt += f"{index} {x} {y} {w} {h}\n"

        with open(os.path.join('./labels', stem + ".txt"), 'w') as f:
            f.write(new_txt)

        cv2.imwrite(os.path.join(path, filename), square)
