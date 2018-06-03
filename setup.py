from pathlib import Path

from setuptools import setup


BASEDIR = Path(__file__).resolve().parent


setup(name='randomness',
      version='0.1',
      description='Generates random secrets (passwords, etc).',
      long_description=((BASEDIR / 'README.rst').read_text()),
      url='http://github.com/crowsonkb/randomness',
      author='Katherine Crowson',
      author_email='crowsonkb@gmail.com',
      license='MIT',
      packages=['randomness'],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': ['randomness=randomness.randomness:main'],
      })
