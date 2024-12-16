"""empty message

Revision ID: cbad4dfe368d
Revises: 3e042ffb527c
Create Date: 2024-12-15 19:42:49.814836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbad4dfe368d'
down_revision = '3e042ffb527c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('workout_card', sa.String(length=2000), nullable=False),
    sa.Column('meal_card', sa.String(length=2000), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('pic')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pic', sa.VARCHAR(length=750), autoincrement=False, nullable=True))

    op.drop_table('Favorites')
    # ### end Alembic commands ###
