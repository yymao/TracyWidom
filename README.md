# TracyWidom

[![PyPI version](https://img.shields.io/pypi/v/TracyWidom.svg)](https://pypi.python.org/pypi/TracyWidom)

Providing the Tracy-Widom distribution functions for beta = 1, 2, or 4 in Python.

This package uses the interpolation tables in http://www.cl.cam.ac.uk/~aib29/TWinSplus.pdf
and the asymptotics in http://arxiv.org/abs/1111.2761.

## Installation

```bash
pip install tracywidom
```

## Example

Here's an example of using the `TracyWidom` package.

```python
import numpy as np
from TracyWidom import TracyWidom

x = np.linspace(-10, 10, 101)
tw1 = TracyWidom(beta=1)  # allowed beta values are 1, 2, and 4
pdf = tw1.pdf(x)
cdf = tw1.cdf(x)

r = np.random.rand(1000)
tw1_sample = tw1.cdfinv(r)
```
