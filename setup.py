# -*- coding: utf-8 -*-
from setuptools import setup
import glob


app_scripts = [i for i in glob.glob("scripts/*")]

setup(
        name='pyunicorn',
        version='0.2.1',
        description='Python client interface to Unicorn service.',
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
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Topic :: Software Development :: Libraries :: Python Modules', 
            'Topic :: Scientific/Engineering :: Physics'],
)
