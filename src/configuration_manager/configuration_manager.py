# configuration_manager.py

# Author : aarontillekeratne
# Date : 13/10/19

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

from google.appengine.api import app_identity
from enum import Enum
import yaml


class Environment(Enum):
    DEV = 0
    TEST = 1
    PROD = 99


str_to_env = {"dev": Environment.DEV, "test": Environment.TEST,
              "prod": Environment.PROD}
env_to_str = {Environment.DEV: "dev", Environment.TEST: "test",
              Environment.PROD: "prod"}


class ConfigurationManager:

    def __init__(self, config_file_path):
        self.cfg_file_path = config_file_path
        self.app_id = app_identity.get_application_id()

    @staticmethod
    def _get_current_environment(app_id):
        """
        Get's the current environment by parsing the application id.
        :return:
        """
        return str_to_env[app_id.split('-')[0]]

    @staticmethod
    def _load_configuration_file(file_path):
        """
        Loads the raw configuration file.
        :param file_path:
        :return:
        """
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)

    @staticmethod
    def _load_config_for_environment(full_cfg, cur_env):
        """
        Loads the configuration for the environment in question.
        :param full_cfg:
        :param cur_env:
        :return:
        """
        return full_cfg[env_to_str[cur_env]]

    def get_app_configuration(self):
        """
        Returns the application configuration.
        :return:

        """
        cur_env = self._get_current_environment(self.app_id)
        full_cfg = self._load_configuration_file(
            self.cfg_file_path)

        return self._load_config_for_environment(full_cfg, cur_env)
