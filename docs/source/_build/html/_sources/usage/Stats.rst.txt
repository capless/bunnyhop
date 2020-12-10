*****
Stats
*****

* Syntax: ``b.Stats.get(date_From, dateTo, pullZone, serverZoneId)``

*TODO: Add description*

Usage example::

    b.Stats.get(dateFrom='2018-12-01', 
                dateTo='2020-01-01', 
                pullZone='example-zone', 
                serverZoneId='serverZoneID'
                )


Get Billing Summary
===================

* Syntax: ``b.Billing.get()``

*TODO: Add description*


Applying coupon codes
=====================

* Syntax: ``b.Billing.applycode(couponCode)``

*TODO: Add description*

Usage example::

    b.Billing.applycode(couponCode='somecode123')