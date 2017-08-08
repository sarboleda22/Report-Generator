import os
import json


# the configuration defaults to the ./development directory
_configuration_directory = os.environ.get('CONFIG', 'development')


class Configuration(dict):
    def __init__(self, file_name, *args, **kw):
        # call the super __init__ to initialize the dictionary
        super(Configuration, self).__init__(*args, **kw)
        """
        If _configuration_directory/file_name exists, load the configuration
        from it and populate this object with the loaded data
        """
        loaded_config = {}
        try:
            loaded_config = json.load(
                open("etc/config/{directory}/{file_name}".format(
                    directory=_configuration_directory,
                    file_name=file_name
                )))
        except FileNotFoundError:
            loaded_config = json.load(
                open("etc/config/default/{file_name}".format(file_name=file_name)))

        for key, val in loaded_config.items():
            self[key] = val

credentials = Configuration("credentials.config.json")
database_server = Configuration("database.server.config.json")

