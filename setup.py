#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
]

test_requirements = []

setup(
    author="Firstname Lastname",
    author_email="___@example.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="SL forecast modules to be called from Firecrown",
    entry_points={
        "console_scripts": [
            "sl_forecast=sl_forecast.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="sl_forecast",
    name="sl_forecast",
    packages=find_packages(include=["sl_forecast", "sl_forecast.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/LSSTDESC/sl_forecast",
    version="0.0.0",
    zip_safe=False,
)
