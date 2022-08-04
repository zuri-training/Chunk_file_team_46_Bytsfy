import unittest
from django.urls import path
from .views import chunk


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()
app_name = "chunked_files"
urlpatterns = [
    path("", chunk, name="chunk"),
]