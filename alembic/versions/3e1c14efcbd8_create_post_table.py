"""create post table

Revision ID: 3e1c14efcbd8
Revises: 
Create Date: 2022-08-12 09:59:34.166391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e1c14efcbd8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
    sa.Column('title',sa.String(), nullable = False ))
    pass


def downgrade():
    op.drop_table('posts')
    pass
