"""empty message

Revision ID: e6a938e6c7ce
Revises: 2a83154f04bc
Create Date: 2024-01-07 21:34:59.525002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6a938e6c7ce'
down_revision = '2a83154f04bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=250),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=150),
               existing_nullable=False)

    # ### end Alembic commands ###