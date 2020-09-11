import pytest
from django.urls import reverse

from .models import User, Board, BoardsAndUsers, Column, BoardAndColumn, Task


@pytest.mark.django_db
def test_board_create():
    Board.objects.create(board_title='ТЕСТОВАЯ БОРДА')
    assert Board.objects.count() == 1


@pytest.mark.django_db
def test_board_and_user_create():
    user = User.objects.create(username='test', email='test@m.ru', password='test')
    board = Board.objects.create(board_title='ТЕСТОВАЯ БОРДА')
    BoardsAndUsers.objects.create(user_name=user, board_title=board)
    assert BoardsAndUsers.objects.count() == 1


@pytest.mark.django_db
def test_column_create():
    Column.objects.create(column_title='ТЕСТОВАЯ КОЛОНКА')
    assert Column.objects.count() == 1


@pytest.mark.django_db
def test_board_and_column_create():
    board = Board.objects.create(board_title='ТЕСТОВАЯ БОРДА')
    column = Column.objects.create(column_title='ТЕСТОВАЯ КОЛОНКА')
    BoardAndColumn.objects.create(board_title=board, column_title=column)
    assert BoardAndColumn.objects.count() == 1


@pytest.mark.django_db
def test_task_create():
    new_user = User.objects.create(username='test', email='test@m.ru', password='test')
    new_board = Board.objects.create(board_title='ТЕСТОВАЯ БОРДА')
    new_column = Column.objects.create(column_title='ТЕСТОВАЯ КОЛОНКА')
    Task.objects.create(user_name=new_user, board_title=new_board, column_title=new_column, task_description='new des')
    assert Task.objects.count() == 1


@pytest.mark.django_db
def test_task_view(admin_client):
    url = reverse('tasks')
    response = admin_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_my_boards_view(admin_client):
    url = reverse('my-boards')
    response = admin_client.get(url)
    assert response.status_code == 200
