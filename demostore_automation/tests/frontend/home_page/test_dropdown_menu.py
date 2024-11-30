import pytest
import logging as logger

from demostore_automation.src.pages.HomePage import HomePage


@pytest.mark.usefixtures("init_driver")
class TestDropDown:
    """
    Test class to verify the display of sorting drop-down on the home page
    """

    @pytest.fixture (scoop='class')
    def setup(self, request):
        request.cls.HomePage = HomePage(self.driver)
        yield

        @pytest.mark.estcf19
        def test_sorting_drop_down_displayed_on_top_page(self, setup):
            logger.info(f"Running Test: test_sorting_drop_down_displayed_on_top_everypage")
            """
            
            Test to verify that the sorting drop-down is displayed on the top of home page.
            
            """
            logger.info(f"Running Test: test_sorting_drop_down_displayed_on_top_home_page")
            self.homepage.go_to_home_page()
            dropdown = self.homepage.get_sorting_dropdown_top_page()
            assert 'Default sorting' in dropdown, 'drop down is not displayed'

        @pytest.mark.estcf20
        def test_sorting_drop_down_displayed_on_bottom_page(self, setup):
            logger.info(f"Running Test: test_sorting_drop_down_displayed_on_top_everypage")
            """
            Test to verify that the sorting drop-down is displayed on the bottom of homepage. 
            
            """
            logger.info(f"Running Test: test_sorting_drop_down_displayed_on_bottom_home_page")
            self.homepage.go_to_home_page()
            dropdown = self.hoepage.get_sorting_dropdown_bottom_page()
            assert 'Default sorting' in dropdown, 'drop down is not displayed'
            
