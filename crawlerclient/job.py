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

from crawlerclient.base import BaseLister
from crawlerclient.utils import transform_to_cliff_list

class Create(BaseLister):
    """Create crawler job
    """

    def get_parser(self, prog_name):
        parser = super(Create, self).get_parser(prog_name)
        parser.add_argument(
                '--start',
                type=str,
                required=True,
                help='Video ID to start from',
        )
        parser.add_argument(
                '--stop',
                type=str,
                required=True,
                help='Video ID to stop on',
        )
        parser.add_argument(
                '--batch',
                type=int,
                default=10,
                help='Number of videos to schedule per worker',
        )
        return parser

    def take_action(self, parsed_args):
        super(Create, self).take_action(parsed_args)
        task = {
            'vid1': parsed_args.start,
            'vid2': parsed_args.stop,
            'batch': parsed_args.batch,
        }
        data = [{'Result': self.client.post_job(task)}]
        return transform_to_cliff_list(data)
