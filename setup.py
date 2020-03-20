import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtail-buttons',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    description='Add a button section in the Draftail WYSIWYG editor.',
    long_description=README,
    url='https://github.com/KalobTaulien/wagtail-button-block',
    author='Eric Sherman, Kalob Taulien',
    author_email='ericandrewsherman@gmail.com, kalob@learnwagtail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Wagtail',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',

    ],
)
