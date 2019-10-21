#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup, find_packages


setup(
    name='django-portmone-ua',
    version='0.1',
    author='Ivan Petukhov',
    author_email='satels@gmail.com',
    packages=find_packages(exclude=['docs', 'tests']),
    url='https://zvonok.com',
    download_url='https://github.com/satels/django-portmone-ua/zipball/master',
    license='MIT license',
    description=u'Приложение для работы с portmone.com.ua.',
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
    install_requires=[],
    include_package_data=True,
)
