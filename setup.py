#  ____  _ _        _      ____  _  _     ____  _____ ____ _____
# | __ )(_) |_ _ __(_)_  _|___ \| || |   |  _ \| ____/ ___|_   _|
# |  _ \| | __| "__| \ \/ / __) | || |_  | |_) |  _| \___ \ | |
# | |_) | | |_| |  | |>  < / __/|__   _| |  _ <| |___ ___) || |
# |____/|_|\__|_|  |_/_/\_\_____|  |_|   |_| \_\_____|____/ |_|

from distutils.core import setup
from os import path
from setuptools import find_packages

directory = path.abspath(path.dirname(__file__))

setup(
    name="bitrix24-rest",
    version="2.0.3",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
    ],
    extras_require={
        "dev": [
            "flake8",
            "safety",
            "pydocstyle",
            "black",
            "isort",
            "pytest",
            "pytest-cov",
            "pytest-asyncio",
            "aioresponses",
            "pytest-aiohttp"
        ],
    },
    url="https://github.com/akopdev/bitrix24-python-rest",
    license="MIT",
    author="Akop Kesheshyan",
    author_email="hello@akop.dev",
    description="Easy way to communicate with bitrix24 portal over REST without OAuth",
    long_description=open(path.join(directory, "README.md"), encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="bitrix24 api rest",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
    ],
)
