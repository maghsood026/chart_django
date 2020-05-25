from django.db import models


class Date(models.Model):
    data_time = models.DateTimeField()


class OrganizationUser(models.Model):
    user_id = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    malicious_rate = models.IntegerField(default=0)

    list_data_time = models.ForeignKey(Date, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user_id