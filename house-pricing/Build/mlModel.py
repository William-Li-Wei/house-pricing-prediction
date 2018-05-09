import numpy as np


def init():
    # TODO: load data from DB
    data = np.array([
        [ 245 , 1400 ],
        [ 312 , 1600 ],
        [ 279 , 1700 ],
        [ 308 , 1875 ],
        [ 199 , 1100 ],
        [ 219 , 1550 ],
        [ 405 , 2350 ],
        [ 324 , 2450 ],
        [ 319 , 1425 ],
        [ 255 , 1700 ]
    ])
    X = data[:, 1:]         # shape (m, 1)
    m = X.shape[0]
    n = X.shape[1]
    Y = data[:, :1]         # shape (m, 1)

    # init params and learning rate
    W = np.zeros((n, 1))    # shape (n, 1)
    b = 0
    alpha = 0.01
    return (X, Y, W, b, alpha)


def meanNorm(X):
    mean = np.mean(X, axis = 0)
    max = np.amax(X, axis = 0)
    min = np.amin(X, axis = 0)
    maxDifference = max - min
    normedX = (X - mean) / maxDifference

    # return normalized training set, mean and maxDifference
    return (normedX, mean, maxDifference)


def getCost(X, Y, W, b):
    m = X.shape[0]
    H = np.dot(X, W) + b
    J = np.sum((Y - H) ** 2) / (2 * m)
    return J


def getGradient(X, Y, W, b):
    m = X.shape[0]
    H = np.dot(X, W) + b
    D = H - Y
    return (np.dot(np.transpose(X), D) / m, sum(H - Y) / m)


def train(X, Y, W, b, alpha):

    for i in range(50000):
        J = getCost(X, Y, W, b)

        # gradient decent
        W = W - alpha * getGradient(X, Y, W, b)[0]
        b = b - alpha * getGradient(X, Y, W, b)[1]

        if(i%1000 == 0):
            print('cost', J)

    return (W, b)


def predict(X, W, b, mean, maxDifference):
    multi_inputs = False
    if isinstance(X, list):
        multi_inputs = True
        X = np.resize(X, (len(X), 1))
    else:
        X = np.array([[X]])

    X = (X - mean) / maxDifference
    H = np.dot(X, W) + b

    if multi_inputs:
        output = H.flaten()
    else:
        output = H[0]

    return output



def getTrainedWeights():
    X, Y, W, b, alpha = init()      # init params
    X, mean, maxDifference = meanNorm(X)   # feature normalization
    W, b = train(X, Y, W, b, alpha) # train the model
    return (W, b, mean, maxDifference)


#prediction = predict(np.array([[1600]]), W, b, mean, maxDifference)
#print('prediction', prediction)
