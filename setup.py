from setuptools import setup, find_packages

setup(
    name='firstpackage',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA hackathon python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/RobynLeighSmith2/firstpackage',
    author='RobynLeighSmith2',
    author_email='smith.robynleigh@gmail.com'
)
