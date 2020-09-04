from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import User, UserAndTask
from .serializers import UserSerializer, UserAndTaskSerializer, DetailUserSerializer
from .models import Board, Task
from .serializers import BoardSerializer, TaskSerializer
from rest_framework.response import Response


# TODO: Обычный пользователь должен уметь просматривать все свои таски и менять их статус.
#  Для этого нужен реализовать отдельный url и view

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class TestAPIView(APIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        users = User.objects.all()
        return users

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = DetailUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user_data = self.request.data

        if len(user_data["user_password"]) > 8:
            new_user = User.objects.create(
                user_name=user_data["user_name"],
                user_password=user_data["user_password"],
                user_role=user_data["user_role"])
            new_user.save()
            serializer = DetailUserSerializer(new_user)
            return Response(serializer.data)
        else:
            return Response('small pass')


# @login_required
@api_view(['GET'])
def users_list(request):
    if request.method == 'GET' and str(request.user) == 'admin':
        queryset = User.objects.all()
        serializer_class = UserSerializer(queryset, many=True)
        return Response({'message': 'aaaa'})
    # elif request.method == "POST":
    #     data = JSONParser().parse(request)
    #     serializer = ProductSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"data": serializer.data, "status": status.HTTP_201_CREATED})
    #     return Response({"data": serializer.data, "status": status.HTTP_400_BAD_REQUEST})


class UserAndTaskViewSet(viewsets.ModelViewSet):
    serializer_class = UserAndTaskSerializer
    queryset = UserAndTask.objects.all()
    permission_classes = [IsAuthenticated]


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
    permission_classes = [IsAuthenticated]


# TODO: сделать вывод всех задач доступным только для админа и модератора
# TODO: сделать редирект после POST на ту же страницу для нового вывода всего списка чего-либо
class AllTasksViewSet(viewsets.ModelViewSet):
    """
    Вьюха позволяет админу или модеру просматривать, добавлять, удалять, обновлять все таски.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        tasks = Task.objects.all()
        return tasks

    def get(self, request, *args, **kwargs):
        # user = User.objects.filter(id=pk)
        tasks = self.get_queryset()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     params = kwargs
    #     print(params['pk'])
    #     return Response({})

    def post(self, request, *args, **kwargs):
        task_data = request.data
        print(task_data['task_creation_date'])
        new_task = Task.objects.create(
            board_title=task_data['board_title'],
            task_description=task_data['task_description'],
            task_creation_date=task_data['task_creation_date'],
            task_deadline=task_data['task_deadline'])
        new_task.save()

        serializer = TaskSerializer(new_task)

        return Response(serializer.data)
