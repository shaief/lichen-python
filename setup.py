import os
from setuptools import setup
from pip.req import parse_requirements

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='Lichen',
    version='0.1.0',
    author='Shai Efrati',
    author_email='shaief@gmail.com',
    packages=['lichen', 'lichen.test'],
    #url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description=("A small software to analyze percentage of lichen seen on a rock"
                "from an image or a sequence of images"),
    keywords="lichen image analyzer",
    #long_description=read('README.md'),
    install_requires=required,
    )