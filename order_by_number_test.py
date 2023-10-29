import sender_stand_request

def positive_assert():
    response = sender_stand_request.get_order_by_track()
    assert response.status_code == 200

def test_1():
    positive_assert()

# Минаков Александр, Earth — Финальный проект. Инженер по тестированию плюс