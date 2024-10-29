"""Cambios 211020242200

Revision ID: 60939b02ef93
Revises: 09bd0819b77f
Create Date: 2024-10-21 22:00:58.195467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60939b02ef93'
down_revision = '09bd0819b77f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pcss', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pcss', schema=None) as batch_op:
        batch_op.drop_column('status')

    # ### end Alembic commands ###