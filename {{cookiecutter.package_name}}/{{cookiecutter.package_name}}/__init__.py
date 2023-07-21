###############################################################################
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
###############################################################################
__version__ = "0.0.1"

import logging
from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

LOGGER = logging.getLogger(__name__)

PROCESS_METADATA = {
    'version': '0.0.1',
    'id': '{{cookiecutter.process_id}}',
    'title': {
        'en': '{{cookiecutter.process_name}}',
    },
    'description': {
        'en': '{{cookiecutter.process_description}}',
    },
    'keywords': [],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://example.org/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'example_input': {
            'title': 'value',
            'description': 'Number to double',
            'schema': {
                'type': 'numeric'
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': []
        }
    },
    'outputs': { },
    'example': {
        'inputs': {
            "value": 5
        },
        'outputs':{
            "result": 10
        }
    }
}


class {{cookiecutter.process_name}}(BaseProcessor):

    def __init__(self, processor_def):
        """
        Initialize object
        :param processor_def: provider definition
        :returns: pygeoapi.process.{{cookiecutter.process_id}}.{{cookiecutter.process_name}}
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):
        mimetype = 'application/json'
        value = data.get("example_input", None)
        output = {
            "result": value*2
        }
        return mimetype, output


    def __repr__(self):
        return '<{{cookiecutter.process_name}}> {}'.format(self.name)