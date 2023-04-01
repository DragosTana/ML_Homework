
import numpy as np
import models.kernel as ker
import misc as misc


class kernel_regression:
    
    def __init__(self, feature, values, type = "nadaraya_watson", kernel = "gaussian", bandwidth = 1.0):
        """
        feature: list of features
        values: list of values
        type: "nadaraya_watson" or "priestley_chao"
        kernel: "gaussian", "uniform", "triangular", "epanechnikov", "cosine"
        bandwidth: float
        
        Naive implementation of kernel regression.
        """
        self.kernel = ker.kernel(kernel)
        self.feature = feature
        self.values = values
        self. bandwidth = bandwidth
        self.type = type
    
    def __call__(self, x):
        
        if self.type == "nadaraya_watson":
            
            #TODO: optimize
            tmp = [x - v for v in self.feature]
            ker_values = [(1/self.bandwidth)*self.kernel(v/self.bandwidth) for v in tmp]

            ker_values = np.array(ker_values)
            values = np.array(self.values)

            num = np.dot(ker_values.T, values)
            denom = np.sum(ker_values)

            return num/denom
        
        if self.type == "priestley_chao":
            pass
    
    def predict(self, x_test, y_test):
        pred = []
        for x in x_test:
            pred.self.__call__(x)
        mse = misc.MSE(y_test, pred)
        return pred, mse