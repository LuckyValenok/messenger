"""default value for deleted and removed column

Revision ID: 4f5614ced868
Revises: 8535d94fcdc9
Create Date: 2023-05-04 09:51:57.899072

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4f5614ced868'
down_revision = '8535d94fcdc9'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('users', 'deleted', False, default=False)
    op.alter_column('chats', 'removed', False, default=False)


def downgrade():
    op.alter_column('users', 'deleted', True, default=None)
    op.alter_column('chats', 'removed', True, default=None)
