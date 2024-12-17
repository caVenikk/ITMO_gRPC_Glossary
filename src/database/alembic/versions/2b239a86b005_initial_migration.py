"""Initial migration

Revision ID: 2b239a86b005
Revises: 
Create Date: 2024-12-17 16:48:15.464984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b239a86b005'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('glossary_terms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('term', sa.String(length=255), nullable=False),
    sa.Column('definition', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('glossary_terms')
    # ### end Alembic commands ###
