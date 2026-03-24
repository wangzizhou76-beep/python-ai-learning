from PIL import Image
from torchvision import transforms

#python的用法 ->tensor数据类型
#通过 transforms.ToTensor去看两个问题
#1.transforms该如何使用 (python)
#2.为什么我们需要Tensor数据类型

# 绝对路径 C:\Users\wangzizhou\pytorch-learn\dataset\train\ants_image\0013035.jpg
# 相对路径 dataset/train/ants_image/0013035.jpg
img_path =  "dataset/train/ants_image/0013035.jpg"
img = Image.open(img_path)

tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)

print(tensor_img)