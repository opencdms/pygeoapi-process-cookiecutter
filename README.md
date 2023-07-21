# About

Cookie cutter based on https://cookiecutter.readthedocs.io/en/stable/ to create a pygeoapi process.

# Usage

 ``
 cookiecutter gh:opencdms/pygeoapi-process-cookiecutter
 ``
 
When running using the cookiecutter the following are requested by the prompt:

- ``package_url``: The home page for the new package / pygeoapi process plugin.
- ``package_name``: The name of the new python package containing the process.
- ``process_id``: The id of the OGC-API process. This is used in the API path to access the process, e.g. https://example.com/processes/{process_id}
- ``process_class_name``: The name of the process class in the package. 
- ``process_description``: A short description of the process
- ``keywords``: A list of keywords
- ``license``: The licence to use for the process, defaults to APL2.

# Links

- https://docs.pygeoapi.io/en/latest/plugins.html#processing-plugins (PygeoAPI documentation)
- https://docs.ogc.org/is/18-062r2/18-062r2.html (The OGA_API processes standard) 
