*********
Pull Zone
*********

Get a Pull Zone
^^^^^^^^^^^^^^^

* Syntax: ``b.Zone.get(id)``

*TODO: Add description*

Usage example::

    zone = b.Zone.get(id='myzone')
    #Returns: <Zone: myzone >

Create a Pull Zone
^^^^^^^^^^^^^^^^^^

* Syntax: ``b.Zone.create(name, Type, OriginUrl, StorageZoneId)``

*TODO: Add description*

Usage example::

   b.Zone.create(
       Name='myzone',
       Type=0, # 0 = Standard and 1 = High Volume
       OriginUrl='https://example.org',
       StorageZoneId='storage-zone-id'
   )

List Pull Zones
^^^^^^^^^^^^^^^

* Syntax: ``b.Zone.list()``

*TODO: Add description*

Update a Pull Zone
^^^^^^^^^^^^^^^^^^

From Id
-------
* Syntax: ``b.Zone.update(Id, **kwargs)``

From Zone Object
-------
* Syntax: ``zone.update(**kwargs)``

*TODO: Add description*

Optional Parameters:

* ``OriginUrl`` *TODO: Add description*
* ``AllowedReferrers`` *TODO: Add description*
* ``BlockedIps`` *TODO: Add description*
* ``EnableCacheSlice`` *TODO: Add description*
* ``EnableGeoZoneUS`` *TODO: Add description*
* ``EnableGeoZoneASIA`` *TODO: Add description*
* ``EnableGeoZoneSA`` *TODO: Add description*
* ``EnableGeoZoneAF`` *TODO: Add description*
* ``ZoneSecurityEnabled`` *TODO: Add description*
* ``ZoneSecurityIncludeHashRemoteIP`` *TODO: Add description*
* ``IgnoreQueryStrings`` *TODO: Add description*
* ``MonthlyBandwidthLimit`` *TODO: Add description*
* ``AccessControlOriginHeaderExtensions`` *TODO: Add description*
* ``EnableAccessControlOriginHeader`` *TODO: Add description*
* ``BlockRootPathAccess`` *TODO: Add description*
* ``EnableWebpVary`` *TODO: Add description*
* ``EnableLogging`` *TODO: Add description*
* ``DisableCookies`` *TODO: Add description*
* ``EnableOriginShield`` *TODO: Add description*
* ``OriginShieldZoneCode`` *TODO: Add description*
* ``AddCanonicalHeader`` *TODO: Add description*
* ``CacheControlMaxAgeOverride`` *TODO: Add description*
* ``AddHostHeader`` *TODO: Add description*
* ``AWSSigningEnabled`` *TODO: Add description*
* ``AWSSigningKey`` *TODO: Add description*
* ``AWSSigningRegionName`` *TODO: Add description*
* ``AWSSigningSecret`` *TODO: Add description*
* ``EnableTLS1`` *TODO: Add description*
* ``EnableTLS1_1`` *TODO: Add description*

Usage example::

    b.Zone.update(
        id='zone-id', #Positional Argument
        OriginUrl='http://example.org',
        AllowedReferrers=['app.example.org', 'www.example.org'],
        BlockedIps=['122.33.22.11'],
        EnableCacheSlice=False,
        EnableGeoZoneUS=True,
        EnableGeoZoneEU=True,
        EnableGeoZoneASIA=True,
        EnableGeoZoneSA=True,
        EnableGeoZoneAF=True,
        ZoneSecurityEnabled=True,
        ZoneSecurityIncludeHashRemoteIP=True,
        IgnoreQueryStrings=True,
        MonthlyBandwidthLimit=1073741824,
        AccessControlOriginHeaderExtensions=['jpg', 'png'],
        EnableAccessControlOriginHeader=True,
        BlockRootPathAccess=True,
        EnableWebpVary=True,
        EnableLogging=True,
        DisableCookies=False,
        BudgetRedirectedCountries=['RU', 'BR'],
        BlockedCountries=['RU', 'BR'],
        EnableOriginShield=True,
        OriginShieldZoneCode='FR',
        AddCanonicalHeader=0,
        CacheControlMaxAgeOverride=-1,
        AddHostHeader=True,
        AWSSigningEnabled=True,
        AWSSigningKey='AK_EXAMPLEKEY',
        AWSSigningRegionName='us-east-1',
        AWSSigningSecret='SK_EXAMPLESECRETKET',
        EnableTLS1=True,
        EnableTLS1_1=True
    )


Delete Pull Zone
^^^^^^^^^^^^^^^^

From Id
-------
* Syntax: ``b.Zone.delete(id)``

From Zone Object
-------
* Syntax: ``zone.delete()``

*TODO: Add description*


Purge File From Pull Zone
^^^^^^^^^^^^^^^^^^^^^^^^^

From Id
-------
* Syntax: ``b.Purge.create(url)``

From Zone Object
-------
* Syntax: ``zone.purge_file(file_path)``

*TODO: Add description*

Purge Entire Pull Zone
^^^^^^^^^^^^^^^^^^^^^^

From Id
-------
* Syntax: ``b.Zone.purge(id)``

From Zone Object
-------
* Syntax: ``zone.purge()``

*TODO: Add description*


Add Edge Rule to Pull Zone
^^^^^^^^^^^^^^^^^^^^^^^^^^

* Syntax: ``b.Zone.create_edge_rule(id, **kwargs)``

*TODO: Add description*

Optional Parameters:

* ``Guid`` *TODO: Add description*
* ``ActionParameter1`` *TODO: Add description*
* ``ActionParameter2`` *TODO: Add description*
* ``Enabled`` *TODO: Add description*
* ``Description`` *TODO: Add description*
* ``ActionType`` *TODO: Add description*
* ``TriggerMatchingType`` *TODO: Add description*
* ``Triggers`` *TODO: Add description*

Usage example::

    b.Zone.create_edge_rule(
        id='myzone',
        Guid="6a2e94df-8aa9-4cd2-b89d-16752102ef9f", # GUID of the edge rule
        ActionParameter1 = "My-Header",
        ActionParameter2 = "HeaderValue",
        Enabled = True,
        Description = "My header value",
        ActionType = 0, # 0 = ForceSSL, 1 = Redirect, 2 = OriginUrl, 3 = OverrideCacheTime, 4 = BlockRequest, 5 = SetResponseHeader, 6 = SetRequestHeader, 7 = ForceDownload, 8 = DisableTokenAuthentication, 9 = EnableTokenAuthentication
        TriggerMatchingType = 1    
        Triggers = []
    )

Hostnames
^^^^^^^^^

*TODO: Add description*

Create a hostname
-----------------
* Syntax: ``b.Zone.create_hostname(hostname)``

Delete a hostname
-----------------
* Syntax: ``b.Zone.delete_hostname(hostname)``

