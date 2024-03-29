# -*- coding: utf-8 -*-
from setuptools import setup
import glob

def readme():
    with open('README.md', 'r') as f:
        return f.read()

app_scripts = [i for i in glob.glob("scripts/*")]

setup(
    name='python-unicorn',
    version='0.4.4',
    description='Python client interface to Unicorn service.',
    long_description=readme() + "\n\n",
    long_description_content_type='text/markdown',
    author='Tong Zhang',
    author_email='zhangt@frib.msu.edu',
    packages=['unicorn.client',
              'unicorn'],
    package_dir={
        'unicorn.client': 'unicorn/client',
        'unicorn': 'unicorn'
    },
    scripts=app_scripts,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    install_requires=['requests', 'xlrd', 'numpy'],
)
