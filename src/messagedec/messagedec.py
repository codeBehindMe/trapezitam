# messagedec.py

# Author : aarontillekeratne
# Date : 22/9/19

# This file is part of ingtrec.

# ingtrec is free software:
# you can redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.

# ingtrec is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with ingtrec.  
# If not, see <https://www.gnu.org/licenses/>.

# Message deconstructor

from bs4 import BeautifulSoup

START_STRING_SEARCH_TOKEN = 'spent'
END_STRING_SEARCH_TOKEN = '\n'


def heuristic_string_subsetter(string):
    """
    Uses keywords to subset the string of interest.
    :param string:
    :return:
    """
    start_pos = string.find(START_STRING_SEARCH_TOKEN)
    end_pos = string[start_pos:].find(END_STRING_SEARCH_TOKEN)

    return string[start_pos:start_pos + end_pos]


class MessageDeconstructor(object):

    def __init__(self, html_email_body):
        self.soup = html_email_body
        self.soup_string = str(self.soup).lower()

    def get_string_of_interest(self):
        """
        Gets the subset of the entire html string that usually comes with the
        email body.
        :return:
        """

        return heuristic_string_subsetter(self.soup_string)
