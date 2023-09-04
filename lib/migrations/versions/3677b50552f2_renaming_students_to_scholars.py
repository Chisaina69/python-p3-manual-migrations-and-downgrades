"""Renaming students to scholars

Revision ID: 3677b50552f2
Revises: 791279dd0760
Create Date: 2023-09-04 11:13:23.758049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3677b50552f2'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
