import logging
import requests
import asserts
# from contextlib2 import ExitStack
from exception import MyException
from printer import log_pass, log_fail
import win_unicode_console
win_unicode_console.enable()
logger = logging.getLogger(__name__)


def run_test(in_file, test_spec):
    """Run a single tavern test

    Args:
        in_file (str): filename containing this test
        test_spec (dict): The specification for this test

    Raises:
        MyException: If any of the tests failed
    """

    if not test_spec:
        logger.warning("Empty test block in %s", in_file)
        return


    test_block_name = test_spec["test_name"]

    logger.info("Running test : %s", test_block_name)

    try:
        req = test_spec["req"]
        r = requests.request(**req)
    except MyException:
        log_fail(req, r, None)
        raise

    validates = test_spec["validates"]
    for validate in validates:
        validate = validate.items()
        # print(validate)
        for key, values in validate:
            # print(values)
            if values[0] == values[1]:
                log_pass(req, r)
            else:
                text = "".join(values[0] + asserts[key] + values[1])
                log_fail(req, r, text)
