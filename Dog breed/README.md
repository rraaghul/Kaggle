# Dog Breed Identification

## Dataset
Source: [Dog Breed Identification](https://www.kaggle.com/c/dog-breed-identification/data).

labels.csv: File contains id of image and label of the image.

train.zip: training images in zipped format (10,342 images).

test.zip: test images in zipped format (10,342 images).

classes: 120

submission.csv: test images and its prediction probabilities of all classes (10,342 rows and 121 columns which has id and 120 classes).

## Code

This project contains clone of the [TensorFlow for poets 2](https://github.com/googlecodelabs/tensorflow-for-poets-2.git) code.
The Transfer learning is done using inception V3 network for identification of dog breed.

![inception V3 network](https://github.com/rraaghul/Kaggle/blob/master/Dog%20breed/Inception.png)


1. Move the images from train - *python images_move.py*
2. Train the network - *python scripts/retrain.py --output_graph=tf_files/dog_breed_class.pb --output_label=tf_files/dog_breed.txt --image_dir=tf_files/train_images --how_many_training_steps=5000 --train_batch_size=64 --bottleneck_dir='tf_files/bottlenecks' --learning_rate=0.001 --model_dir=tf_files/models*
3. Move the test images into **tf_files/test**
4. Prediction - *python scripts/label_image.py --graph=tf_files/dog_breed_class.pb --labels=tf_files/dog_breed.txt --image=tf_files/test/*

## Results
The Log loss was used as metrics for evaluation.

Log Loss -2.23419
