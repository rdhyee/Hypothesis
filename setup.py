#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='Hypothes_is',
    version='0.0.1',
    description="Python wrapper for the hypothes.is web API",
    long_description="Python wrapper for the hypothes.is web API",
    author="Jon Udell",
    author_email='judell@hypothes.is',
    url='https://github.com/judell/Hypothesis',
    packages=[
        'Hypothes_is',
    ],
    package_dir={'Hypothes_is':
                 'Hypothes_is'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='Hypothesis',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
