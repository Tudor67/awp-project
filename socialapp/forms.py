from django.forms import Form, CharField, Textarea


class UserPostForm(Form):
    text = CharField(widget=Textarea(
        attrs={'cols': 100, 'rows': 5}),
        label="Enter your post here")


class UserPostCommentForm(Form):
    text = CharField(widget=Textarea(
        attrs={'cols': 50, 'rows': 2}),
        label="Enter your comment here")
    author = CharField(widget=Textarea(
        attrs={'cols': 20, 'rows': 1}), 
        initial = 'Eau de Web',
        label="Enter your name here   ")
