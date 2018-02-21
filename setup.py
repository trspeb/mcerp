import os
from setuptools import setup
#import distutils.core

## Building through 2to3, for Python 3 (see also setup(...,
## cmdclass=...), below:
#try:
    #from distutils.command.build_py import build_py_2to3 as build_py
#except ImportError:
    ## 2.x
    #from distutils.command.build_py import build_py

import mcerp3

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

readme = 'README.rst'

#distutils.core.setup(
setup(
    name='mcerp3',
    version=mcerp3.__version__,
    author='Paul Freeman',
    description='Real-time latin-hypercube-sampling-based Monte Carlo Error Propagation',
    author_email='paul.freeman.cs@gmail.com',
    url='https://github.com/paul-freeman/mcerp3',
    license='BSD License',
    long_description=read(readme),
    package_data={'': [readme]},
    packages=[
        'mcerp3', 
        ],
    install_requires=[
        'numpy', 
        'scipy', 
        'matplotlib'
        ],
    keywords=[
        'monte carlo', 
        'latin hypercube', 
        'sampling calculator', 
        'error propagation', 
        'uncertainty', 
        'risk analysis',
        'error', 
        'real-time'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
        ],
    #cmdclass={'build_py': build_py}
    )
