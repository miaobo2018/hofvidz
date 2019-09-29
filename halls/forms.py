from .models import Video
from django import forms

class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		fields = ['title', 'url', 'youtube_id']
		labels = {'youtube_id':'YouTube Id'}