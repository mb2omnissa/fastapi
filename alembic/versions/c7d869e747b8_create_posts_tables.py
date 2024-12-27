"""create posts tables

Revision ID: c7d869e747b8
Revises: 
Create Date: 2024-12-27 12:57:10.454794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7d869e747b8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts",sa.Column("id",sa.Integer,primary_key=True, nullable=False),
                    sa.Column("title",sa.String(255), nullable=False),
                    sa.Column("content",sa.Text(), nullable=False),
                    sa.Column("published",sa.Boolean,nullable=False),
                    sa.Column("created_at",sa.DateTime,nullable=False),)


def downgrade() -> None:
    op.drop_table("posts")
