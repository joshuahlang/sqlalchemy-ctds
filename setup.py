#!/usr/bin/env python

import glob
import io
import os
import os.path
import platform
import re
import setuptools
import setuptools.dist
import sys


install_requires = [
    'ctds>=1.6',
    'SQLAlchemy',
]

setup_requires = [
    'pytest-runner'
]

tests_require = [
    'pytest'
]

def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf-8')
    ) as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r'''^__version__ = ['"]([^'"]*)['"]''',
        version_file,
        re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name = 'sqlalchemy_ctds',
    version = find_version(os.path.dirname(__file__), 'src', 'sqlalchemy_ctds', '__init__.py'),

    author = 'Joshua Lang',
    author_email = 'joshual@zillowgroup.com',
    description = 'SQLAlchemy connector for ctds',
    long_description = read('README.rst'),
    keywords = [
        'ctds',
        'mssql',
        'SQL Server',
        'SQLAlchemy',
    ],
    license = 'MIT',
    url = 'https://github.com/joshuahlang/sqlalchemy-ctds',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: C',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: SQL',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
    ],

    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*',

    packages = setuptools.find_packages('src'),
    package_data = {
        'sqlalchemy_ctds': []
    },
    package_dir = {'': 'src'},

    entry_points = {
        'sqlalchemy.dialects': [
              'mssql.ctds = sqlalchemy_ctds.ctds:MSDialect_ctds',
        ]
    },

    install_requires = install_requires,

    setup_requires = setup_requires,
    tests_require = tests_require,

    extras_require = {
        'tests': tests_require,
    },

    # Prevent easy_install from warning about use of __file__.
    zip_safe = False
)
