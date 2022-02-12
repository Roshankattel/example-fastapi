"""add some columns to posts table

Revision ID: 3300ecfddd50
Revises: babc3c8c732e
Create Date: 2022-02-12 21:28:18.962427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3300ecfddd50'
down_revision = 'babc3c8c732e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column(('created_at'), sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
