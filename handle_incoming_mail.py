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

from src.logging_manager.logging_manager import app_logger
from src.net.http import post

import webapp2
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from src.utils.misc import unicode_to_utf8_safe

from src.messagedec.messagedec import MessageDeconstructor
from src.configuration_manager.configuration_manager import \
    ConfigurationManager

from src.transaction.transaction import Transaction
from src.transaction.transaction import from_json_string

APP_CONFIG_FILE_PATH = 'app_config.yaml'

app_config = ConfigurationManager(APP_CONFIG_FILE_PATH).get_app_configuration()


class HandleIncomingMail(InboundMailHandler):

    def receive(self, mail_message):
        app_logger.info("Received message from: " + mail_message.sender)

        html_bodies = mail_message.bodies('text')

        all_string = ""
        for _, b in html_bodies:
            all_string = all_string.join(unicode_to_utf8_safe(b.decode()))
        app_logger.debug("Received email with body:\n" + all_string)

        app_logger.info("Extracting transaction text from email.")
        t_text = MessageDeconstructor(all_string).get_string_of_interest()
        app_logger.debug("Extracted payload: " + t_text)

        payload = {"TransactionText": t_text}
        app_logger.info("Sending transaction text for entity extraction")

        gt_func_url = app_config['gtfurl']
        app_logger.debug(
            "Sending payload: " + gt_func_url)

        tx_o = post(gt_func_url, payload)
        app_logger.debug("Received response: " + str(tx_o))

        t = Transaction(from_json_string(tx_o))
        app_logger.debug("Validating transaction object")

        try:
            t.validate()
        except ValueError as v:
            app_logger.error("Invalid transaction")
            raise v


app = webapp2.WSGIApplication([HandleIncomingMail.mapping()], debug=True)
