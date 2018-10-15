from setuptools import find_packages, setup

import versioneer

with open("./README.rst") as f:
    long_description = f.read()

requirements = [
    # package requirements go here
    "pandas",
    "networkx",
    "geopandas",
    "pysal",
]

setup(
    name="GerryChain",
    description="Use Markov chain Monte Carlo to analyze districting plans and gerrymanders",
    author="Metric Geometry and Gerrymandering Group",
    author_email="gerrymandr@gmail.com",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/mggg/GerryChain",
    packages=find_packages(exclude=("tests",)),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    entry_points={"console_scripts": ["gerrychain=gerrychain.__main__:main"]},
    install_requires=requirements,
    keywords="GerryChain",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
    ],
)
