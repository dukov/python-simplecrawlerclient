# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging

from cliff.lister import Lister

from crawlerclient.http_client import HTTPClient
from crawlerclient.utils import transform_to_cliff_list

class BaseLister(Lister):

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.client = HTTPClient(self.app_args.host,
                self.app_args.port, proto=self.app_args.proto)
