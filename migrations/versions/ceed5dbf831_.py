"""
Adding basic user info

Revision ID: ceed5dbf831
Revises: None
Create Date: 2014-10-18 12:29:44.184253

"""

# revision identifiers, used by Alembic.
revision = 'ceed5dbf831'
down_revision = None

from alembic import op
import sqlalchemy as sa

def upgrade():
	op.create_table(
		'users',
		sa.Column('id', sa.Integer, primary_key=True),
 		sa.Column('username', sa.String(80), unique=True),
 		sa.Column('email', sa.String(120), unique=True)
	)

def downgrade():
    op.drop_table('users')
