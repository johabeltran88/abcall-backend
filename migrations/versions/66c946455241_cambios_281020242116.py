"""Cambios 281020242116

Revision ID: 66c946455241
Revises: 7235debd209c
Create Date: 2024-10-28 21:48:35.648644

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '66c946455241'
down_revision = '7235debd209c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pccs',
    sa.Column('subject', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('consumer_id', sa.String(length=36), nullable=False),
    sa.Column('company_id', sa.String(length=36), nullable=True),
    sa.Column('agent_id', sa.String(length=36), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['agent_id'], ['agents.id'], ),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['consumer_id'], ['consumers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pcss')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pcss',
    sa.Column('subject', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('consumer_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('company_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('agent_id', sa.VARCHAR(length=36), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['agent_id'], ['agents.id'], name='pcss_agent_id_fkey'),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name='pcss_company_id_fkey'),
    sa.ForeignKeyConstraint(['consumer_id'], ['consumers.id'], name='pcss_consumer_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='pcss_pkey')
    )
    op.drop_table('pccs')
    # ### end Alembic commands ###