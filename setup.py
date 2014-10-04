import os
from setuptools import setup, find_packages

# dependencies: Django, collection, itertools, autoslug

setup(
    name='django-active-login-required',
    version='0.1',
    description='',
    author='Matt Dennewitz',
    author_email='mattdennewitz@gmail.com',
    url='http://github.com/mattdennewitz/django-active-login-required',
    packages=find_packages(),
    install_requires=['django >= 1.6'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
