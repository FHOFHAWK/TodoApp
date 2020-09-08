from django.test import TestCase

from .models import User, Board, BoardsAndUsers, Column, BoardAndColumn, Task


class BoardTestCase(TestCase):
    def setUp(self):
        Board.objects.create(board_title='ТЕСТОВАЯ БОРДА')

    def test_board_str(self):
        """
        Тест метода str в модели Board
        """
        new_board = Board.objects.get(board_title='ТЕСТОВАЯ БОРДА')
        self.assertEqual(new_board.__str__(), 'ТЕСТОВАЯ БОРДА')
        self.assertNotEqual(new_board.__str__(), 'prikoldes')


class BoardsAndUsersTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='test', email='test@m.ru', password='test')
        Board.objects.create(board_title='ТЕСТОВАЯ БОРДА')

    def test_boards_and_users_create(self):
        """
        Тест создания модели BoardsAndUsers
        """
        new_user = User.objects.get(username='test')
        new_board = Board.objects.get(board_title='ТЕСТОВАЯ БОРДА')
        new_board_and_user = BoardsAndUsers.objects.create(user_name=new_user, board_title=new_board)
        self.assertEqual(str(new_board_and_user.user_name), 'test')
        self.assertEqual(str(new_board_and_user.board_title), 'ТЕСТОВАЯ БОРДА')


class ColumnTestCase(TestCase):
    """
    Тест создания модели Column
    """

    def setUp(self):
        Column.objects.create(column_title='ТЕСТОВАЯ КОЛОНКА')

    def test_boards_and_users_create(self):
        """
        Тест создания модели Column
        """
        new_column = Column.objects.get(column_title='ТЕСТОВАЯ КОЛОНКА')
        self.assertEqual(new_column.column_title, 'ТЕСТОВАЯ КОЛОНКА')


class BoardAndColumnTestCase(TestCase):
    def setUp(self):
        Board.objects.create(board_title='ТЕСТОВАЯ БОРДА')
        Column.objects.create(column_title='ТЕСТОВАЯ КОЛОНКА')

    def test_boards_and_users_create(self):
        """
        Тест создания модели BoardAndColumn
        """
        new_board = Board.objects.get(board_title='ТЕСТОВАЯ БОРДА')
        new_column = Column.objects.get(column_title='ТЕСТОВАЯ КОЛОНКА')
        new_board_and_column = BoardAndColumn.objects.create(board_title=new_board, column_title=new_column)
        self.assertEqual(str(new_board_and_column.board_title), 'ТЕСТОВАЯ БОРДА')
        self.assertEqual(str(new_board_and_column.column_title), 'ТЕСТОВАЯ КОЛОНКА')


class TaskTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='test', email='test@m.ru', password='test')
        Board.objects.create(board_title='ТЕСТОВАЯ БОРДА')
        Column.objects.create(column_title='ТЕСТОВАЯ КОЛОНКА')

    def test_boards_and_users_create(self):
        """
        Тест создания модели Task
        """
        new_user = User.objects.get(username='test')
        new_board = Board.objects.get(board_title='ТЕСТОВАЯ БОРДА')
        new_column = Column.objects.get(column_title='ТЕСТОВАЯ КОЛОНКА')
        new_task = Task.objects.create(user_name=new_user, board_title=new_board, column_title=new_column,
                                       task_description='new des')

        self.assertEqual(str(new_task.user_name), 'test')
        self.assertEqual(str(new_task.board_title), 'ТЕСТОВАЯ БОРДА')
        self.assertEqual(str(new_task.column_title), 'ТЕСТОВАЯ КОЛОНКА')
        self.assertEqual(str(new_task.task_description), 'new des')
