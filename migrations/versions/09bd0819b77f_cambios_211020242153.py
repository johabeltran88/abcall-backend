"""Cambios 211020242153

Revision ID: 09bd0819b77f
Revises: 042c06e2be61
Create Date: 2024-10-21 21:53:38.489035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09bd0819b77f'
down_revision = '042c06e2be61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pcss',
    sa.Column('subject', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('consumer_id', sa.String(), nullable=False),
    sa.Column('company_id', sa.String(), nullable=True),
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['consumer_id'], ['consumers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pcss')
    # ### end Alembic commands ###