from setuptools import setup, find_packages

setup(
    name="xtherm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "seaborn",
        "h5py",
        "pandas",
        "numba"
    ]
) 