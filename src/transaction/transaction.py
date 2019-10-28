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


def from_dictionary(d):
    def wrapper():
        return d


class Transaction:

    def __init__(self, *args, **kwargs):
        self.d = args[0]()

    def validate(self):
        """
        Make sure it's a valid transaction.
        :return:
        """
        pass
