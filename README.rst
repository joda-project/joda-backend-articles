Joda Articles Backend
=====================


Quick start
-----------
1. Add Joda Articles to your ``INSTALLED_APPS`` and ``JODA_FEATURES`` settings::

    INSTALLED_APPS = [
        ...
        'joda-articles',
    ]

    JODA_FEATURES = [
        ...
        'articles',
    ]

2. Run ``python manage.py migrate`` to create the articles models.


Copyright info
--------------
Copyright (C) 2016-2017 Tadej Novak

This project may be used under the terms of the
GNU Affero General Public License version 3.0 as published by the
Free Software Foundation and appearing in the file LICENSE.md.
