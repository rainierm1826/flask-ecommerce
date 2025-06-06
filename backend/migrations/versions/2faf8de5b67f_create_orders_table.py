"""Create orders table

Revision ID: 2faf8de5b67f
Revises: 
Create Date: 2025-03-31 11:32:54.733758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2faf8de5b67f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('oid', sa.String(length=36), nullable=False),
    sa.Column('uid', sa.String(length=36), nullable=False),
    sa.Column('pid', sa.String(length=36), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['pid'], ['product.pid'], ),
    sa.ForeignKeyConstraint(['uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('oid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    # ### end Alembic commands ###
