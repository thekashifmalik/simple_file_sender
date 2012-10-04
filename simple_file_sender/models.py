from django.db import models

class UploadedFile(models.Model):
	data = models.FileField(upload_to='uploaded_files')
	name = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name