"""rename department

Revision ID: e3616a262877
Revises: a425dd58374a
Create Date: 2025-02-12 21:16:19.034421

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'e3616a262877'
down_revision = 'a425dd58374a'
branch_labels = None
depends_on = None


def upgrade():
    # Rename the table from 'department' to 'departments'
    op.rename_table('department', 'departments')


def downgrade():
    # Rename it back from 'departments' to 'department' if needed
    op.rename_table('departments', 'department')
