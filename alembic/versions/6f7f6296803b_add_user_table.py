"""add user table

Revision ID: 6f7f6296803b
Revises: f699b054d6c9
Create Date: 2022-08-12 10:19:58.805489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f7f6296803b'
down_revision = 'f699b054d6c9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')   )
    pass


def downgrade():
    op.drop_table('users')
    pass
