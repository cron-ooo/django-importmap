django-importmap
=====

Django-importmap is a dependency to dynamically import modules.


Quick start
-----------

1. Add "importmap" to your ``INSTALLED_APPS`` setting like this:
```
    INSTALLED_APPS = [
        ...
        'polls',
    ]
 ```

2. Add variable ``IMPORTMAP_FILE_PATH`` with the path to the file with imports to your ``settings.py`` module: 

    ```
    IMPORTMAP_FILE_PATH = os.path.join(BASE_DIR, 'importmap.importmap')
    ```
