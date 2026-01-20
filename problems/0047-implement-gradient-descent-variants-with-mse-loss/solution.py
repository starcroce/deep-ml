import numpy as np

def compute_grad_mse_loss(X, y, weights):
    n = len(y)
    y_pred = np.dot(X, weights)
    grad = 2 * np.dot(X.T, (y_pred - y)) / n
    return grad


def batch_gd(X, y, weights, learning_rate, n_epochs):
    for i in range(n_epochs):
        grad = compute_grad_mse_loss(X, y, weights)
        weights -= learning_rate * grad
    return weights


def sgd_gd(X, y, weights, learning_rate, n_epochs):
    for i in range(n_epochs):
        for j in range(len(y)):
            xj, yj = X[j:j+1], y[j:j+1]
            grad = compute_grad_mse_loss(xj, yj, weights)
            weights -= learning_rate * grad
    return weights


def mini_batch_gd(X, y, weights, learning_rate, n_epochs, batch_size):
    for i in range(n_epochs):
        for j in range(0, len(y), batch_size):
            xj, yj = X[j:j+batch_size], y[j:j+batch_size]
            grad = compute_grad_mse_loss(xj, yj, weights)
            weights -= learning_rate * grad
    return weights

def gradient_descent(X, y,