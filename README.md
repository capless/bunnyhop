# bunnyhop
Python library for BunnyCDN

## Status
Documentation only phase

## Install

```shell script
pip install bunnyhop
```

## Getting Started 

```python
from bunnyhop import Bunny

b = Bunny('<api_key>')
```
## Pull Zones

#### Get a Pull Zone

```python
zone = b.Zone.get(id='myzone')
#Returns: <Zone: myzone > 
```

#### Create a Pull Zone
```python
b.Zone.create(
    Name='myzone',
    Type=0, # 0 = Standard and 1 = High Volume
    OriginUrl='https://example.org',
    StorageZoneId='storage-zone-id'
)
```

#### List Pull Zones
```python
b.Zone.list()
```

#### Update a Pull Zone
```python
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
```

#### Delete Pull Zone
```python
#From top-level
b.Zone.delete(id='myzone')

#From Zone object
zone.delete()
```

#### Purge File From Pull Zone
```python
# From top-level
b.Purge.create(url='https://myzone.b-cdn.net/css/style.css')

# From Zone Object
zone.purge_file('css/style.css')
```

#### Purge Esntire Pull Zone
```python
# From top-level
b.Zone.purge(
    id='myzone'
)
# From Zone object
zone.purge()
```

#### Add Edge Rule to Pull Zone
```python
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
```
<hr/>
## Storage

### Storage Zones

#### Create Storage Zone
```python

# Create a Storage Zone (available regions are listed below)
b.Storage.create(name='example-a', main_storage_region='NY', replica_regions=['DE', 'SG', 'SYD'])
# Returns: <StorageZone: example-a (id: 1234)>
```

##### Storage Regions

- DE - Europe (Falkenstein)
- NY - North America (New York)
- SG - Asia (Singapore)
- SYD - Oceania (Sydney)

#### List Storage Zones
```python
b.Storage.all()
# Returns: [<StorageZone: example-a (id: 1234)>, <StorageZone: example-b (id: 12345)>]
```

#### Delete a Storage Zone
```python
b.Storage.delete(1234)
# Returns: None
```

#### Get a Storage Zone
```python
zone = b.Storage.get(1234)
# Returns: <StorageZone: example-a (id: 1234)>
```

### Storage Files

```python
# Get a Storage Zone
zone = b.StorageZone.get(1234)
# Returns: <StorageZone: example-a (id: 1234)>

# Lists files in the zone
obj_list = zone.all()
# Returns [<StorageFile: index.html>, <StorageFile: base.css>]

# Get a file
obj = zone.get('index.html')
#Returns <StorageFile: index.html>

# Download that File
obj.download()

# Delete a file
zone.delete('index.html')

# Upload a File
zone.upload_file(dest_path='folder/path/error.html', local_path='/home/mj/work/error.html')
# Returns: <StorageFile: error.html>

# Create a file from a string
zone.create_file('base.css', "body {background-color: powderblue;}")
# Returns: <StorageFile: base.css>
```

### Storage JSON Files

```python

# Create a json file
mj = zone.create_json('23.json', {'first_name':'Michael', 'last_name': 'Jordan'})
# Returns <StorageJSONFile: 23.json>

# Get information from file
mj['first_name']
# Returns: 'Michael'
```

<hr/>
# Purge

## Create a Purge
```python
# Purge a zone or file
b.Purge.create(url='https://myzone.b-cdn.net/style.css')
```

<hr/>
# Stats

```python
b.Stats.get(dateFrom='2018-12-01', dateTo='2020-01-01', pullZone='example-zone', serverZoneId='serverZoneID')
```
<hr/>
# Billing

#### Get Billing Summary
```python
b.Billing.get()
```

#### ApplyCode

```python
b.Billing.applycode(couponCode='somecode123')
```

<hr/>

# Bunny Stream

1. Acquire first your BunnyNet Stream API key. This Stream API key is different from your own API key.
2. Create a Video Library in your Bunny console and acquire its Library ID by `navigating to it > API > Video Library ID`
3. Initialize BunnyStream yung the two keys you have.


