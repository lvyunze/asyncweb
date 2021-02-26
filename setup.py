import os
import re
import sys
import pathlib
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='asyncweb',
    description='Asynchronous restful API',
    version="0.0.1",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
         "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Development Status :: 3 - Alpha',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: AsyncIO',
    ],
    author='yunze',
    author_email='17817462542@163.com',
    url='https://github.com/lvyunze/asyncweb',
    packages=['asyncweb'],
    python_requires='>=3.6',
    install_requires=[
        'aiohttp'
    ],
    include_package_data=True,
)
