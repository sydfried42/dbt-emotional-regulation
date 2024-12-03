"""test

Revision ID: 8fa9674edbdf
Revises: 
Create Date: 2024-12-03 14:54:10.517658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fa9674edbdf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('biologies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('test', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('biologies', schema=None) as batch_op:
        batch_op.drop_column('test')

    # ### end Alembic commands ###