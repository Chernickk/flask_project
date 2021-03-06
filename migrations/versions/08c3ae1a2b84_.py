"""empty message

Revision ID: 08c3ae1a2b84
Revises: 4143e5301d11
Create Date: 2021-04-21 15:38:33.051173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08c3ae1a2b84'
down_revision = '4143e5301d11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friend_request',
    sa.Column('initiator_id', sa.Integer(), nullable=False),
    sa.Column('target_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('requested', 'approved', 'rejected', name='status'), nullable=True),
    sa.Column('requested_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['initiator_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['target_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('initiator_id', 'target_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('friend_request')
    # ### end Alembic commands ###
