"""add content to posts table

Revision ID: f19a76220f40
Revises: c7d869e747b8
Create Date: 2024-12-27 15:43:02.481300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f19a76220f40'
down_revision: Union[str, None] = 'c7d869e747b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
