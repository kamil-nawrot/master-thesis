import os
from PIL import Image


def resize_dataset(newsize):
    for root, dirs, files in os.walk("./data"):
        for file in files:
            im = Image.open(os.path.join(root, file))
            im = im.resize(newsize)
            im.save("./data/" + file, "PNG")
            print(file, ": ", im.size)


def rename_dataset():
    for root, dirs, files in os.walk("./data"):
        i = 1
        for file in files:
            print(file)
            if "normal" in root:
                print(root + "/normal_" + str(i).zfill(5) + ".png")
                os.rename(os.path.join(root, file), os.path.join(root, "normal_" + str(i).zfill(5) + ".png"))
                i = i + 1
            elif "covid_19" in root:
                print(root + "/covid_" + str(i).zfill(5) + ".png")
                os.rename(os.path.join(root, file), os.path.join(root, "covid_" + str(i).zfill(5) + ".png"))
                i = i + 1
            elif "lungs_opacity" in root:
                print(root + "/lungs_opacity_" + str(i).zfill(5) + ".png")
                os.rename(os.path.join(root, file), os.path.join(root, "lungs_opacity_" + str(i).zfill(5) + ".png"))
                i = i + 1
            elif "pneumonia" in root:
                if "bacteria" in root:
                    print(root + "/pneumonia_bacteria_" + str(i).zfill(5) + ".png")
                    os.rename(os.path.join(root, file),
                              os.path.join(root, "pneumonia_bacteria_" + str(i).zfill(5) + ".png"))
                else:
                    print(root + "/pneumonia_virus_" + str(i).zfill(5) + ".png")
                    os.rename(os.path.join(root, file),
                              os.path.join(root, "pneumonia_virus_" + str(i).zfill(5) + ".png"))
                i = i + 1