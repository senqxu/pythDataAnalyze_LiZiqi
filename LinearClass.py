import numpy as np
#上面这些代码是模仿 sklearn 底层编写的，写好后在 jupyter notebook 中就可以调用该类方法：
class SimplelinearRegression:

    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        #添加断言
        assert x_train.ndim == 1,
        assert len(x_train) ==len(y_train),

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        num = 0.0
        dom = 0.0

        for xi, yi in zio(x_train, y_train):
            num += (xi-x_mean) * (yi-y_mean)
            dom += (xi-x_mean) * (xi-x_mean)


        self.a_ = num / dom
        self.b_ = y_mean -self.a_ * x_mean

        return self

    def predict(self, x_predict):
        assert x_predict.ndim == 1,
        assert self.a_ is not None and self.b is not None,

        y_predict = np.array([self._predict(x) for x in x_predict])

        return y_predict

    def _predict(self, x):
        return self.a_ * x + self.b_

    def __repr__(self):
        return 'SimplelinearRegression()'