"""Initial migration.

Revision ID: fe340afa3437
Revises: 
Create Date: 2022-07-11 20:44:21.884007

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, MetaData

# revision identifiers, used by Alembic.
revision = 'fe340afa3437'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    user_table = op.create_table('user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('full_name', sa.String(length=200), nullable=True),
        sa.Column('email', sa.String(length=45), nullable=False),
        sa.Column('password', sa.String(length=60), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###

    op.bulk_insert(user_table,
        [
            {'id':1, 'full_name':'John Smith', 'email':'johnsmith@correo.com', 
                'password':'123456', 'status':'A'},
            {'id':2, 'full_name':'Ed Williams', 'email':'edwilliams@correo.com', 
                'password':'123456', 'status':'A'},            
            {'id':3, 'full_name':'Wendy Jones', 'email':'wendyjones@correo.com', 
                'password':'123456', 'status':'A'}
        ]
    )

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###