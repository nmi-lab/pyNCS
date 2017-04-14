# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='pyNCSre',
	version='20170129',
	description='Python Neurormophic Chips and Systems, repackaged',
	author='Emre Neftci',
	author_email='eneftci@uci.edu',
	url='https://github.com/nmi-lab/pyNCS',
	packages = ['pyNCSre', 'pyNCSre.pyST', 'pyNCSre.api'],
        package_dir={'' : 'src'},
	package_data={'pyNCSre' : ['data/*.dtd',
                             'data/chipfiles/*.csv',
                             'data/chipfiles/*.nhml',
                             'data/chipfiles/*.xml']},
        include_package_data=True,
        install_requires=['numpy',
                          'lxml',
                          'matplotlib'],
     )
