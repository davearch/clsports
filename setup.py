#!/usr/bin/python
# sportsCommand
# Command Line Sports News

# GNU General Public License

__author__ = "David Archuleta Jr, Michael McCauley"
__copyright__ = "Copyright (c) 2015 David Archuleta Jr, Michael McCauley"
__license__ = "GPL"

import sys
import codecs

import setuptools
from setuptools import setup, find_packages

def long_description():
	with codecs.open('README.md', encoding='utf8') as f:
		return f.read()

setup(
	name='sportsCommand',
	version='1.0',
	description='Sports news aggregator for the command line.',
	long_description=long_description(),
	author='David Archuleta',
	author_email='davearch@email.arizona.edu',
	url='',
        scripts = [
                'bin/clsportsClient',
        ],
	packages=find_packages(),
)
