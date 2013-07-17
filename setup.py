from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(name='mcerp',
    version='0.9',
    author='Abraham Lee',
    description='Real-time Monte Carlo, Latin-Hypercube Sampling-based, Error Propagation',
    author_email='tisimst@gmail.com',
    url='https://github.com/tisimst/mcerp',
    license='BSD License',
    long_description=long_description,
    package_dir={'mcerp':''},
    packages=['mcerp'],
    requires=['numpy','scipy'],
    include_package_data = True,
    package_data = {
        '': ['revision_history.txt', 'README.rst'],
        },
    keywords=[
        'monte carlo', 
        'latin hypercube', 
        'sampling calculator', 
        'error propagation', 
        'uncertainty', 
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
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
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
        ]
    )
