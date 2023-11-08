import tesserocr

from PIL import Image

# 1. jpg to 文字
# image = Image.open('C:/Users/qq115/Pictures/code1.jpg')
# print(tesserocr.image_to_text(image))

# 2. 文件 to 文字
# print(tesserocr.file_to_text('C:/Users/qq115/Pictures/code1.jpg'))

# 3.
image = Image.open('C:/Users/op.117655/Pictures/code.jpg')
# 将图片转化为灰度图像
# image = image.convert('L')
# image.show()
# 传入1即可将图片进行二值化处理
# image = image.convert('1')
# image.show()
# 上面的方法采用的是默认阔值127,不过我们不能直接转化原因，要将原图先转为灰度图像，然后再指定二值化阔值
image = image.convert('L')
threshold = 128
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
image.show()
print(tesserocr.image_to_text(image))

