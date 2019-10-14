# handle_incoming_mail.py

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

import logging
import urllib2

import webapp2
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from src.utils.misc import unicode_to_utf8_safe

from src.messagedec.messagedec import MessageDeconstructor
from src.configuration_manager.configuration_manager import \
    ConfigurationManager

APP_CONFIG_FILE_PATH = 'app_config.yaml'

app_config = ConfigurationManager(APP_CONFIG_FILE_PATH)


class HandleIncomingMail(InboundMailHandler):

    def receive(self, mail_message):
        logging.info("Received message from: " + mail_message.sender)

        html_bodies = mail_message.bodies('text')

        all_string = ""
        for _, b in html_bodies:
            all_string = all_string.join(unicode_to_utf8_safe(b.decode()))

        logging.debug("Received email with body:\n" + all_string)
        payload = MessageDeconstructor(all_string).get_string_of_interest()

        logging.info("Extracted payload: " + payload)


app = webapp2.WSGIApplication([HandleIncomingMail.mapping()], debug=True)
