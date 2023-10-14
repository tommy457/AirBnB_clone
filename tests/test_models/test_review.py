#!/usr/bin/python3
"""Test module for the Review Class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Class representing unittest for Review"""
    test_review = Review()

    def test_create_and_init(self):
        """Test method for creating a new instance"""
        self.assertEqual(Review, type(self.test_review))
        self.assertTrue(hasattr(self.test_review, "id"))
        self.assertTrue(hasattr(self.test_review, "created_at"))
        self.assertTrue(hasattr(self.test_review, "updated_at"))
        self.assertTrue(hasattr(self.test_review, "text"))
        self.assertTrue(hasattr(self.test_review, "place_id"))
        self.assertTrue(hasattr(self.test_review, "user_id"))

    def test_attrs_type(self):
        """Test Method that checks id type"""
        self.assertEqual(str, type(self.test_review.text))
        self.assertEqual(str, type(self.test_review.place_id))
        self.assertEqual(str, type(self.test_review.user_id))

    def test_str_output(self):
        """Test Method that checks str dunder method return format"""
        output = "[Review] ({}) {}".format(
            self.test_review.id, self.test_review.__dict__)
        self.assertEqual(str(self.test_review), output)


if __name__ == "__main__":
    unittest.main()
