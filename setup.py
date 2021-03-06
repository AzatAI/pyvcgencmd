#!/usr/bin/env python3

import os
import sys

from codecs import open

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

about = {}  # create a empty dictionary to store the content of the __version__.py file
# execute the __version__.py file and get the content, save to the dictionary about.
with open(os.path.join(here, "pyvcgencmd", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist")
    os.system("twine upload dist/*")
    os.system("rm -rf dist")
    os.system("rm -rf *.egg-info")
    sys.exit()

if sys.argv[-1] == "publishwin":
    os.system("python3 setup.py sdist")
    os.system("twine upload dist/*")
    os.system("rm dist")
    os.system("rm *.egg-info")
    sys.exit()

requires = ["pydantic", "psutil"]

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name="pyvcgencmd",
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=find_packages(),
    package_data={"": ["LICENSE"]},
    # package_dir={'startpkg': 'src'},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=requires,
    # entry_points='''
    # ''',
    license=about["__license__"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    project_urls={
        "Documentation": "https://github.com/AzatAI/pyvcgencmd",
        "Source": "https://github.com/AzatAI/pyvcgencmd",
    },
)
