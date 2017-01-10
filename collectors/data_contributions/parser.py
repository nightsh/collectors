# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
from .record import Record
logger = logging.getLogger(__name__)


def parse_record(item):

    # Init data
    data = {}

    # Map data
    data['id'] = item['id']

    data['user_id'] = item['user_id']
    data['trial_id'] = item['trial_id']
    data['category_id'] = item['data_category_id']

    data['url'] = item['url']
    data['file_url'] = item['data_url']

    data['contribution_comments'] = item['comments']
    data['curation_comments'] = item['curation_comments']

    # Create record
    record = Record.create(None, data)

    return record
