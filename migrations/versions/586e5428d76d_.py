"""empty message

Revision ID: 586e5428d76d
Revises: a6eaccaa4db0
Create Date: 2023-08-30 21:09:46.543951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '586e5428d76d'
down_revision = 'a6eaccaa4db0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###