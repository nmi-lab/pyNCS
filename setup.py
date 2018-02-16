# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='pyNCSre',
	version='20180208_0',
	description='Python Neurormophic Chips and Systems, reworked',
	author='Emre Neftci',
	author_email='eneftci@uci.edu',
	url='https://github.com/nmi-lab/pyNCS',
        download_url='https://github.com/nmi-lab/pyNCS/tarball/stable_20170814',
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
