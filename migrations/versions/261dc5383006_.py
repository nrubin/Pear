"""empty message

Revision ID: 261dc5383006
Revises: 3eec895822a
Create Date: 2014-11-24 21:35:25.393114

"""

# revision identifiers, used by Alembic.
revision = '261dc5383006'
down_revision = '3eec895822a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSON as psql_json
from sqlalchemy.dialects.postgresql import ARRAY as psql_array

"""
		sa.Column('id', sa.Integer, primary_key=True),
 		sa.Column('username', sa.String(80), unique=True),
 		sa.Column('email', sa.String(120), unique=True)
"""

def upgrade():
    op.create_table(
    	'activities',
	     sa.Column('activity_id',sa.Integer, primary_key=True),
	     sa.Column('name',sa.String(80), nullable=False),
	     sa.Column('description',sa.Text(), nullable=False),
	     sa.Column('duration',sa.BigInteger) ,
	     sa.Column('difficulty',sa.String(80)),
	     sa.Column('pricing',psql_json),
	     sa.Column('schedule',psql_array(sa.DateTime(timezone=False)))
    )


def downgrade():
    op.drop_table('activities')
