from  django.db import models
from  rest_framework import serializers
class Email(models.Model):
    uid=models.BigIntegerField(verbose_name="UID",db_index=True)
    folder=models.CharField(max_length=50,verbose_name="Folder",db_index=True,default="INBOX")
    subject=models.CharField(max_length=500,blank=True,db_index=True)
    to=models.CharField(max_length=200,blank=True,db_index=True)
    from_email=models.CharField(max_length=200,blank=True)
    from_name=models.CharField(max_length=200,blank=True)
    cc=models.JSONField(default=list,blank=True)
    bcc=models.JSONField(default=list,blank=True)
    date=models.DateTimeField(null=True,blank=True,db_index=True)
    text=models.TextField(blank=True)
    html=models.TextField(blank=True)
    attachments=models.JSONField(default=list,blank=True)
    size=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = [('uid', 'folder')]
        indexes=[
            models.Index(fields=['folder', 'date']),
            models.Index(fields=['folder']),
        ]
        verbose_name="邮件"
        verbose_name_plural="邮件"
    def __str__(self):
        return f"{self.folder} - {self.subject} - {self.date}"


class EmailAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

class EmailListSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Email
        fields = 'uid','folder','subject','from_name','date'


class EmailDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'