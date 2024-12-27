"""update created on post table

Revision ID: 14aeaf9a446f
Revises: 37462bc78cd6
Create Date: 2024-12-27 20:50:49.345711

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14aeaf9a446f'
down_revision: Union[str, None] = '37462bc78cd6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('posts', 'created_at',existing_type=sa.DateTime, type_=sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()"),
                    postgresql_using="created_at::TIMESTAMP")
    pass


def downgrade() -> None:
    op.alter_column(
        'posts',
        'owner_id',
        existing_type=sa.DateTime,
        type_=sa.DateTime,
        postgresql_using="owner_id::text"
    )
    pass
