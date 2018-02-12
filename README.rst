========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |requires|
        | |codecov|


.. |requires| image:: https://requires.io/github/euri10/python-gae_flask_boilerplate/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/euri10/python-gae_flask_boilerplate/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/euri10/python-gae_flask_boilerplate/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/euri10/python-gae_flask_boilerplate

.. end-badges

gae falsk

* Free software: BSD 2-Clause License


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
