import numpy as np
from random import shuffle

def svm_loss_naive(W, X, y, reg):
  """
  Structured SVM loss function, naive implementation (with loops).

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # initialize the gradient as zero
  dW = np.zeros(np.shape(W))
  
  # compute the loss and the gradient
  num_classes = W.shape[1]
  num_train = X.shape[0]
  num_features = X.shape[1]
  
  loss = 0.0
    
  dW = dW.T
    
  for i in range(num_train):
    scores = np.dot(X[i], W)
    correct_class_score = scores[y[i]]
    diff_cnt = 0
    for j in range(num_classes):
      if j == y[i]:
        continue
      margin = scores[j] - correct_class_score + 1 # note delta = 1
      if margin >= 0:
        diff_cnt += 1
        loss += margin
        dW[j] += X[i]
    dW[y[i]] -= X[i] * diff_cnt

  # Right now the loss is a sum over all training examples, but we want it
  # to be an average instead so we divide by num_train.
  
  loss = loss / num_train
  dW = dW.T / num_train
  # Add regularization to the loss.
  loss += 0.5 * reg * np.sum(W * W)
  dW += 1 * reg * W

  #############################################################################
  # TODO:                                                                     #
  # Compute the gradient of the loss function and store it dW.                #
  # Rather that first computing the loss and then computing the derivative,   #
  # it may be simpler to compute the derivative at the same time that the     #
  # loss is being computed. As a result you may need to modify some of the    #
  # code above to compute the gradient.                                       #
  #############################################################################


  return loss, dW


def svm_loss_vectorized(W, X, y, reg):
  """
  Structured SVM loss function, vectorized implementation.

  Inputs and outputs are the same as svm_loss_naive.
  """
  loss = 0.0
  dW = np.zeros(W.shape) # initialize the gradient as zero

  num_train = np.shape(y)[0]
  #############################################################################
  # TODO:                                                                     #
  # Implement a vectorized version of the structured SVM loss, storing the    #
  # result in loss.                                                           #
  #############################################################################
  pass
  scores = X.dot(W)
  correct_scores = scores[np.arange(num_train), y]
  margin = np.maximum(scores-correct_scores[:,np.newaxis]+1, 0)
  margin[np.arange(num_train), y] = 0
  loss = np.sum(margin) / num_train
  loss += 0.5 * reg * np.sum(W*W)
  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################


  #############################################################################
  # TODO:                                                                     #
  # Implement a vectorized version of the gradient for the structured SVM     #
  # loss, storing the result in dW.                                           #
  #                                                                           #
  # Hint: Instead of computing the gradient from scratch, it may be easier    #
  # to reuse some of the intermediate values that you used to compute the     #
  # loss.                                                                     #
  #############################################################################
  X_mask = np.zeros(np.shape(margin))
  X_mask[margin>0] = 1
  incorrect_num = np.sum(X_mask, axis=1)
  X_mask[np.arange(num_train), y] = -incorrect_num
  dW = X.T.dot(X_mask)
  pass
         
  dW /= num_train
  dW += reg * np.sum(W)
  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################

  return loss, dW
