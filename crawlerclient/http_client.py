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

import json
import logging
import requests

class HTTPClient(object):

    def __init__(self, host, port, proto='http'):
        self.host = host
        self.port = port
        self.proto = proto
        self.root = "{0}://{1}:{2}/".format(proto, host, port)

    def get(self, path):
        r = requests.get(self.root + path)
        return r.json()

    def post(self, path, data):
        r = requests.post(self.root + path, data=data)
        return r.text

    def get_status(self):
        return self.get('status')

    def get_agents(self):
        return self.get('agents')

    def post_job(self, job_data):
        return self.post('jobs', json.dumps(job_data))
