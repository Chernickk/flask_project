"""some changes

Revision ID: 09a7f2a6688b
Revises: 9032b586ceda
Create Date: 2021-04-15 12:43:35.024472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09a7f2a6688b'
down_revision = '9032b586ceda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('media', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'media', 'user', ['user_id'], ['id'])
    op.add_column('profile', sa.Column('photo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'profile', 'media', ['photo_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'profile', type_='foreignkey')
    op.drop_column('profile', 'photo_id')
    op.drop_constraint(None, 'media', type_='foreignkey')
    op.drop_column('media', 'user_id')
    # ### end Alembic commands ###
