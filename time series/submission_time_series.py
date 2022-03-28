# -*- coding: utf-8 -*-
"""Copy of submission_time_series.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15BjuAMY61WnDwy7mXUMVLXTJZpyNvlTD

## **PROYEK KEDUA BELAJAR PENGEMBANGAN MACHINE LEARNING**
## **Membuat Model Machine Learning dengan Data Time Series**
#Nama : Addina Dwi Nugroho
#Email : addin27nugroho@gmail.com
"""

#sambung google colab ke google drive
from google.colab import drive
drive.mount('/content/drive')

#import library yang dibutuhkan
import numpy as np
import pandas as pd
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import tensorflow as tf

#baca dataset
df = pd.read_csv("/content/drive/My Drive/dataset/Weather in Szeged 2006-2016.csv")

#preprocessing data
df = df[["Formatted Date","Temperature (C)"]]

df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)

df = df.set_index('Formatted Date')

df = df.resample('D').mean()

df = df.reset_index()

df.info()

df.head()

df.isnull().sum()

#plot dataset
dates = df['Formatted Date'].values
temp  = df['Temperature (C)'].values
 
 
plt.figure(figsize=(15,5))
plt.plot(dates, temp)
plt.title('Temperature average',
          fontsize=20);

#bagi dataset menjadi 80% data training dan 20% data validation
df_train = df[:3217]
dates_train = df_train['Formatted Date']
temp_train = df_train['Temperature (C)']
df_validation = df[3217:]
dates_validation = df_validation['Formatted Date']
temp_validation = df_validation['Temperature (C)']
df_train.tail(), df_validation.head()

def windowed_dataset(series, window_size, batch_size, shuffle_buffer):
    series = tf.expand_dims(series, axis=-1)
    ds = tf.data.Dataset.from_tensor_slices(series)
    ds = ds.window(window_size + 1, shift=1, drop_remainder=True)
    ds = ds.flat_map(lambda w: w.batch(window_size + 1))
    ds = ds.shuffle(shuffle_buffer)
    ds = ds.map(lambda w: (w[:-1], w[-1:]))
    return ds.batch(batch_size).prefetch(1)

#buat model
train_set = windowed_dataset(temp_train, window_size=60, batch_size=100, shuffle_buffer=1000)
validation_set = windowed_dataset(temp_validation, window_size=60, batch_size=100, shuffle_buffer=1000)
model = tf.keras.models.Sequential([
  tf.keras.layers.LSTM(60, return_sequences=True),
  tf.keras.layers.LSTM(60),
  tf.keras.layers.Dense(30, activation="relu"),
  tf.keras.layers.Dense(10, activation="relu"),
  tf.keras.layers.Dense(1),
])

optimizer = tf.keras.optimizers.SGD(lr=1.0000e-04, momentum=0.9)
model.compile(loss=tf.keras.losses.Huber(),
              optimizer=optimizer,
              metrics=["mae"])

#Gunakan Callback agar proses otomatis berhenti ketika mae model memenuhi kriteria (MAE < 10% skala data)
#skala data = 50, 10% dari skala data berarti 5
class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('mae' and 'val_mae')<5):
      print("\nMAE MODEL KURANG DARI 10%, PELATIHAN MODEL DIHENTIKAN.")
      self.model.stop_training = True

callbacks = myCallback()

#latih model
history = model.fit(train_set,  validation_data=validation_set, epochs=100, callbacks=[callbacks])

#visualisasi hasil pelatihan model

mae = history.history['mae'] #mae training
val_mae = history.history['val_mae'] #mae validation
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(mae)) #jumlah epoch

plt.figure(figsize=(15,5))
plt.plot(epochs, mae, marker='o', color='blue', label='MAE Training')
plt.plot(epochs, val_mae, marker='o', color='red', label='MAE Validasi')
plt.legend()
plt.title('MAE Pelatihan Model', pad=30, fontsize=30)
plt.xlabel('Epoch', fontsize=20)
plt.ylabel('Nilai MAE', fontsize=20)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.xticks([0,5,10,15,20])
plt.ylim(ymin=0)
plt.show()

plt.figure(figsize=(15,5))
plt.plot(epochs, loss, marker='o', color='blue', label='Loss Training')
plt.plot(epochs, val_loss, marker='o', color='red', label='Loss Validasi')
plt.legend()
plt.title('Loss Pelatihan Model', pad=30, fontsize=30)
plt.xlabel('Epoch', fontsize=20)
plt.ylabel('Nilai Loss', fontsize=20)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.xticks([0,5,10,15,20])
plt.ylim(ymin=0)
plt.show()