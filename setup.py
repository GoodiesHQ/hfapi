#!/usr/bin/env python3
from setuptools import setup, find_packages
from hfapi import (
    __author__, __version__,
)

setup(  name="hfapi",
        version=__version__,
        # packages=find_packages(),
        py_modules=["hfapi"],
        install_requires=["requests", "aiohttp", "pydantic"],
        description="HackForums API v2 Integration",
        long_description=open("README.md", "r", encoding="utf-8").read(),
        author=__author__,
        author_email="goodies@protonmail.com",
        url="https://github.com/GoodiesHQ/hfapi/",
        classifiers = [
            "License :: OSI Approved :: GNU Affero General Public License v3",
            "Topic :: Internet :: WWW/HTTP :: Session",
            "Topic :: Security",
        ],
)
