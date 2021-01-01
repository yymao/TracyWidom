#!/usr/bin/env python
"""
TracyWidom.py
Generate Tracy-Widom distribution functions
Author: Yao-Yuan Mao (yymao)
Project website: https://github.com/yymao/TracyWidom

The MIT License (MIT)
Copyright (c) 2013-2021 Yao-Yuan Mao
http://opensource.org/licenses/MIT
"""

import os
from setuptools import setup


def _get_version(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path)) as f:
        for line in f:
            if line.startswith("__version__"):
                return line.partition('=')[2].strip().strip(" '\"")
    raise ValueError('__version__ not define!')


__version__ = _get_version("TracyWidom.py")


setup(
    name="TracyWidom",
    version=__version__,
    description='Generate Tracy-Widom distribution functions',
    url='https://github.com/yymao/TracyWidom',
    download_url='https://github.com/yymao/TracyWidom/archive/v{}.tar.gz'.format(__version__),
    author='Yao-Yuan Mao',
    author_email='yymao.astro@gmail.com',
    maintainer='Yao-Yuan Mao',
    maintainer_email='yymao.astro@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    keywords='Tracy-Widom',
    py_modules=["TracyWidom"],
    install_requires=['numpy>=1.7.0', 'scipy>=0.13.0'],
)
