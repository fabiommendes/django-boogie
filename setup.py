import re
import os
from setuptools import setup, find_packages

init = open(os.path.join('src', 'boogie', '__init__.py')).read()
version = re.search(r"__version__ = '(\d+\.\d+.\d+)'", init).group(1)

setup(
    name='django-boogie',
    version=version,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    setup_requires='setuptools >= 30.3',
)
