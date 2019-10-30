# test_transaction.py

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

from src.transaction.transaction import Transaction
from src.transaction.transaction import from_json_string
from src.transaction.transaction import from_dictionary
import pytest
import yaml


@pytest.fixture(scope='class')
def app_config():
    with open('app_config.yaml', 'r') as f:
        cfg = yaml.safe_load(f)
    yield cfg['dev']


@pytest.fixture(scope='class')
def data():
    yield {"TransactionVersion": "transactionv3",
           "Location": "Home", "Amount": "$10.00", "NumericAmount": 10.00,
           "TxNotifyUnixEpoch": 1231231}


@pytest.fixture(scope='module')
def post_result():
    yield '{"TransactionVersion":"transactionv3","Location":"home","Amount":"$10","NumericAmount":10,"TxNotifyUnixEpoch":1572256352}\n'


@pytest.mark.usefixtures('app_config')
class TestTransaction:

    def test_from_json_string(self, post_result):
        expected = {u"TransactionVersion": u"transactionv3",
                    u"Location": u"home", u"Amount": u"$10",
                    u"NumericAmount": 10, u"TxNotifyUnixEpoch": 1572256352}
        assert from_json_string(post_result)() == expected

    def test_transacion_is_invalid_when_two_keys_are_null(self):
        """
        Test to see if validation works.
        # FIXME: Ill defined test.
        :return:
        """
        test_dict = {"TransactionVersion": "transactionv3",
           "Location": "", "Amount": "", "NumericAmount": 10.00,
           "TxNotifyUnixEpoch": 1231231}

        with pytest.raises(ValueError):
            Transaction(from_dictionary(test_dict)).validate()
