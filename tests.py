import unittest
from server import app
from model import db, connect_to_db, example_data
from server import get_table_assignments, get_all_tables


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

    def test_main_page_load(self):
        """Tests that the page loads."""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn("Last name:", result.data)

    def test_get_all_tables(self):
        """Integration test. Tests get_all_tables and dependencies, and
        validates that app connects to database."""

        result = get_all_tables()
        self.assertEqual(len(result), 3)

    def test_get_table_assignments(self):
        """Unit test. Tests get_table_sizes function."""

        self.assertEqual(
            get_table_assignments(['name'] * 11),
            [['name', 'name', 'name', 'name', 'name'],
                ['name', 'name', 'name'],
                ['name', 'name', 'name']])


if __name__ == '__main__':
    unittest.main()
