"""Renaming students to scholars

Revision ID: 736dfc8fad56
Revises: 791279dd0760
Create Date: 2025-06-04 08:35:43.995826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '736dfc8fad56'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('students', 'name', new_column_name='full_name')

def downgrade():
    op.alter_column('students', 'full_name', new_column_name='name')