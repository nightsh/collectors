# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB
from alembic import op


# revision identifiers, used by Alembic.
revision = '0eb08182bd23'
down_revision = '0087dc1eb534'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('data_contributions',
        sa.Column('id', UUID, primary_key=True),
        sa.Column('meta_created', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('meta_updated', sa.DateTime(timezone=True), server_default=sa.text('now()')),

        sa.Column('user_id', UUID),
        sa.Column('trial_id', UUID),
        sa.Column('category_id', sa.Text),

        sa.Column('url', sa.Text),
        sa.Column('file_url', sa.Text),

        sa.Column('contribution_comments', sa.Text),
        sa.Column('curation_comments', sa.Text),

    )


def downgrade():
    op.drop_table('data_contributions')
