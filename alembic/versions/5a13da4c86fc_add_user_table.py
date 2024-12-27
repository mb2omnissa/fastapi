"""add user table

Revision ID: 5a13da4c86fc
Revises: f19a76220f40
Create Date: 2024-12-27 15:49:41.078021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a13da4c86fc'
down_revision: Union[str, None] = 'f19a76220f40'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id', name='user_pk'),
                    sa.UniqueConstraint('email', name='user_email'),
                    )


def downgrade() -> None:
    op.drop_table('users')
    pass
