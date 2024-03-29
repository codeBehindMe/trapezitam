# cloud_function.py

# Author : aarontillekeratne
# Date : 2/11/19

# This file is part of trapezitam.

# trapezitam is free software:
# you can redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.

# trapezitam is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with trapezitam.  
# If not, see <https://www.gnu.org/licenses/>.

import requests
from google.appengine.ext import ndb
from src.logging_manager.logging_manager import app_logger

TOKEN_REQUEST_HEADER = {'Metadata-Flavour': 'Google'}
AUTH_REFERENCE_ID = "5194620877fd2a6cb2ea948682b171f5"


class SecKey(ndb.Model):
    AuthKey = ndb.StringProperty()
    KeyType = ndb.StringProperty()


class CloudFunctionFactory:

    def __init__(self, metadata_server_token_url, devshell_project_id):
        self.metadata_server_toke_url = metadata_server_token_url
        self.devshell_project_id = devshell_project_id

    def create_function(self, function_url):
        """
        Creates a new cloud function object.
        :param function_url: Url to the cloud function.
        :return:
        """
        return _CloudFunction(function_url, self.metadata_server_toke_url,
                              self.devshell_project_id)


class _CloudFunction:

    def __init__(self, function_url, metadata_server_token_url,
                 devshell_project_id):
        self.func_url = function_url
        self.metadata_server_token_url = metadata_server_token_url
        self.devshell_project_id = devshell_project_id

    def _create_auth_header(self):
        """
        Creates the authorisation header.
        :return:
        """


        return {"Authorization": "Bearer {0}".format(AUTH_REFERENCE_ID)}

    def __call__(self, payload, **kwargs):
        """
        Calls the cloud function
        :param args:
        :param payload:
        :param kwargs:
        :return:
        """

        response = requests.post(self.func_url, json=payload,
                                 headers=self._create_auth_header())
        if response.status_code != 200:
            raise ValueError("Error response {0}".format(response.content))
        return response
