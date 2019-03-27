"""new fields in user model

Revision ID: 79d9c6eec536
Revises: 4cb30c43922d
Create Date: 2019-03-26 20:40:22.911610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79d9c6eec536'
down_revision = '4cb30c43922d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###