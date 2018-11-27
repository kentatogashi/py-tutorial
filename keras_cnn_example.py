# datasets: https://www.kaggle.com/tongpython/cat-and-dog

import numpy as np
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import load_img, img_to_array
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Dropout, Flatten
from keras.optimizers import RMSprop
from keras.callbacks import ReduceLROnPlateau

def convert_to_img_arr(path):
    data = []
    for i in os.listdir(path):
        if i == '_DS_Store': continue
        filepath = path + '/' + i
        img = load_img(filepath, grayscale=True, target_size=(200, 200))
        img_arr = img_to_array(img)
        data.append(img_arr/255.)
    return data

cat_path = '../input/training_set/training_set/cats'
cat_data = convert_to_img_arr(cat_path)
cat_data np.array(cat_data)
dog_path = '../input/training_set/training_set/dogs'
dog_data = convert_to_img_arr(dog_path)
dog_data = np.array(dog_data)

train_data = np.r_[cat_data, dog_data]
cat_label = np.zeros(4000).reshape(-1, 1)
dog_label = np.ones(4005).reshape(-1, 1)
train_label = np.r_[cat_label, dog_label]

X_train, X_val, y_train, y_val = train_test_split(train_data, train_label, test_size=0.2)

model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(5,5), padding='Same', input_shape=(200, 200, 1), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Conv2D(filters=32, kernel_size=(5,5), padding='Same', input_shape=(200, 200, 1), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='binary_crossentropy'))

optimizer = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

learning_rate_reduction = ReduceLROnPlateau(monitor='val_acc', patience=3, verbose=2, factor=0.5, min_lr=0.00001)
epochs = 10
batch_size 50

history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=2, callbacks=[learning_rate_reduction])
score = model.evaluate(X_train, y_train)
print(f'{model.metrics_names[0]}: {score[0]}, {model.metrics_names[1]}: {score[1]}')
