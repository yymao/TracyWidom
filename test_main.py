import numpy as np
from TracyWidom import TracyWidom


def test_main():
    x = np.linspace(-10, 10, 101)
    y = np.linspace(0, 1, 101)

    for beta in (1, 2, 4):
        tw = TracyWidom(beta)
        pdf = tw.pdf(x)
        cdf = tw.cdf(x)
        cdfinv = tw.cdfinv(y)


if __name__ == '__main__':
    test_main()
