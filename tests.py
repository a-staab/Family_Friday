import unittest
from server import app
from model import db, connect_to_db, example_data


class Test(unittest.TestCase):
    """Tests for public pages."""

    def setUp(self):
        """Connect to testing database and populate with exemplary data."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///test_database")

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Reset."""

        # End session and delete tables
        db.session.close()
        db.drop_all()

    def test_signup_page_render(self):
        """Tests that the page loads."""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn("Last name:", result.data)



if __name__ == '__main__':
    unittest.main()
