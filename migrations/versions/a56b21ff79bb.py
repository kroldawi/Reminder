"""first one

Revision ID: a56b21ff79bb
Revises: 
Create Date: 2020-05-21 11:30:36.934671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a56b21ff79bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ts', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('when', sa.Date(), nullable=True),
    sa.Column('recurring', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ts', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('thing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ts', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag_event_assoc',
    sa.Column('tag', sa.Integer(), nullable=True),
    sa.Column('event', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event'], ['event.id'], ),
    sa.ForeignKeyConstraint(['tag'], ['tag.id'], )
    )
    op.create_table('tag_thing_assoc',
    sa.Column('tag', sa.Integer(), nullable=True),
    sa.Column('thing', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tag'], ['tag.id'], ),
    sa.ForeignKeyConstraint(['thing'], ['thing.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag_thing_assoc')
    op.drop_table('tag_event_assoc')
    op.drop_table('thing')
    op.drop_table('tag')
    op.drop_table('event')
    # ### end Alembic commands ###