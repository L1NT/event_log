# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='event_log',
    version='0.0.1',
    description='Simple Django app to report running/cycling/triathlon events.',
    author='Luke Jeter)',
    author_email='luke.jeter@gmail.com',
    url='',
    download_url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: None',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)



