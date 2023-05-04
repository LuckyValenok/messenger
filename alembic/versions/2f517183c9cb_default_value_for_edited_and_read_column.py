"""default value for edited and read column

Revision ID: 2f517183c9cb
Revises: 4f5614ced868
Create Date: 2023-05-04 10:44:16.381273

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2f517183c9cb'
down_revision = '4f5614ced868'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('messages', 'edited', False, default=False)
    op.alter_column('messages', 'read', False, default=False)


def downgrade():
    op.alter_column('messages', 'edited', True, default=None)
    op.alter_column('messages', 'read', True, default=None)
