# import 하세요.
from PIL import Image, ImageFilter


def image_resize(image, height):  # 이미지 객체 , 세로 사이즈

    if height == 300:  # 300 이면  800 300
        return image.resize((800, 300))
    else:  # 아니면 800 600
        return image.resize((800, 600))


def image_rotate(image):  # 180 도 회전 시켜서 반환
    return image.rotate(180)


def image_change_bw(image):
    return image.convert('L')