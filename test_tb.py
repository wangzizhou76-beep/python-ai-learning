from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")
image_path = "data2/train/bees_image/85112639_6e860b0469.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)

writer.add_image("train", img_array, 1,dataformats="HWC")
for i in range(100):
    writer.add_scalar("y=2x",2*i,i)

writer.close()