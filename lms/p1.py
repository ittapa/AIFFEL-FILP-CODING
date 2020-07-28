'''
1. data import    train
 - 정규화
 - reshape
2. model layer set
   - hyper param
3. 학습 train
   - compile
   - fit
4. 성능 및 정확도 확인    test
   - test data improt
   - evaluate
'''


import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os, glob

## data import function
def load_data(img_path):
    # 가위 : 0, 바위 : 1, 보 : 2
    number_of_data = 300  # 가위바위보 이미지 개수 총합에 주의하세요.
    img_size = 28
    color = 3
    # 이미지 데이터와 라벨(가위 : 0, 바위 : 1, 보 : 2) 데이터를 담을 행렬(matrix) 영역을 생성합니다.
    imgs = np.zeros(number_of_data * img_size * img_size * color, dtype=np.int32).reshape(number_of_data, img_size,
                                                                                          img_size, color)
    labels = np.zeros(number_of_data, dtype=np.int32)

    idx = 0
    for file in glob.iglob(img_path + '/scissor/*.jpg'):
        img = np.array(Image.open(file), dtype=np.int32)
        imgs[idx, :, :, :] = img  # 데이터 영역에 이미지 행렬을 복사
        labels[idx] = 0  # 가위 : 0
        idx = idx + 1

    for file in glob.iglob(img_path + '/rock/*.jpg'):
        img = np.array(Image.open(file), dtype=np.int32)
        imgs[idx, :, :, :] = img  # 데이터 영역에 이미지 행렬을 복사
        labels[idx] = 1  # 바위 : 1
        idx = idx + 1

    for file in glob.iglob(img_path + '/paper/*.jpg'):
        img = np.array(Image.open(file), dtype=np.int32)
        imgs[idx, :, :, :] = img  # 데이터 영역에 이미지 행렬을 복사
        labels[idx] = 2  # 보 : 2
        idx = idx + 1

    print("학습데이터(x_train)의 이미지 개수는", idx, "입니다.")
    return imgs, labels
## end data import function


##1. train data import , 정규화
image_dir_path = os.getenv("HOME") + "/aiffel/rock_scissor_paper"
x_train, y_train = load_data(image_dir_path)
x_train_norm = x_train/255.0   # 입력은 0~1 사이의 값으로 정규화
#

# 2. model hyperpram, layer set
n_channel_1=48
n_channel_2=42
n_dense=36
n_train_epoch=10

model=keras.models.Sequential()
model.add(keras.layers.Conv2D(n_channel_1, (3,3), activation='relu', input_shape=(28,28,3)))
model.add(keras.layers.MaxPool2D(2,2))
model.add(keras.layers.Conv2D(n_channel_2, (3,3), activation='relu'))
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(n_dense, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))

print('Model에 추가된 Layer 개수: ', len(model.layers))

model.summary()



# 3 학습 train
model.compile(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])

print(x_train_norm.shape)
print(y_train.shape)
model.fit(x_train_norm, y_train, epochs=10)
#end 학습 완료


#3-2 test 데이터 import 및 정규화
image_dir_test_path = os.getenv("HOME") + "/aiffel/test_rcp" #test data 폴더를 따로 생성함.
x_test, y_test = load_data(image_dir_test_path)
x_test_norm = x_test/255.0   # 입력은 0~1 사이의 값으로 정규화


#test data 를 통한 검
test_loss, test_accuracy = model.evaluate(x_test_reshaped,y_test, verbose=2)
print("test_loss: {} ".format(test_loss))
print("test_accuracy: {}".format(test_accuracy))

