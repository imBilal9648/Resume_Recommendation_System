"""empty message

Revision ID: 74f37cc50650
Revises: 646e83a85128
Create Date: 2021-05-27 19:01:37.093483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74f37cc50650'
down_revision = '646e83a85128'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job_description', sa.Column('keywords', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job_description', 'keywords')
    # ### end Alembic commands ###