```python
from bunnyhop import BunnyStream
from envs import env
import os


BUNNYCDN_STREAM_API_KEY = '<STREAM_API_KEY>'
BUNNYCDN_STREAM_LIBRARY_KEY = '<LIBRARY_KEY>'


b = BunnyStream(
    api_key=BUNNYCDN_STREAM_API_KEY,
    library_id=BUNNYCDN_STREAM_LIBRARY_KEY
)
```


# StreamCollection
A `Collection` that can be created in a Bunny's video library.


## List Collection
Lists all of collections available in the given library ID


```python
b.StreamCollection.all(items_per_page=9)
```



## Create Collection
Create a collection. Returns a `StreamCollection` object which you can perform the same operations if you want to not specify the ID


```python
stream_col = b.StreamCollection.create('test')
stream_col.guid
```



## Get a Collection
Acquires a collection based on the GUID you gave. This returns a `StreamCollection` object.


```python
stream_col = b.StreamCollection.get('6d1089a9-0764-4580-a5c9-e26a98fa7812')
```


## Update a Collection
Updates a `StreamCollection` object if it has properties but if not, GUID is required.


```python
stream_col.update('updated')
```


## Delete a Collection
Deletes a collection based on a GUID you provided. If the object is a `StreamCollection` property, it will delete itself if you didn't specified a GUID.


```python
stream_col.delete()
```



# Video
A `Video` that can be created and then uploaded to a collection or just a library.

## Create a Video
Create a `Video` object in Bunny API. 

**This is required before running `upload()`**


```python
vid = b.Video.create(title='new_video', collection_id='6d1089a9-0764-4580-a5c9-e26a98fa7812')
```


## Upload a Video
Uploads the Video to Bunny. **`create()` is required before uploading**. If the object is a `Video`-class it will upload itself. Otherwise, provide the GUID of the created video.


```python
import requests

mp4_file = requests.get('https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/1080/Big_Buck_Bunny_1080_10s_1MB.mp4')
vid.upload(mp4_file.content)
# with open(mp4_file, 'rb') as file:
#     vid.upload(file)
```


## Get a Video
Acquires a `Video` based on the given GUID.


```python
vid = b.Video.get('fde3acc9-7139-403a-a514-781151e57841')
```


## Fetch a Video
Uploads a video to the specified `video_id` from the URL that was given. Requires `create()` to be called first and use its provided `video_id`


```python
b.Video.fetch(
    url='https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/1080/Big_Buck_Bunny_1080_10s_1MB.mp4',
    headers={},
    video_id='5a32233f-b1fd-41f7-ae41-c49ed714fc67')
```


## List videos
Acquires the list of the videos that are in the current library. 

**Notes**

- The minimum `itemsPerPage` is 10, anything below that will be ignored.


```python
b.Video.all(items_per_page=1)
```

## Update a Video
Update a `Video`'s title and collection it belongs. If the object is a `Video` class, it will update itself without needing to provide GUID.


```python
vid.update('updatedTitle', '6d1089a9-0764-4580-a5c9-e26a98fa7812')
```


## Delete a Video
Deletes a `Video` based on its GUID. If the object is an `Video` class, it will delete itself.


```python
vid.delete()
```


## Set Video's thumbnail
Set a `Video`'s thumbnail with the specified image's URL


```python
vid.set_thumbnail(thumbnail_url='https://dummyimage.com/600x400/000/fff.jpg')
```


## Add Captions


```python
import base64
import requests

cc_file = requests.get('https://raw.githubusercontent.com/andreyvit/subtitle-tools/master/sample.srt')
cc_to_upload = base64.b64encode(cc_file.content)

print(cc_to_upload)
vid.add_caption(srclang='en', label='test_label', captions_file=cc_to_upload)
```


## Delete Captions


```python
vid.delete_caption('en')
```