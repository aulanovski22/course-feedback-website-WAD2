from django import forms
from course_feedback.models import Profile, Course, Review


class RegisterForm(forms.ModelForm):
    username = forms.CharField(help_text="Username")
    email = forms.CharField(help_text="Email")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Password")

    class Meta:
        model = Profile
        fields = ('username', 'email', 'password',)

class LoginForm(forms.ModelForm):
    username = forms.CharField(help_text="Username")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Password")

    class Meta:
        model = Profile
        fields = ('username', 'password',)

class AddReview(forms.ModelForm):
    content = forms.CharField(help_text="Enter feedback here.")

    class Meta:
        model = Review
        fields=('content',)

class AddCourse(forms.ModelForm):
    courseID = forms.CharField()
    name = forms.CharField()
    photo = forms.ImageField()

    class Meta:
        model = Course
        fields = ('courseID', 'name', 'photo',)