import pandas as pd
import os
import shutil

df = pd.read_csv('labels.csv')
labels_list = list(set(df['breed'].tolist()))
src = 'train/{0}.jpg'
des = 'train_images/{0}/{1}.jpg'
for label in labels_list:
    if not os.path.exists('train_images/' + label):
        os.mkdir('train_images/' + label)
for index, row in df.iterrows():
    shutil.move(src.format(row['id']), des.format(row['breed'], row['id']))
