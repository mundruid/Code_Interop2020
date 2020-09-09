import re


def validate_rtr_name(name):
    if re.match('[A-Z]{2}-rtr-\d{3}', name):
        return True
    else:
        return False

if __name__ == "__main__":
    pass
