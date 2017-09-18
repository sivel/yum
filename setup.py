#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# Copyright 2005 Duke University

import os
import re
import codecs

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    try:
        f = codecs.open(os.path.join(here, *file_paths), 'r', 'latin1')
        version_file = f.read()
        f.close()
    except:
        raise RuntimeError("Unable to find version string.")

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Get the long description from the relevant file
try:
    f = codecs.open('README', encoding='utf-8')
    long_description = f.read()
    f.close()
except:
    long_description = ''


setup(
    name='python-yum',
    version=find_version('yum/__init__.py'),
    description=('Yum - an automatic updater and installer for rpm-based '
                 'systems'),
    long_description=long_description,
    keywords='yum python-yum',
    author='YUM',
    author_email='yum-devel@lists.baseurl.org',
    url='http://yum.baseurl.org',
    license='GNU General Public License v2 or later (GPLv2+)',
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        ('License :: OSI Approved :: GNU General Public License v2 or later '
         '(GPLv2+)'),
    ]
)
