===============================
``mcerp`` Package Documentation
===============================

Overview
========

``mcerp`` is a stochastic calculator for `Monte Carlo methods`_ that uses 
`latin-hypercube sampling`_ to perform non-order specific 
`error propagation`_ (or uncertainty analysis). With this package you can 
**easily** and **transparently** track the effects of uncertainty 
through mathematical calculations. Advanced mathematical functions, similar 
to those in the standard `math`_ module can also be evaluated directly. 

What's New In This Release
==========================

- Added full customization capabilities to the plotting function with 
  ``**kwargs``.
- Added `package documentation`_.

Required Packages
=================

The following packages should be installed automatically (if using ``pip``
or ``easy_install``), otherwise they will need to be installed manually:

- `NumPy`_ : Numeric Python
- `SciPy`_ : Scientific Python
- `Matplotlib`_ : Python plotting library

These packages come standard in *Python(x,y)*, *Spyder*, and other 
scientific computing python bundles.

Main Features
=============

1. **Transparent calculations**. **No or little modification** to existing 
   code required.
    
2. Basic `NumPy`_ support without modification. (I haven't done extensive 
   testing, so please let me know if you encounter bugs.)

3. Advanced mathematical functions supported through the ``mcerp.umath`` 
   sub-module. If you think a function is in there, it probably is. If it 
   isn't, please request it!

4. **Easy statistical distribution constructors**. The location, scale, 
   and shape parameters follow the notation in the respective Wikipedia 
   articles.

5. **Correlation enforcement** and variable sample visualization capabilities.

6. **Probability calculations** using conventional comparison operators.

Installation
============

**Make sure you have the**  `SciPy`_ **and** `NumPy`_ **and** `Matplotlib`_ 
**packages installed!** This package won't work without them.

You have **several easy, convenient options** to install the ``mcerp`` 
package (administrative privileges may be required)

#. Simply copy the unzipped ``mcerp-XYZ`` directory to any other location that
   python can find it and rename it ``mcerp``.
    
#. From the command-line, do one of the following:
   
   a. Manually download the package files below, unzip to any directory, and run::
   
       $ [sudo] python setup.py install

   b. If ``setuptools`` is installed, run::

       $ [sudo] easy_install --upgrade mcerp
    
   c. If ``pip`` is installed, run::

       $ [sudo] pip install --upgrade mcerp

Python 3
--------

To use this package with Python 3.x, you will need to run the ``2to3`` 
conversion tool at the command-line using the following syntax while in the 
unzipped ``mcerp`` directory::

    $ 2to3 -w .
    
This should take care of the main changes required. Then, run::

    $ python3 setup.py install

If bugs continue to pop up, please email the author.

You can also get the bleeding-edge code from `GitHub`_ (though I can't 
promise there won't be stability issues...).

See also
========

- `uncertainties`_ : First-order error propagation
- `soerp`_ : Second-order error propagation

Contact
=======

Please send **feature requests, bug reports, or feedback** to 
`Abraham Lee`_.


    
.. _Monte Carlo methods: http://en.wikipedia.org/wiki/Monte_Carlo_method
.. _latin-hypercube sampling: http://en.wikipedia.org/wiki/Latin_hypercube_sampling
.. _soerp: http://pypi.python.org/pypi/soerp
.. _error propagation: http://en.wikipedia.org/wiki/Propagation_of_uncertainty
.. _math: http://docs.python.org/library/math.html
.. _NumPy: http://www.numpy.org/
.. _SciPy: http://scipy.org
.. _Matplotlib: http://matplotlib.org/
.. _scipy.stats: http://docs.scipy.org/doc/scipy/reference/stats.html
.. _uncertainties: http://pypi.python.org/pypi/uncertainties
.. _source code: https://github.com/tisimst/mcerp
.. _Abraham Lee: mailto:tisimst@gmail.com
.. _package documentation: http://pythonhosted.org/mcerp
.. _GitHub: http://github.com/tisimst/mcerp