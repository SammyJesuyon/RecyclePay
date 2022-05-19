from db.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from lib.utils import Util


class VerifyEmail(generics.GenericAPIView):
    permissions_classes = (AllowAny,)

    def get(self, request):
        encoded_email = request.GET.get('')
        try:
            decoded_email = Util.decode_email(encoded_email)
            user = User.objects.get(email=decoded_email)
            if user is not None:
                user.is_verified = True
                user.save()
                return Response(data={
                    "success": "Your account has been successfully verified"
                }, status=status.HTTP_200_OK)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response(data={'Invalid activation link!'}, status=status.HTTP_400_BAD_REQUEST)