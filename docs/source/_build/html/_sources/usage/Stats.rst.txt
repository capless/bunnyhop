*****
Stats
*****

.. code:: python

   b.Stats.get(dateFrom='2018-12-01', dateTo='2020-01-01', pullZone='example-zone', serverZoneId='serverZoneID')


Get Billing Summary
===================

.. code:: python

   b.Billing.get()

Applying coupon codes
=====================

.. code:: python

   b.Billing.applycode(couponCode='somecode123')