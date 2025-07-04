from django.test import SimpleTestCase
from django.urls import reverse, resolve
from exercise.views import (exercise_list, exercise_detail,
                            edit_exercise_item, add_exercise_item,
                            delete_exercise_item, favourite_exercise_list,
                            toggle_is_favourite_exercise)


class TestUrls(SimpleTestCase):

    def test_exercise_list_url_resolves(self):
        url = reverse("exercise_list")
        print(resolve(url))
        self.assertEqual(resolve(url).func, exercise_list)

    def test_exercise_detail_url_resolves(self):
        url = reverse("exercise_detail", args=["slug-test"])
        print(resolve(url))
        self.assertEqual(resolve(url).func, exercise_detail)

    def test_add_exercise_item_url_resolves(self):
        url = reverse("add_exercise_item")
        print(resolve(url))
        self.assertEqual(resolve(url).func, add_exercise_item)

    def test_edit_exercise_item_url_resolves(self):
        url = reverse("edit_exercise_item", args=["slug-test"])
        print(resolve(url))
        self.assertEqual(resolve(url).func, edit_exercise_item)

    def test_delete_exercise_item_url_resolves(self):
        url = reverse("delete_exercise_item", args=["slug-test"])
        print(resolve(url))
        self.assertEqual(resolve(url).func, delete_exercise_item)

    def test_favourite_exercise_list_url_resolves(self):
        url = reverse("favourite_exercise_list")
        print(resolve(url))
        self.assertEqual(resolve(url).func, favourite_exercise_list)

    def test_toggle_is_favourite_exercise_url_resolves(self):
        url = reverse("toggle_is_favourite_exercise", args=["id-test"])
        print(resolve(url))
        self.assertEqual(resolve(url).func, toggle_is_favourite_exercise)
