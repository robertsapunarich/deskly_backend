"""create base models

Revision ID: 09e098ecd462
Revises: 
Create Date: 2024-06-26 13:11:06.001031

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09e098ecd462'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.MetaData(),
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("email", sa.String, unique=True, index=True),
        sa.Column("hashed_password", sa.String, nullable=False),
        sa.Column("type", sa.String, nullable=False),
    )
    

    op.create_table(
        "tasks",
        sa.MetaData(),
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String),
        sa.Column("priority", sa.String),
        sa.Column("status", sa.String, default="open"),
        sa.Column("assignee_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("customer_id", sa.Integer, sa.ForeignKey("users.id")),
    )

    op.create_table(
        "threads",
        sa.MetaData(),
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String),
        sa.Column("task_id", sa.Integer, sa.ForeignKey("tasks.id")),
    )

    op.create_table(
        "messages",
        sa.MetaData(),
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("thread_id", sa.Integer, sa.ForeignKey("threads.id")),
        sa.Column("body", sa.String),
        sa.Column("subject", sa.String),
    )


def downgrade() -> None:
    op.drop_table("messages")
    op.drop_table("threads")
    op.drop_table("tasks")
    op.drop_table("users")
