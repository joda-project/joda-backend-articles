joda-backend-articles
=====================
|web| |pypi| |license| |codecov| |travis|

This is a Django powered articles backend for Joda - a simple reference
management web application. For details see the `homepage <https://joda.tano.si>`_
or `main repository <https://github.com/joda-project/joda>`_.

Quick start
-----------
1. Install package ``pip install joda_articles`` inside Joda virtual environment.

2. Add Joda Articles to your ``INSTALLED_APPS`` and ``JODA_FEATURES`` settings::

    INSTALLED_APPS = [
        ...
        'joda_articles',
    ]

    JODA_FEATURES = [
        ...
        'articles',
    ]

3. Run ``python manage.py migrate`` to create the articles models.


Contributing
------------
There are several guidelines on contributing to Joda:

- `Submitting issues <https://github.com/joda-project/joda/blob/master/CONTRIBUTING.md#submitting-issues>`_
- `Proposing a new feature <https://github.com/joda-project/joda/blob/master/CONTRIBUTING.md#feature-requests>`_
- `Submiting a pull-request <CONTRIBUTING.md#pull-requests>`_
- `Building instructions <BUILDING.md>`_


Copyright info
--------------
Copyright (C) 2016-2017 Tadej Novak

This project may be used under the terms of the
GNU Affero General Public License version 3.0 as published by the
Free Software Foundation and appearing in the file `LICENSE.md <LICENSE.md>`_.


.. |web| image:: https://img.shields.io/badge/web-joda.tano.si-green.svg
    :alt: Homepage
    :scale: 100%
    :target: https://joda.tano.si

.. |pypi| image:: https://img.shields.io/pypi/v/joda-articles.svg
    :alt: PyPI
    :scale: 100%
    :target: https://pypi.python.org/pypi/joda-articles

.. |license| image:: https://img.shields.io/github/license/joda-project/joda-backend-articles.svg
    :alt: License
    :scale: 100%
    :target: https://github.com/joda-project/joda-backend-articles/blob/master/LICENSE.md

.. |travis| image:: https://travis-ci.org/joda-project/joda-backend-articles.svg?branch=master
    :alt: Build Status
    :scale: 100%
    :target: https://travis-ci.org/joda-project/joda-backend-articles

.. |codecov| image:: https://codecov.io/github/joda-project/joda-backend-articles/coverage.svg?branch=master
    :alt: codecov.io
    :scale: 100%
    :target: https://codecov.io/github/joda-project/joda-backend-articles?branch=master
