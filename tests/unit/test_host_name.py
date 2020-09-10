import pytest

from examples import hosts


class TestHostNames:
    def test_validate_rtr_name_correct(self):
        assert hosts.validate_rtr_name('IL-rtr-421') == True

    def test_validate_rtr_name_wrong_str_num(self):
        assert hosts.validate_rtr_name('ILQ-rtr-421') == False

    def test_validate_rtr_name_wrong_int_num(self):
        assert hosts.validate_rtr_name('SC-rtr-41') == False

    def test_validate_rtr_name_no_dash(self):
        assert hosts.validate_rtr_name('SCrtr-41') == False

    def test_validate_rtr_name_no_rtr(self):
        assert hosts.validate_rtr_name('SC-41') == False