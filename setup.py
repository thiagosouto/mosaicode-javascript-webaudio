# -*- coding: utf-8 -*-

from glob import glob

DISTUTILS_DEBUG = "True"

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {}

config['classifiers'] = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: JavaScript',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Code Generators',
]

setup(name='mosaicode-lib-javascript-webaudio',
      install_requires=['mosaicode'],
      tests_require=[],
      test_suite='',
      version='1.6',
      packages = find_packages(exclude=["tests.*", "tests"]),
      scripts=[],
      description='Computer Music Programming Tool',
      author='Bits & Beads Research Lab',
      author_email='mosaicode-dev@googlegroups.com',
      maintainer="Bits & Beads Research Lab",
      maintainer_email="mosaicode-dev@googlegroups.com",
      license="GNU GPL3",
      url='https://mosaicode.github.io/',

      # this is fucked up! must put it in package_data!!
      data_files=[
            ('/usr/share/mosaicode/extensions/mosaicode_lib_javascript_webaudio/examples', glob("examples/*"))
      ],
      **config
      )
