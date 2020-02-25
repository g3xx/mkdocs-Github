from setuptools import setup, find_packages
from distutils.core import Command

VERSION = '0.0.4'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mkdocs-github",
    version=VERSION,
    url='https://github.com/g3xx/mkdocs-Github',
    license='MIT',
    description='simple theme github for Mkdocs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='g3xx',
    author_email='cc@c0de.pro',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'github = mkdocs_github',
        ]
    },
    zip_safe=False
)