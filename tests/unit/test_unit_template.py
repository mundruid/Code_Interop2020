import pytest
import mock

class TestUnitSample:

    def setup:
        """Create necessary objects, properties, and mocks"""

    def teardown:
        """Reset mocks"""

    def test_foo_success(test, mocks, fixtures):
        """Successful test"""
        # initialize fixtures
        mock_response = test
        # call mock inline if needed
        with mock.patch() as mocker:
            # call mock function

            # call foo
            foo()

        # make necessary assertions
        assert ...

    def test_foo_failure():
        ...

