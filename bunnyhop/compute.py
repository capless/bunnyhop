from bunnyhop.base import APIKeyRecord, Record


class ScriptSet(Record):
    """
    A set of scripts.
    Attributes:
        objects (list): A list of Script objects.
        current_page (int): The current page.
        total_items (int): The total number of items.
        has_more_items (bool): Whether there are more items.
    """
    pass


class Script(APIKeyRecord):
    def __init__(self, api_key: str, data: dict):
        """
        Script constructor.
        Args:
            api_key (str): BunnyCDN's API key.
            data (dict): A dict representation of a script.
        """
        super().__init__(api_key, data)
        # Convert the script variables to ScriptVariable objects.
        self.edge_script_variables = ScriptVariableSet(
            {'objects': [ScriptVariable(api_key, v) for v in self.edge_script_variables]})

    def __repr__(self):
        """Return a string representation of the Script object.

        Returns:
            A string representation of the Script object.
        """
        return f"<Script {self.name}>"

    def publish(self, uuid: str, note: str = None):
        """Publish the script.
        """
        params = {
            'Note': note
        }

        path = f'/compute/script/{self.id}/publish/{self.uuid}'
        self.__dict__.update(self._make_request('POST', path, json=params))


class ScriptVariableSet(Record):
    """
    A set of script variables.
    Attributes:
        objects (list): A list of ScriptVariable objects.
    """
    pass


class ScriptVariable(APIKeyRecord):

    def create(self, name: str, required: bool = False, default: str = None):
        """
        Create a script variable.
        Args:
            name (str): The name of the variable.
            required (bool, optional): Whether the variable is required. Defaults to False.
            default (str, optional): The default value of the variable. Defaults to None.
        """
        params = {
            'Name': name,
            'Required': required,
            'DefaultValue': default,
        }
        path = f'/compute/script/{self.id}/variables/add'
        data = self._make_request('POST', path, json=params)
        self.__dict__.update(data)

    def update(self, name: str, variable_id: int, required: bool = False, default: str = None):
        """
        Update a script variable.
        Args:
            name (str): The name of the variable.
            variable_id (int): The ID of the variable.
            required (bool, optional): Whether the variable is required. Defaults to False.
            default (str, optional): The default value of the variable. Defaults to None.
        """
        params = {
            'Name': name,
            'Required': required,
            'DefaultValue': default,
        }
        path = f'/compute/script/{self.id}/variables/{variable_id}'
        data = self._make_request('POST', path, json=params)
        self.__dict__.update(data)

    def get(self, variable_id: int):
        """
        Get a script variable.
        Args:
            variable_id (int): The ID of the variable.
        """
        path = f'/compute/script/{self.id}/variables/{variable_id}'
        data = self._make_request('GET', path)
        self.__dict__.update(data)

    def delete(self, variable_id: int):
        """
        Delete a script variable.
        Args:
            variable_id (int): The ID of the variable.
        """
        path = f'/compute/script/{self.id}/variables/{variable_id}'
        data = self._make_request('DELETE', path)
        self.__dict__.update(data)


class ScriptCode(APIKeyRecord):

    def __repr__(self):
        """Return a string representation of the ScriptCode object.

        Returns:
            A string representation of the ScriptCode object.
        """
        return f"<ScriptCode {self.name}>"

    def get(self):
        """Get the script code.

        Returns:
            A string containing the script code.
        """
        path = f'/compute/script/{self.id}/code'
        data = self._make_request('GET', path)
        self.__dict__.update(data)

    def update(self, code: str):
        """Update the script code.

        Args:
            code (str): The script code.
        """
        path = f'/compute/script/{self.id}/code'
        data = self._make_request('POST', path, json={'Code': code})
        self.__dict__.update(data)


class ScriptReleaseSet(Record):
    pass


class ScriptRelease(APIKeyRecord):

    def list(self, id: int, page: int = 1, per_page: int = 100):
        """List all script releases.

        Args:
            id (int): The ID of the script.
            page (int, optional): The page number to get. Defaults to 1.
            per_page (int, optional): The number of releases to get per page. Defaults to 100.

        Returns:
            A ScriptReleaseSet object.
        """
        params = {
            'page': page,
            'perPage': per_page,
        }
        path = f'/compute/script/{id}/releases'
        data = self._make_request('GET', path, params=params)
        data['objects'] = [ScriptRelease(self.api_key, release) for release in data.get('Items', [])]
        data.pop('Items')
        return ScriptReleaseSet(data)


