from distutils.core import setup

setup(
    name='Lichen',
    version='0.1.0',
    author='Shai Efrati',
    author_email='shaief@gmail.com',
    packages=['lichen', 'lichen.test'],
    #url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='A small software to analyze percentage of lichen seen on a rock from an image or a sequence of images',
    #long_description=open('README.txt').read(),
    install_requires=[
        "PIL==1.1.7",
        "numpy==1.8.0",
        "wsgiref==0.1.2",
    ],
)