************
Storage Zone
************

Create Storage Zone
^^^^^^^^^^^^^^^^^^^

.. code:: python


   # Create a Storage Zone (available regions are listed below)
   b.Storage.create(name='example-a', main_storage_region='NY', replica_regions=['DE', 'SG', 'SYD'])
   # Returns: <StorageZone: example-a (id: 1234)>

Storage Regions
'''''''''''''''

-  DE - Europe (Falkenstein)
-  NY - North America (New York)
-  SG - Asia (Singapore)
-  SYD - Oceania (Sydney)

List Storage Zones
^^^^^^^^^^^^^^^^^^

.. code:: python

   b.Storage.all()
   # Returns: [<StorageZone: example-a (id: 1234)>, <StorageZone: example-b (id: 12345)>]

Delete a Storage Zone
^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   b.Storage.delete(1234)
   # Returns: None

Get a Storage Zone
^^^^^^^^^^^^^^^^^^

.. code:: python

   zone = b.Storage.get(1234)
   # Returns: <StorageZone: example-a (id: 1234)>

Storage Files
^^^^^^^^^^^^^

.. code:: python

   # Get a Storage Zone
   zone = b.StorageZone.get(1234)
   # Returns: <StorageZone: example-a (id: 1234)>

   # Lists files in the zone
   obj_list = zone.all()
   # Returns [<StorageFile: index.html>, <StorageFile: base.css>]

   # Get a file
   obj = zone.get('index.html')
   #Returns <StorageFile: index.html>

   # Get a file as StorageObject
   zone = b.Storage.get_object(1234)
   # Returns: <StorageObject: example-a (id: 1234)>

   # Download that File
   obj.download()

   # Delete a file
   zone.delete_file('index.html')

   # Upload a File
   zone.upload_file(dest_path='folder/path/', file_name='error.html', local_path='/home/mj/work/')
   # Returns: <StorageFile: error.html>

   # Create a file from a string
   zone.create_file('base.css', "body {background-color: powderblue;}")
   # Returns: <StorageFile: base.css>

Storage JSON Files
^^^^^^^^^^^^^^^^^^

.. code:: python


   # Create a json file
   mj = zone.create_json('23.json', {'first_name':'Michael', 'last_name': 'Jordan'})
   # Returns <StorageJSONFile: 23.json>

   # Get information from file
   mj['first_name']
   # Returns: 'Michael'

