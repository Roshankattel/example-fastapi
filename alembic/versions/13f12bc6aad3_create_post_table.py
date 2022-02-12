"""create post table

Revision ID: 13f12bc6aad3
Revises: 
Create Date: 2022-02-11 17:03:18.707586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13f12bc6aad3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(),  nullable=False,
                    primary_key=True), sa.Column('title', sa.String(),  nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
