from rest_framework import status, serializers
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from celery.result import AsyncResult
from .email import EmailAddSerializer, Email,EmailListSerializer
from ..tasks import send_email_task


class EmailAPIView(ListCreateAPIView):
    def create(self, request, *args, **kwargs):
        """
        处理 POST 请求，异步获取最近几天的电子邮件。
        """
        print(request)
        print(request.data)
        days=request.data.get('days')
        try:
            days = int(days)
            if days <= 0:
                raise ValueError
        except ValueError:
            return Response({"detail": "参数 days 必须为正整数"}, status=status.HTTP_400_BAD_REQUEST)
        async_result=send_email_task.delay(days=days)  # 使用 Celery 异步执行任务
        data = {
            "status": async_result.state,
            "days": days
        }
        return Response(data, status=status.HTTP_200_OK)


class EmailListView(ListCreateAPIView):
    serializer_class = EmailListSerializer
    def get(self, request, *args, **kwargs):
        """
        处理 GET 请求，返回所有存储的电子邮件。
        """
        emails = Email.objects.all().order_by('-uid') # 按 uid 降序排列
        serializer = self.get_serializer(emails, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmailStatusAPIView(APIView):
    def get(self, request, *args, **kwargs):
        task_id=request.query_params.get('task_id')
        r = AsyncResult(task_id)
        return Response(
            {
                "task_id": r.id,
                "state": r.state,
                "ready": r.ready(),
                "successful": r.successful() if r.ready() else None,
                "result": r.result if r.ready() else None,
            },
            status=status.HTTP_200_OK
        )