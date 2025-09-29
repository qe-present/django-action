from  django.db import models
class Email(models.Model):
    uid=models.BigIntegerField(verbose_name="UID",db_index=True)
    folder=models.CharField(max_length=50,verbose_name="Folder",db_index=True,default="INBOX")
    subject=models.CharField(max_length=500,blank=True,db_index=True)
    sender=models.CharField(max_length=200,blank=True,db_index=True)
    receiver=models.CharField(max_length=200,blank=True)
    cc=models.JSONField(default=list,blank=True)
    date=models.DateTimeField(null=True,blank=True,db_index=True)
    is_seen=models.BooleanField(default=False)
    is_flagged=models.BooleanField(default=False)
    text=models.TextField(blank=True)
    html=models.TextField(blank=True)
    attachments=models.JSONField(default=list,blank=True)
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
