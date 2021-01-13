# TracyWidom

[![Conda Version](https://img.shields.io/conda/vn/conda-forge/tracywidom.svg)](https://anaconda.org/conda-forge/tracywidom)
[![PyPI Version](https://img.shields.io/pypi/v/TracyWidom.svg)](https://pypi.python.org/pypi/TracyWidom)

Providing the Tracy-Widom distribution functions for beta = 1, 2, or 4 in Python.

This package uses the interpolation tables in 

- Bejan, Andrei Iu. (2005), Largest eigenvalues and sample covariance matrices. Tracy–Widom and Painleve II: Computational aspects and realization in S-Plus with applications, M.Sc. dissertation, Department of Statistics, The University of Warwick.

and the asymptotics in

- Borot, Gaëtan and Nadal, Céline (2012), Right tail expansion of Tracy-Widom beta laws, Random Matrices: Theory and Applications Vol. 01, No. 03, 1250006. ([arXiv:1111.2761](https://arxiv.org/abs/1111.2761))

This package is MIT licensed. If you use this package in your work, please consider citing the above publications and listing the URL of this package (`https://github.com/yymao/TracyWidom/`). 


## Installation

You can install `tracywidom` via conda or pip:

```bash
# Install via conda with the conda-forge channel
conda install tracywidom --channel conda-forge

# Or, install via pip
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
