*********
Pull Zone
*********

Get a Pull Zone
^^^^^^^^^^^^^^^

.. code:: python

   zone = b.Zone.get(id='myzone')
   #Returns: <Zone: myzone > 

Create a Pull Zone
^^^^^^^^^^^^^^^^^^

.. code:: python

   b.Zone.create(
       Name='myzone',
       Type=0, # 0 = Standard and 1 = High Volume
       OriginUrl='https://example.org',
       StorageZoneId='storage-zone-id'
   )

List Pull Zones
^^^^^^^^^^^^^^^

.. code:: python

   b.Zone.list()

Update a Pull Zone
^^^^^^^^^^^^^^^^^^

.. code:: python

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
   # From Zone object
   zone.update(
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

.. code:: python

   #From top-level
   b.Zone.delete(id='myzone')

   #From Zone object
   zone.delete()

Purge File From Pull Zone
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   # From top-level
   b.Purge.create(url='https://myzone.b-cdn.net/css/style.css')

   # From Zone Object
   zone.purge_file('css/style.css')

Purge Entire Pull Zone
^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   # From top-level
   b.Zone.purge(
       id='myzone'
   )
   # From Zone object
   zone.purge()

Add Edge Rule to Pull Zone
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

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

.. code:: python

   # Create a hostname
   b.Zone.create_hostname("myHostname")

   # Delete a hostname
   b.Zone.delete_hostname("myHostname")