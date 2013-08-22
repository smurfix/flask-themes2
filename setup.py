from setuptools import setup
import sys

requires = ["Flask>=0.6", "simplejson"]
#if sys.version_info < (2, 6):
#    requires.append("simplejson")

def long_desc():
    with open('README.rst', 'rb') as f:
        return f.read()

execfile("quokka_themes/version.py")

kw = {
    "name": "Quokka-Themes",
    "version": __version__,
    "url": "https://github.com/pythonhub/quokka-themes",
    "license": "MIT",
    "author": "rochacbruno",
    "author_email": "rochacbruno+pythonhub@gmail.com",
    "description": "Provides infrastructure for theming Flask applications (and supports Flask>=0.6!)",
    "long_description": long_desc(),
    "keywords": "flask themes theming style",
    "packages": [
        "quokka_themes"
    ],
    "zip_safe": False,
    "install_requires": requires,
    "tests_require": "nose",
    "test_suite": "nose.collector",
    "classifiers": [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
}

if __name__ == "__main__":
    setup(**kw)
