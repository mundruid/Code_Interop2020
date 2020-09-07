import pytest
import mock

class TestUnitSample:

    def setup:
        """Create necessary objects, properties, and mocks"""

    def teardown:
        """Reset mocks"""

    def test_foo_success(test):
        """Successful test"""
        # initialize fixtures
        mock_response = test
        # call mock inline if needed
        with mock.patch() as mocker:
            # call mock function

            # call foo
            foo()

        # make necessari assertions
        assert ...

    def test_foo_failure():
        ...