from src.todoapp.config.core import settings


def test_health(test_app) -> None:
    # Given
    # When
    response = test_app.get(f"{settings.API_V1_STR}/healthz")

    # Then
    assert response.status_code == 200
