from website.models import User


def test_home(client):
    response = client.get("/")
    assert b"<title>Home</title>" in response.data


def test_registration(client, app):
    response = client.post(
        "/sign-up", data={"email": "dummy@test.com", "username": "testUser", "password1": "testpassword", "password2": "testpassword"})

    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "dummy@test.com"
