from setuptools import setup
from setuptools import find_packages

setup(name='logik',
      version='0.3',
      description='A simple way to interact with propositional logic in python',
      url='https://github.com/64bit-lab/Logik',
      author='Arthur Correnson',
      author_email='arthur.correnson@gmail.com',
      license='MIT',
      packages=find_packages(),
      scripts=['bin/logik'],
      zip_safe=False)
