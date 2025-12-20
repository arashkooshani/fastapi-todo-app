"""created user relations

Revision ID: 99ca61cdbca2
Revises: 145440dd06b8
Create Date: 2025-12-20 10:56:23.953328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99ca61cdbca2'
down_revision: Union[str, Sequence[str], None] = '145440dd06b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table('tasks') as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_tasks_user_id_users',
            'users',
            ['user_id'],
            ['id']
        )


def downgrade():
    with op.batch_alter_table('tasks') as batch_op:
        batch_op.drop_constraint('fk_tasks_user_id_users', type_='foreignkey')
        batch_op.drop_column('user_id')
