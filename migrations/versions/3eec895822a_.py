"""
Adding rich user info

Revision ID: 3eec895822a
Revises: ceed5dbf831
Create Date: 2014-11-09 15:58:32.457559

"""

# revision identifiers, used by Alembic.
revision = '3eec895822a'
down_revision = 'ceed5dbf831'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY


def upgrade():
    op.drop_column('users', 'username')

    op.alter_column('id','user_id')

    op.add_column('users', sa.Column('fbid',sa.BigInteger, primary_key=True))
    op.add_column('users', sa.Column('first_name', sa.String(80), nullable=False))
    op.add_column('users', sa.Column('last_name', sa.String(80), nullable=False))
    op.add_column('users', sa.Column('bio', sa.Text()))
    op.add_column('users', sa.Column('gender',sa.String(20)))
    op.add_column('users', sa.Column('relationship_status', sa.String(20)))
    op.add_column('users', sa.Column('interested_in', ARRAY(sa.String(20))))
    op.add_column('users', sa.Column('last_short_token', sa.String(250)))
    op.add_column('users', sa.Column('last_long_token', sa.String(250)))
    op.add_column('users', sa.Column('account_status', db.String(20)))

def downgrade():
    op.drop_column('users', 'fbid')
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'bio')
    op.drop_column('users', 'gender')
    op.drop_column('users', 'relationship_status')
    op.drop_column('users', 'interested_in')
    op.drop_column('users', 'last_long_token')
    op.drop_column('users', 'last_short_token')
    op.drop_column('users', 'account_status')

    op.add_column('users', sa.Column('username', sa.String(80), unique=True))