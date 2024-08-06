from django.db import models
from tinymce.models import HTMLField
import re
# as per recommendation from @freylis, compile once only
CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

# Create your models here.
class ClientEmail(models.Model):

    id = models.AutoField(db_column="ID", primary_key=True)
    email = models.CharField(db_column="EMAIL", max_length=50, unique=True)

    def __str__(self):
        return str(self.email)
    

class Article(models.Model):
    id = models.AutoField(db_column="ID", primary_key=True)
    title = HTMLField()
    content = HTMLField()
    image = models.ImageField(upload_to="articleImages/")
    category = models.CharField(max_length=20)
    description = HTMLField(max_length=300)
    creationDate = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateField(auto_now=True)
    
    def __str__(self):
        return str(cleanhtml(self.title))


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.TextField()
    lastName = models.TextField()
    email = models.TextField()
    subject = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.subject)