"""empty message

Revision ID: 9a5728c7df84
Revises: e371c2fc2f9e
Create Date: 2021-04-23 17:12:29.748232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a5728c7df84'
down_revision = 'e371c2fc2f9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('followed_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], name='followers_followed_id_fkey'),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], name='followers_follower_id_fkey')
    )
    # ### end Alembic commands ###
