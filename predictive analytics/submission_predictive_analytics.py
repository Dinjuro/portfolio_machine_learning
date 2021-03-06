# -*- coding: utf-8 -*-
"""submission_predictive_analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13qPxHxKyvZnkJS81qT3L5tkVbh61EROt

## **PROYEK PERTAMA MACHINE LEARNING TERAPAN**
## **Membuat Model Predictive Analytics**
## **Studi Kasus : Prediksi Harga Mobil Bekas BMW**
#Nama : Addina Dwi Nugroho
#Email : addin27nugroho@gmail.com

###**Tahap 1 : Data Loading**
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

from google.colab import drive

import zipfile, os

#sambung google colab ke google drive
drive.mount('/content/drive')

#ekstrak dataset yang masih berformat zip
local_zip = '/content/drive/My Drive/dataset/100,000 UK Used Car Data set.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp/100,000 UK Used Car Data set')
zip_ref.close()

#definisikan direktori dataset
base_dir = '/tmp/100,000 UK Used Car Data set'
print(os.listdir(base_dir)) #cek list direktori dataset

#baca dataset
df = pd.read_csv("/tmp/100,000 UK Used Car Data set/bmw.csv")

df

"""#####Dokumentasi:
#####- Ada 10781 baris (records) dalam dataset
#####- Terdapat 9 kolom yaitu: model, year, price, transmission, mileage, fuelType, tax, mpg, engineSize

###**Tahap 2 : Deskripsi Variabel**
"""

df.info()

"""#####Dari output terlihat bahwa:

#####-Terdapat 3 kolom dengan tipe object, yaitu: model, transmission, dan fuelType. Kolom ini merupakan categorical features (fitur non-numerik).
#####-Terdapat 5 kolom numerik dengan tipe data float64 dan int64 yaitu: year, mileage, tax, mpg, engineSize.
#####-Terdapat 1 kolom numerik dengan tipe data int64, yaitu: price. Kolom ini merupakan target fitur.
"""

df.describe()

"""###**Tahap 3 : Handling Missing Value**
##### Dari hasil fungsi describe(), nilai minimum tax dan engineSize adalah 0. Patut diduga bahwa ini merupakan data yang tidak valid atau sering disebut missing value. Missing value harus diatasi agar data menjadi valid
"""

x = (df.tax == 0).sum()
y = (df.engineSize == 0).sum()
 
print("Nilai 0 di kolom tax ada: ", x)
print("Nilai 0 di kolom engineSize ada: ", y)

"""##### Karena jumlah sampel missing value cukup sedikit (3%), maka sampel yang memiliki missing value dihapus saja"""

# Drop baris dengan nilai 'tax', dan 'engineSize' = 0
df = df.loc[(df[['tax','engineSize']]!=0).all(axis=1)]
 
# Cek ukuran data untuk memastikan baris sudah di-drop
df.shape

df.describe()

"""###**Tahap 4 : Handling Outliers**
##### deteksi outliers pada fitur numerik dengan teknik visualisasi data (boxplot)
"""

sns.boxplot(x=df['year'])

sns.boxplot(x=df['price'])

sns.boxplot(x=df['mileage'])

sns.boxplot(x=df['tax'])

sns.boxplot(x=df['mpg'])

sns.boxplot(x=df['engineSize'])

#tangani outliers dengan teknik IQR method
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR=Q3-Q1
df=df[~((df<(Q1-1.5*IQR))|(df>(Q3+1.5*IQR))).any(axis=1)]
 
# Cek ukuran dataset setelah kita drop outliers
df.shape

"""###**Tahap 5 : Univariate Analysis**
#####Analisis data dengan teknik Univariate EDA
"""

#Bagi fitur menjadi 2
categorical_features = ['model', 'transmission', 'fuelType']
numerical_features = ['year', 'price', 'mileage', 'tax', 'mpg', 'engineSize']

"""#####Categorical Features"""

feature = categorical_features[0]
count = df[feature].value_counts()
percent = 100*df[feature].value_counts(normalize=True)
df1 = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df1)
count.plot(kind='bar', title=feature)