class Compute(APIKeyRecord):

    def list_scripts(self, page: int = 1, per_page: int = 100, search: str = None):
        """List all compute scripts.
        Args:
            page (int, optional): The page number to get. Defaults to 1.
            per_page (int, optional): The number of scripts to get per page. Defaults to 100.
            search (str, optional): A search term to filter the scripts by. Defaults to None.
        Returns:
            A ScriptSet object.

        """
        params = {
            'page': page,
            'perPage': per_page,
            'search': search,
        }
        path = '/compute/script'
        data = self._make_request('GET', path, params=params)
        data['objects'] = [Script(self.api_key, script) for script in data.get('Items', [])]
        data.pop('Items')
        return ScriptSet(data)

    def create_script(self, name: str, script_type: int = 0):
        """
        Create a compute script.

        Args:
            name (str): The name of the script.
            script_type (int, optional): The script type. Defaults to 0.
        Returns:
            A Script object.
        """
        params = {
            'Name': name,
            'ScriptType': script_type,
        }
        path = '/compute/script'
        data = self._make_request('POST', path, json=params)
        return Script(self.api_key, data)

    def get_script(self, script_id: int):
        """Get a compute script.

        Args:
            script_id (int): The ID of the script.

        Returns:
            A Script object.
        """
        path = f'/compute/script/{script_id}'
        data = self._make_request('GET', path)
        return Script(self.api_key, data)

    def update_script(self, script_id: int, name: str, script_type: int = 0):
        """Update a compute script.

        Args:
            script_id (int): The ID of the script.
            name (str): The name of the script.
            script_type (int, optional): The script type. Defaults to 0.

        Returns:
            A Script object.
        """
        params = {
            'Name': name,
            'ScriptType': script_type,
        }
        path = f'/compute/script/{script_id}'
        data = self._make_request('POST', path, json=params)
        return Script(self.api_key, data)

    def delete_script(self, script_id: int):
        """Delete a compute script.

        Args:
            script_id (int): The ID of the script.
        """
        path = f'/compute/script/{script_id}'
        self._make_request('DELETE', path)

    def get_script_code(self, script_id: int):
        """Get the code of a compute script.

        Args:
            script_id (int): The ID of the script.

        Returns:
            A string containing the script code.
        """
        sc = ScriptCode(self.api_key, {'Id': script_id})
        sc.get()
        return sc

    def update_script_code(self, script_id: int, code: str):
        """Update the code of a compute script.

        Args:
            script_id (int): The ID of the script.
            code (str): The script code.
        """
        sc = ScriptCode(self.api_key, {'Id': script_id})
        sc.update(code)
        return sc

    def list_script_releases(self, script_id: int, page: int = 1, per_page: int = 100):
        """List all script releases.

        Args:
            script_id (int): The ID of the script.
            page (int, optional): The page number to get. Defaults to 1.
            per_page (int, optional): The number of releases to get per page. Defaults to 100.

        Returns:
            A ScriptReleaseSet object.
        """
        sr = ScriptRelease(self.api_key, {'Id': script_id})
        return sr.list(script_id, page, per_page)

    def publish_script(self, script_id: int, uuid: str, note: str):
        """Publish a script release.

        Args:
            script_id (int): The ID of the script.
            uuid (str): The UUID of the release.
            note (str): The release note.

        Returns:
            A ScriptRelease object.
        """
        script = Script(self.api_key, {'Id': script_id})
        script.publish(uuid, note)
        return script

    def create_script_variable(self, script_id: int, name: str, required: bool, default_value: str = None):
        """Create a script variable.

        Args:
            script_id (int): The ID of the script.
            name (str): The name of the variable.
            variable_type (int): The variable type.
            default_value (str, optional): The default value of the variable. Defaults to None.

        Returns:
            A ScriptVariable object.
        """
        sv = ScriptVariable(self.api_key, {'Id': script_id})
        sv.create(script_id, name, required, default_value)
        return sv

    def update_script_variable(self, script_id: int, variable_id: int, name: str, required: bool,
                               default_value: str = None):
        """Update a script variable.

        Args:
            script_id (int): The ID of the script.
            variable_id (int): The ID of the variable.
            name (str): The name of the variable.
            variable_type (int): The variable type.
            default_value (str, optional): The default value of the variable. Defaults to None.

        Returns:
            A ScriptVariable object.
        """
        sv = ScriptVariable(self.api_key, {'Id': script_id})
        sv.update(script_id, variable_id, name, required, default_value)
        return sv

    def delete_script_variable(self, script_id: int, variable_id: int):
        """Delete a script variable.

        Args:
            script_id (int): The ID of the script.
            variable_id (int): The ID of the variable.
        """
        sv = ScriptVariable(self.api_key, {'Id': script_id})
        sv.delete(script_id, variable_id)
        return sv
