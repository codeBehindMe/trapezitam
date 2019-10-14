# misc.py

# Author : aarontillekeratne
# Date : 14/10/19

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

import unicodedata


# FIXME: This function isn't doing what it's saying.
def unicode_to_utf8_safe(uc_str):
    """
    Converts the strings from unicode to utf8.
    :param uc_str:
    :return:
    """
    # Replace xa0

    uc_str = unicodedata.normalize('NFKC', uc_str)

    return str(uc_str)
