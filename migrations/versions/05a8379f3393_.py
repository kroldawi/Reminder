"""empty message

Revision ID: 05a8379f3393
Revises: 8704062bfd77
Create Date: 2020-05-26 15:53:36.108966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05a8379f3393'
down_revision = '8704062bfd77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('thing', sa.Column('updated_ts', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('thing', 'updated_ts')
    # ### end Alembic commands ###
