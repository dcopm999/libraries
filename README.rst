=====
PharmCRM libraries
=====

Набор базовых библиотке для PharmCRM

Quick start
-----------

1. Add "libraries" to your INSTALLED_APPS setting like this::

     INSTALLED_APPS = (
     ...
     'libraries',
     )
     
Coverage
--------

1. coverage setup.py tests
2. coverage xml
3. pylint --disable=W1202 --output-format=parseable --reports=no module > pylint.log
