import pytest
import logging as logger

from demostore_automation.src.pages.HomePage import HomePage


@pytest.mark.usefixtures("init_driver")
class TestDropDown:
    """
    Test class to verify the display of sorting drop-down on the home page
    """

    @pytest.fixture ('scoop='class')
    