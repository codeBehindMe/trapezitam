# transaction.py

# Author : aarontillekeratne
# Date : 27/10/19

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

import json
from numbers import Number
from src.logging_manager.logging_manager import app_logger


def from_dictionary(d):
    def wrapper():
        return d

    return wrapper


def from_json_string(json_string):
    def wrapper():
        return json.loads(json_string)

    return wrapper


class Transaction:

    def __init__(self, getter, *args, **kwargs):
        self.d = getter()

    @staticmethod
    def _is_zero_value(obj):
        """
        Check's that the object is a zero value.

        Zero values are a check to see if the transactions fields has
        reasonable amounts. A zero value constitutes of a literal zero for
        number types or empty strings for string types.

        :param obj: object to check.
        :return: boolean indicated if it's a zero value or not.
        """
        if isinstance(obj, basestring):
            if len(obj) == 0:
                return True
        if isinstance(obj, Number):
            if obj == 0:
                return True
        return False

    def validate(self):
        """
        Make sure it's a valid transaction.
        :return:
        """
        if sum([self._is_zero_value(v) for _, v in self.d.iteritems()]) > 1:
            app_logger.error("Found two or more items with zero values")
            raise ValueError("Invalid transaction")

    def __str__(self):
        return str(self.d)
