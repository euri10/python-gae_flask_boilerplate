========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-gae_flask_boilerplate/badge/?style=flat
    :target: https://readthedocs.org/projects/python-gae_flask_boilerplate
    :alt: Documentation Status

.. |requires| image:: https://requires.io/github/euri10/python-gae_flask_boilerplate/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/euri10/python-gae_flask_boilerplate/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/euri10/python-gae_flask_boilerplate/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/euri10/python-gae_flask_boilerplate

.. |version| image:: https://img.shields.io/pypi/v/gae-flask-boilerplate.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/gae-flask-boilerplate

.. |commits-since| image:: https://img.shields.io/github/commits-since/euri10/python-gae_flask_boilerplate/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/euri10/python-gae_flask_boilerplate/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/gae-flask-boilerplate.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/gae-flask-boilerplate

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/gae-flask-boilerplate.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/gae-flask-boilerplate

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/gae-flask-boilerplate.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/gae-flask-boilerplate


.. end-badges

gae falsk

* Free software: BSD 2-Clause License

Installation
============

::

    pip install gae-flask-boilerplate

Documentation
=============

https://python-gae_flask_boilerplate.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
