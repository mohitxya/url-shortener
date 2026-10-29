"""alter sequence start value

Revision ID: 04177f9358c6
Revises: b9d62552178d
Create Date: 2026-10-29 12:42:59.031404

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04177f9358c6'
down_revision: Union[str, Sequence[str], None] = 'b9d62552178d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("TRUNCATE TABLE urls;")
    op.execute("ALTER SEQUENCE urls_id_seq RESTART WITH 1000000000;")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("ALTER SEQUENCE urls_id_seq RESTART WITH 1;")
