"""first commit

Revision ID: 6e20933e9ec0
Revises: 
Create Date: 2023-09-07 21:04:16.289704

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e20933e9ec0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=25), nullable=False),
    sa.Column('last_name', sa.String(length=25), nullable=True),
    sa.Column('username', sa.String(length=25), nullable=False),
    sa.Column('telegram_id', sa.Integer(), nullable=True),
    sa.Column('language_code', sa.String(length=5), nullable=False),
    sa.Column('is_premium', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('first_name'),
    sa.UniqueConstraint('telegram_id')
    )
    op.create_index(op.f('ix_User_id'), 'User', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_User_id'), table_name='User')
    op.drop_table('User')
    # ### end Alembic commands ###
