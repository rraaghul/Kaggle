# Digit Recognizer using MNIST dataset


## Dataset

Source: [MNIST_digit](https://www.kaggle.com/c/digit-recognizer/data)

train.csv: 42,000 images with 784 columns representing pixels from 28*28 image

test.csv:  28,000 images with 784 columns representing pixels from 28*28 image

classes: 10 classes (0-9)

output.csv: Predicted output file with image_id and the label

## Code

The CNN architecure is used for training the data. Model is trained with Adam optimizer and batch size 100 and 10 epochs.
  
Model Architecture:
  1. Convolution layer with same padding and 5*5 kernel
  2. Maxpooling layer with 2*2 kernel
  3. Convolution layer with same padding and 5*5 kernel
  4. Maxpooling layer with 2*2 kernel
  5. Flatten
  6. Dense with 1024 nodes
  7. Dropout
  8. softmax with 10 nodes

## Results

Accuracy : 98.6%
