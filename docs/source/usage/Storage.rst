************
Storage Zone
************

Create Storage Zone
^^^^^^^^^^^^^^^^^^^

* Syntax: ``b.Storage.create(name, main_storage_region, replica_regions``
* Returns: StorageZone object

*TODO: Add description*

Usage example::

   # Create a Storage Zone (available regions are listed below)
   b.Storage.create(name='example-a', main_storage_region='NY', replica_regions=['DE', 'SG', 'SYD'])
   # Returns: <StorageZone: example-a (id: 1234)>

Storage Regions
---------------

-  DE - Europe (Falkenstein)
-  NY - North America (New York)
-  SG - Asia (Singapore)
-  SYD - Oceania (Sydney)

List Storage Zones
^^^^^^^^^^^^^^^^^^

* Syntax: ``b.Storage.all()``
* Returns: List of StorageZone objects

*TODO: Add description*

Delete a Storage Zone
^^^^^^^^^^^^^^^^^^^^^

* Syntax: ``b.Storage.delete(Id)``

*TODO: Add description*

Usage example::

    b.Storage.delete(1234)
    # Returns: None

Get a Storage Zone
^^^^^^^^^^^^^^^^^^

* Syntax: ``b.Storage.get(Id)``
* Returns: StorageZone object

*TODO: Add description*

Usage example::

    zone = b.Storage.get(1234)
    # Returns: <StorageZone: example-a (id: 1234)>

Storage Files
^^^^^^^^^^^^^

Get a Storage Zone 
------------------

* Syntax: ``b.StorageZone.get(Id)``
* Returns: StorageZone object

*TODO: Add description*

Usage example::

    zone = b.Storage.get(1234)
    # Returns: <StorageZone: example-a (id: 1234)>

Lists files in the zone
-----------------------

* Syntax: ``zone.all()``
* Returns: List of StorageFile object

*TODO: Add description*

Usage example::

    # Lists files in the zone
    obj_list = zone.all()
    # Returns [<StorageFile: index.html>, <StorageFile: base.css>]

Get a file
----------

* Syntax: ``zone.get(file_path)``
* Returns: StorageFile object

*TODO: Add description*

Usage example::

    # Get a file
    obj = zone.get('index.html')
    #Returns <StorageFile: index.html>

Get a file as StorageObject
---------------------------

* Syntax: ``b.Storage.get_object(Id)``
* Returns: StorageObject

*TODO: Add description*

Usage example::

    # Get a file as StorageObject
    zone = b.Storage.get_object(1234)
    # Returns: <StorageObject: example-a (id: 1234)>

Download File
-------------

* Syntax: ``obj.download()``

*TODO: Add description*

Delete a file
-------------

* Syntax: ``zone.delete_file(file_path)``

*TODO: Add description*

Upload a File
-------------

* Syntax: ``zone.upload_file(dest_path, file_name, local_path)``
* Returns: StorageFile object

*TODO: Add description*

Usage example::

    # Upload a File
    zone.upload_file(dest_path='folder/path/', file_name='error.html', local_path='/home/mj/work/')
    # Returns: <StorageFile: error.html>

Create a file from a string
---------------------------

* Syntax: ``zone.create_file(file_name, string)``
* Returns: StorageFile

*TODO: Add description*

Usage example::

    # Create a file from a string
    zone.create_file('base.css', "body {background-color: powderblue;}")
    # Returns: <StorageFile: base.css>
    
Storage JSON Files
^^^^^^^^^^^^^^^^^^

Create a json file
------------------
* Syntax: ``zone.create_json(file_name,**kwargs)``

*TODO: Add description*

Usage example::

    # Create a json file
    mj = zone.create_json('23.json', {'first_name':'Michael', 'last_name': 'Jordan'})
    # Returns <StorageJSONFile: 23.json>

Get information from file
-------------------------
* Syntax: ``file[key]``

*TODO: Add description*

Usage example::

    # Get information from file
    mj['first_name']
    # Returns: 'Michael'

