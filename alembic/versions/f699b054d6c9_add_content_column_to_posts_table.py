"""add content column to posts table

Revision ID: f699b054d6c9
Revises: 3e1c14efcbd8
Create Date: 2022-08-12 10:12:18.724536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f699b054d6c9'
down_revision = '3e1c14efcbd8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
