import random
import time
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CustomUser, InvitationCode
from .serializers import InviteCodeSerializer, UserProfileSerializer


class UserLoginAPIView(APIView):

    """ Логика входа пользователя, если он есть то предостовляется 4х значный код подтверждения
     если нет то создает нового """

    def post(self, request):
        phone_number = request.data['phone_number']
        user, created = CustomUser.objects.get_or_create(phone_number=phone_number)

        if created:
            user.activated_code = CustomUser.generate_random_code()  # генерация активационного кода
            user.save()
            return Response(data={'message': 'Номер телефона успешно зарегистрирован',
                                  'invite_code': user.activated_code},
                            status=status.HTTP_201_CREATED)

        confirm_code = random.randint(1000, 10000)
        request.session['confirm_code'] = confirm_code
        time.sleep(2)  # имитация задержки бд

        return Response(data={'message': 'Введите код подтверждения',
                              'confirm_code': confirm_code},
                        status=status.HTTP_200_OK)


class ConfirmCodeAPIView(APIView):

    """ Подтверждение пользователя"""

    def post(self, request):
        confirm_code = request.session['confirm_code']  # хранение временного кода в сессии
        input_code = request.data.get('confirm_code')

        if confirm_code == input_code:
            return Response(data={'message': 'success'}, status=status.HTTP_200_OK)

        raise NotFound('wrong code!')


class CodeActivateAPIView(CreateAPIView):

    """ Активация пригласительного кода другого пользователя в своем профиле """

    queryset = InvitationCode.objects.all()
    serializer_class = InviteCodeSerializer

    def post(self, request, *args, **kwargs):

        user = CustomUser.objects.get(id=self.kwargs['pk'])
        request_code = request.data.get('code')

        try:
            CustomUser.objects.get(activated_code=request_code)
        except:
            raise NotFound('Код не существует!')

        if user.activated_code != request_code and user.activated_code:

            if user.is_activated:
                return Response({'message': 'Код уже активирован'}, status=status.HTTP_400_BAD_REQUEST)

            user.is_activated = True
            InvitationCode.objects.create(user=user, code=request_code)  # создаем отношение
            user.save()
            owner = CustomUser.objects.get(activated_code=request_code)  # владелец пригласительного кода
            owner.activated_by.add(user)

            return Response({'message': 'Код активирован'}, status=status.HTTP_200_OK)

        return Response(data={'message': 'Нельзя активировать свой код!'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
