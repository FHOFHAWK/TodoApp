from django.test import TestCase

from .models import User, Board, BoardsAndUsers


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
        a = BoardsAndUsers.objects.create(user_name=new_user, board_title=new_board)
        self.assertEqual(BoardsAndUsers, a.user_name)
        self.assertEqual(BoardsAndUsers.board_title, a.board_title)
