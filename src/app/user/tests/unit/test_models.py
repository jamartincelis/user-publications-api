from app.user.models import User

def test_new_user():
    user = User(full_name='John Smith', email='johnsmith@correo.com', password='123456', 
        status='A')

    assert user.email == 'johnsmith@correo.com'
    assert user.password == '123456'
    assert user.__repr__() == '<User: johnsmith@correo.com>'

def test_new_user_with_fixture(new_user):
    assert new_user.email != 'patkennedy79@gmail.com'
    assert new_user.password != 'pass'


def test_setting_password(new_user):
    new_user.set_password('MyNewPassword')
    assert not new_user.password == 'pass'

def test_user_id(new_user):
    new_user.id = 17
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)
    assert new_user.get_id() == '17'

