# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
from .parser import parse_record
logger = logging.getLogger(__name__)


def collect(conf, conn):

    #TODO: We have to somehow manage the case when a contribution get rejected after
    #      being approved and collected.
    #      Not sure it's a valid use case though, so we're not checking now.

    explorer_table = conn['explorer']['data_contributions']
    count = 0

    collected = []
    for existing in conn['warehouse']['data_contributions']:
        collected.append(existing['id'])

    for contribution in explorer_table.find(approved=True):
        if contribution['id'] not in collected:
            record = parse_record(contribution)
            record.write(conf, conn)
            count+=1

    logger.info('Collected %s contributions', count)
