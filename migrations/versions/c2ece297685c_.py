"""empty message

Revision ID: c2ece297685c
Revises: 05a8379f3393
Create Date: 2020-06-01 11:57:05.841847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2ece297685c'
down_revision = '05a8379f3393'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'document', 'document', ['parent_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'document', type_='foreignkey')
    # ### end Alembic commands ###
