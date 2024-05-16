from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()
    f.close()

setup(
name='spp',
version='0.1',
author='rawmiT',
author_email='ramtinpourmoghadam00@gmail.com',
description='A simple Security Per Point system based on PostgreSQL',
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: Linux/Windows',
],
python_requires='>=3',
install_requires=requirements
)