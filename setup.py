#!/usr/bin/env python

import re
from setuptools import find_packages, setup

VERSION_FILE = "tweepy_mastodon/__init__.py"
with open(VERSION_FILE) as version_file:
    match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                      version_file.read(), re.MULTILINE)

if match:
    version = match.group(1)
else:
    raise RuntimeError(f"Unable to find version string in {VERSION_FILE}.")

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name="tweepy-mastodon",
    version=version,
    description="Mastodon library with Tweepy interface for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="TAKAHASHI Shuuji",
    author_email="shuuji3@gmail.com",
    url="https://github.com/shuuji3/tweepy-mastodon",
    project_urls={
        "Documentation": "https://github.com/shuuji3/tweepy-mastodon",
        "Issue Tracker": "https://github.com/shuuji3/tweepy-mastodon/issues",
        "Source Code": "https://github.com/shuuji3/tweepy-mastodon",
    },
    download_url="https://pypi.org/project/tweepy-mastodon/",
    packages=find_packages(),
    install_requires=[
        "Mastodon.py>=1.8.0,<2",
        "tweepy>=4.12.1,<5",
    ],
    extras_require={
        "async": [
            "aiohttp>=3.7.3,<4",
            "async-lru>=1.0.3,<2",
        ],
        "docs": [
            "myst-parser==0.15.2",
            "readthedocs-sphinx-search==0.1.1",
            "sphinx==4.2.0",
            "sphinx-hoverxref==0.7b1",
            "sphinx-tabs==3.2.0",
            "sphinx_rtd_theme==1.0.0",
        ],
        "dev": [
            "coverage>=4.4.2",
            "coveralls>=2.1.0",
            "tox>=3.21.0",
            "pytest>=7.2.1",
            "pytest_mock>=3.10.0"
        ],
        "socks": ["requests[socks]>=2.27.0,<3"],
        "test": ["vcrpy>=1.10.3"],
    },
    test_suite="tests",
    keywords="mastodon library",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
    zip_safe=True,
)
