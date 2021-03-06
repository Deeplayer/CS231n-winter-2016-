

import time
from LinearSVM import *
from data_utils import load_CIFAR10

def get_CIFAR10_data(num_training=49000, num_dev=500):
  """
  Load the CIFAR-10 dataset from disk and perform preprocessing to prepare
  it for the linear classifier. These are the same steps as we used for the
  SVM, but condensed to a single function.
  """
  # Load the raw CIFAR-10 data
  cifar10_dir = 'E:/PycharmProjects/ML/CS231n/cifar-10-batches-py'
  X_train, y_train, X_test, y_test = load_CIFAR10(cifar10_dir)
  mask = range(num_training)
  X_train = X_train[mask]
  mask = np.random.choice(num_training, num_dev, replace=False)
  X_dev = X_train[mask]
  y_dev = y_train[mask]

  X_train = np.reshape(X_train, (X_train.shape[0], -1))
  X_dev = np.reshape(X_dev, (X_dev.shape[0], -1))

  mean_image = np.mean(X_train, axis=0)
  X_dev -= mean_image
  X_dev = np.hstack([X_dev, np.ones((X_dev.shape[0], 1))])

  return X_dev, y_dev

X_dev, y_dev = get_CIFAR10_data()

# generate a random SVM weight matrix of small numbers
W = np.random.randn(3073, 10) * 0.0001

tic = time.time()
loss_naive, grad_naive = svm_loss_naive(W, X_dev, y_dev, 0.00001)
toc = time.time()
print 'Naive loss and gradient: computed in %fs' % (toc - tic)  # about 0.198s

tic = time.time()
loss_vectorized, grad_vectorized = svm_loss_vectorized(W, X_dev, y_dev, 0.00001)
toc = time.time()
print 'Vectorized loss and gradient: computed in %fs' % (toc - tic)  # about 0.005s
