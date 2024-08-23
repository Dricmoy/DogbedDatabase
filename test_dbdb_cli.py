import subprocess
import os
import unittest

class TestDBDBCLI(unittest.TestCase):

    def setUp(self):
        """Set up an example database file before each test."""
        self.dbname = 'example.db'
        self.set_key_value('foo', 'bar')

    def tearDown(self):
        """Remove the test database file after each test."""
        if os.path.exists(self.dbname):
            os.remove(self.dbname)

    def run_command(self, *args):
        """Run a command using the subprocess module."""
        result = subprocess.run(['python', '-m', 'dbdb.tool'] + list(args),
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        return result.stdout.strip(), result.stderr.strip()

    def set_key_value(self, key, value):
        """Helper function to set a key-value pair in the database."""
        _, stderr = self.run_command(self.dbname, 'set', key, value)
        self.assertEqual(stderr, "")

    def test_get_existing_key(self):
        """Test getting an existing key's value."""
        stdout, stderr = self.run_command(self.dbname, 'get', 'foo')
        self.assertEqual(stdout, 'bar')
        self.assertEqual(stderr, "")

    def test_get_nonexistent_key(self):
        """Test getting a value for a key that does not exist."""
        stdout, stderr = self.run_command(self.dbname, 'get', 'nonexistent')
        self.assertIn("KeyError", stderr)
        self.assertEqual(stdout, "")

    def test_delete_key(self):
        """Test deleting a key from the database."""
        stdout, stderr = self.run_command(self.dbname, 'delete', 'foo')
        self.assertEqual(stderr, "")

        # Try to get the deleted key, should result in a KeyError
        stdout, stderr = self.run_command(self.dbname, 'get', 'foo')
        self.assertIn("KeyError", stderr)
        self.assertEqual(stdout, "")

    def test_overwrite_value(self):
        """Test overwriting an existing key's value."""
        self.set_key_value('foo', 'baz')
        stdout, stderr = self.run_command(self.dbname, 'get', 'foo')
        self.assertEqual(stdout, 'baz')
        self.assertEqual(stderr, "")

if __name__ == '__main__':
    unittest.main()
