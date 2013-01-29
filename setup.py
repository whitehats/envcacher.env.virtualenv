#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright 2013 WhiteHats <office@whitehats.pl>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

__author__ = u'Tomasz Czyż'
__copyright__ = 'WhiteHats <office@whitehats.pl>'
__license__ = 'Apache License 2.0'

from setuptools import setup, find_packages
from envcacher.env.virtualenv import __version__


setup(name='envcacher.env.virtualenv',
      version=__version__,
      url='http://github.com/whitehats/envcacher.env.virtualenv/',
      download_url='http://pypi.python.org/pypi/envcacher.env.virtualenv/',
      license='Apache License 2.0',
      author=u'WhiteHats',
      author_email='office@whitehats.pl',
      description='Script for cache whole virtual environments (like python virtualenv or nodejs)',
      long_description=open('README').read(),
      zip_safe=False,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
      ],
      platforms='any',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['sh>=1.0.0',
                        'virtualenv',
                        'envcacher>=0.3.0'],
      entry_points={
          'envcacher.env': ['python = envcacher.env.virtualenv:PythonVirtualEnv',
                            'virtualenv = envcacher.env.virtualenv:PythonVirtualEnv']},
      )
