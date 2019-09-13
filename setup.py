from setuptools import setup

setup(name='logik',
      version='0.1',
      description='A simple way to interact with propositional logic in python',
      url='https://github.com/64bit-lab/Logik',
      author='Arthur Correnson',
      author_email='arthur.correnson@gmail.com',
      license='MIT',
      packages=['logik'],
      scripts=['bin/logik'],
      zip_safe=False)