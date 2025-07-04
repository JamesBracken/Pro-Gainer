from exercise.forms import ExerciseForm, AddFavouriteExerciseForm
from unittest.mock import patch
from exercise.models import Exercise
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase


class TestExerciseForm(TestCase):

    def test_exercise_form_valid_data(self):
        # Creating an image variable to use as data for the image field
        image = SimpleUploadedFile(
            name="test_image.jpg",
            content=b"\x47\x49\x46\x38\x39\x61",
            content_type="image/gif",
        )

        form = ExerciseForm(
            files={"image": image},
            data={
                "exercise_title": "Test Exercise",
                "instruction": "Do this properly.",
                "difficulty": "easy",
                "recommended_sets": 3,
                "recommended_reps": 12,
                "intensity": "light",
                "targeted_muscles": "Chest",
                "indirectly_targeted_muscles": "Shoulders",
                "equipment": "Mat",
            }
        )
        print(form.errors)
        self.assertTrue(form.is_valid())


class TestAddFavouriteExerciseForm(TestCase):

    # Creating this dummy data is causing an actual https request to cloudinary
    # so we are making this a mock upload call instead
    @patch('cloudinary.uploader.upload')
    def setUp(self, mock_upload):

        # Creating a dummy image
        image = SimpleUploadedFile(
            name="test_image.jpg",
            content=b"\x47\x49\x46\x38\x39\x61",
            content_type="image/gif",
        )

        # Creating a valid Exercise instance for the test
        self.exercise = Exercise.objects.create(
            exercise_title="Test Exercise",
            instruction="Do this properly.",
            difficulty="easy",
            recommended_sets=3,
            recommended_reps=12,
            intensity="light",
            targeted_muscles="Chest",
            indirectly_targeted_muscles="Shoulders",
            equipment="Mat",
            image=image,  # assign the image here
            slug="test-exercise"  # add slug if required
        )

    def test_exercise_form_valid_data(self):

        form = AddFavouriteExerciseForm(
            data={
                "exercise": self.exercise.id,
            }
        )
        print(form.errors)
        self.assertTrue(form.is_valid())
