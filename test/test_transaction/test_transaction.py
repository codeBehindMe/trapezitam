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

from src.net.http import post
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


@pytest.mark.usefixtures('app_config')
class TestTransaction:

    def test_validate(self, app_config):
        """
        Test to see if validation works.
        # FIXME: Ill defined test.
        :return:
        """
        res = post(app_config['gtfurl'], )
