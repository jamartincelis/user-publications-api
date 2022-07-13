"""Add Publication Model.

Revision ID: 0b8df429fc14
Revises: fe340afa3437
Create Date: 2022-07-12 22:28:16.121535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b8df429fc14'
down_revision = 'fe340afa3437'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    publication_table = op.create_table('publication',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=50), nullable=False),
        sa.Column('description', sa.String(length=200), nullable=False),
        sa.Column('priority', sa.String(length=60), nullable=True),
        sa.Column('status', sa.String(length=20), nullable=False),
        sa.Column('time', sa.DateTime(), nullable=True),
        sa.Column('user', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['user'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
    op.bulk_insert(publication_table,
        [
            {'id':1, 'title':'Mi publicacion de prueba', 'priority':'high',
                'description':'Mi publicacion de prueba descripción', 'status':'A', 
                'user':1},
            {'id':2, 'title':'Mi publicacion de prueba 2', 'priority':'high',
                'description':'Mi publicacion de prueba descripción 2', 'status':'A', 
                'user':1},
            {'id':3, 'title':'Mi publicacion de prueba 3', 'priority':'high',
                'description':'Mi publicacion de prueba descripción', 'status':'A', 
                'user':1},
            {'id':4, 'title':'Mi publicacion de prueba 4', 'priority':'high',
                'description':'Mi publicacion de prueba descripción 2', 'status':'A', 
                'user':2}
        ]
    )  

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('publication')
    # ### end Alembic commands ###
