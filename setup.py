from setuptools import setup, find_packages

setup(
name='ez-localizr',
version='0.0.3',
author='Tyler Koziol',
author_email='tora@tora-ouji.com',
description='An insanely simple localization tool for Python.',
packages=find_packages(),
py_module=['ezlocalizr', '__init__'],
install_requires=['PyYAML', 'ftfy'],
scripts=[
	'ezlocalizr/__init__.py',
	'ezlocalizr/ezlocalizr.py'
],
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.8',
)