from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    Model
)


class Question(Model):
    """
    The question model for the polls includes the
    question text and the date of publishment
    """
    question_text = CharField(max_length=200)
    pub_date = DateTimeField('date published')


class Choice(Model):
    """
    Each question has multiple choices with
    the number of votes for the choice
    """
    question = ForeignKey(Question, on_delete=CASCADE)
    choice_text = CharField(max_length=200)
    votes = IntegerField(default=0)