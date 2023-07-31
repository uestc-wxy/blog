"""empty message

Revision ID: b438f2aef1de
Revises: 444d20c9eebb
Create Date: 2020-06-11 11:51:39.811931

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b438f2aef1de'
down_revision = '444d20c9eebb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reply',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('content', sa.String(length=255), nullable=False),
    sa.Column('love_num', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['comment.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('news', 'desc',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('news', 'desc',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.drop_table('reply')
    # ### end Alembic commands ###
