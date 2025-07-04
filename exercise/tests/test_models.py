from django.test import TestCase
from django.utils import timezone
from exercise.models import Exercise, FavouriteExercise


class TestExerciseModel(TestCase):
    def setUp(self):
        self.exercise1 = Exercise.objects.create(
            exercise_title="Push Up",
            image="https://res.cloudinary.com/demo/image/upload/sample.jpg",
            difficulty="easy",
            intensity="light",
            instruction="Keep your back straight and lower yourself until your elbows are at 90 degrees.",
            equipment="None",
            targeted_muscles="Chest, Triceps",
            indirectly_targeted_muscles="Shoulders, Core",
            recommended_sets=3,
            recommended_reps=12,
            created_at=timezone.now(),
        )

    def test_exercise_is_assigned_slug_on_creation(self):
        self.assertEqual(self.exercise1.slug, "push-up")


class TestFavouriteExerciseModel(TestCase):
    def setUp(self):
        self.exercise = Exercise.objects.create(
            exercise_title="Squat",
            image="https://res.cloudinary.com/demo/image/upload/sample.jpg",
            difficulty="medium",
            intensity="moderate",
            instruction="Lower your hips from a standing position and then stand back up.",
            equipment="Barbell",
            targeted_muscles="Legs",
            indirectly_targeted_muscles="Core",
            recommended_sets=4,
            recommended_reps=10,
            created_at=timezone.now(),
        )

        self.favourite_exercise1 = FavouriteExercise.objects.create(
            exercise=self.exercise,
            added_at=timezone.now(),
        )
