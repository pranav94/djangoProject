import pytest
from django.utils import timezone
from django.db.utils import IntegrityError

from polls.models import (
    Question,
    Choice
)


@pytest.mark.django_db()
def test_add_question():
    """
    Test if we can add a question to the database safely
    """
    pub_date = timezone.now()
    question = Question(question_text="Test question", pub_date=pub_date)
    question.save()
    assert question.question_text == "Test question"
    assert question.pub_date == pub_date

@pytest.mark.django_db()
def test_add_choice_to_question():
    """
    Test if we can add a choice to a question safely
    """
    pub_date = timezone.now()
    question = Question(question_text="Test question", pub_date=pub_date)
    question.save()
    choice = Choice(question_id=question.id, choice_text="Test choice", votes=23)
    choice.save()
    assert choice.choice_text == "Test choice"
    assert choice.votes == 23

@pytest.mark.django_db(transaction=True)
def test_add_choice_to_no_question():
    """
    Assert Integrity error if a choice is added
    to a question that does not exist
    """
    with pytest.raises(IntegrityError) as excinfo:
        choice = Choice(question_id=33, choice_text="Test choice", votes=23)
        choice.save()

    assert "FOREIGN KEY constraint failed" in str(excinfo)
    