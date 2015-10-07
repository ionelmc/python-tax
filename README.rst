===
Tax
===

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-tax/badge/?style=flat
    :target: https://readthedocs.org/projects/python-tax
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ionelmc/python-tax.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/python-tax

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/python-tax?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/python-tax

.. |requires| image:: https://requires.io/github/ionelmc/python-tax/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/python-tax/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/ionelmc/python-tax/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/python-tax

.. |codecov| image:: https://codecov.io/github/ionelmc/python-tax/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/python-tax

.. |landscape| image:: https://landscape.io/github/ionelmc/python-tax/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ionelmc/python-tax/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg?style=flat
    :target: https://www.codacy.com/app/ionelmc/python-tax
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/ionelmc/python-tax/badges/gpa.svg
   :target: https://codeclimate.com/github/ionelmc/python-tax
   :alt: CodeClimate Quality Status
.. |version| image:: https://img.shields.io/pypi/v/tax.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/tax

.. |downloads| image:: https://img.shields.io/pypi/dm/tax.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/tax

.. |wheel| image:: https://img.shields.io/pypi/wheel/tax.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/tax

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/tax.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/tax

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/tax.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/tax

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/ionelmc/python-tax/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/ionelmc/python-tax/

A taxy Tox to tax your current site-packages. This is a variant of Tox that doesn't use virtualenvs at all - just installs everything in
the current environment. Use at your own peril.

* Free software: BSD license

Installation
============

::

    pip install tax

Usage
=====

Instead of ``tox`` just run::

    tax

**Warning: all virtualenv creation is skipped. Good luck.**

Documentation
=============

https://python-tax.readthedocs.org/

Development
===========

To run the all tests run::

    tox