feature = categorical_features[1]
count = df[feature].value_counts()
percent = 100*df[feature].value_counts(normalize=True)
df1 = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df1)
count.plot(kind='bar', title=feature)

feature = categorical_features[2]
count = df[feature].value_counts()
percent = 100*df[feature].value_counts(normalize=True)
df1 = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df1)
count.plot(kind='bar', title=feature)

"""#####Numerical Features"""

df.hist(bins=50, figsize=(20,15))
plt.show()

"""###**Tahap 6 : Multivariate Analysis**
#####Analisis data dengan teknik Multivariate EDA untuk menunjukkan hubungan antar dua variabel atau lebih

#####Categorical Features
"""

cat_features = df.select_dtypes(include='object').columns.to_list()
 
for col in cat_features:
  sns.catplot(x=col, y="price", kind="bar", dodge=False, height = 4, aspect = 3,  data=df, palette="Set3")
  plt.title("Rata-rata 'price' Relatif terhadap - {}".format(col))

"""#####Numerical Features"""

# mengamati hubungan antar fitur numerik dengan fungsi pairplot()
sns.pairplot(df, diag_kind = 'kde')

plt.figure(figsize=(10, 8))
correlation_matrix = df.corr().round(2)
# annot = True to print the values inside the square
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

"""#####Dari grafik, dapat disimpulkan bahwa fitur ???tax' dan 'engineSize' tidak memiliki korelasi. Sehingga, fitur tersebut dapat di-drop"""

df.drop(['tax','engineSize'], inplace=True, axis=1)
df.head()

"""###**Tahap 7 : Data Preparation**

#####Encoding Fitur Kategori
"""

from sklearn.preprocessing import  OneHotEncoder
df = pd.concat([df, pd.get_dummies(df['model'], prefix='model', drop_first=True)],axis=1)
df = pd.concat([df, pd.get_dummies(df['transmission'], prefix='transmission', drop_first=True)],axis=1)
df = pd.concat([df, pd.get_dummies(df['fuelType'], prefix='fuelType', drop_first=True)],axis=1)
df.drop(['model','transmission','fuelType'], axis=1, inplace=True)
df.head()

"""#####Train Test Split"""

from sklearn.model_selection import train_test_split
 
X = df.drop(["price"],axis =1)
y = df["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)

print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

"""#####Standarisasi """

from sklearn.preprocessing import StandardScaler
 
numerical_features = ['year', 'mileage', 'mpg']
scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()

X_train[numerical_features].describe().round(4)

"""###**Tahap 8 : Model Development**

#####Model Development dengan K-Nearest Neighbor
"""

# Siapkan dataframe untuk analisis model
models = pd.DataFrame(index=['train_mse', 'test_mse'], 
                      columns=['KNN', 'RandomForest', 'Boosting'])

from sklearn.neighbors import KNeighborsRegressor
 
knn = KNeighborsRegressor(n_neighbors=8)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_train)

"""#####Model Development dengan Random Forest"""

# Impor library yang dibutuhkan
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
 
# buat model prediksi
RF = RandomForestRegressor(n_estimators=30, max_depth=16, random_state=55, n_jobs=-1)
RF.fit(X_train, y_train)
 
models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)

"""#####Model Development dengan Boosting Algorithm"""

from sklearn.ensemble import AdaBoostRegressor
 
boosting = AdaBoostRegressor(n_estimators=30, learning_rate=0.05, random_state=55)                             
boosting.fit(X_train, y_train)
models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)

"""###**Tahap 8 : Evaluasi Model**"""

## Scale our numerical features so they have zero mean and a variance of one
X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])

mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting'])
model_dict = {'KNN': knn, 'RF': RF, 'Boosting': boosting}
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3 
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3
 
mse

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""#####Dari grafik, dapat disimpulkan model KNN memberikan nilai eror yang paling kecil. Model inilah yang akan kita pilih sebagai model terbaik untuk melakukan prediksi harga mobil"""

#uji prediksi
prediksi = X_test.iloc[:1].copy()
pred_dict = {'y_true':y_test[:1]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)
 
pd.DataFrame(pred_dict)