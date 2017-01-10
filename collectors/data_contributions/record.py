# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Json


class Record(base.Record):
    table = 'data_contributions'

    # Fields

    id = Text(primary_key=True)
    user_id = Text()
    trial_id = Text()
    category_id = Text()
    url = Text()
    file_url = Text()
    contribution_comments = Text()
    curation_comments = Text()
