


import pytest
from demostore_automation.src.pages.HomePage import HomePage
from demostore_automation.src.pages.Header import Header
from demostore_automation.src.pages.CartPage import CartPage


@pytest.mark.usefixtures("init_driver")
class TestCartPageExpiredCouponSmoke:

    @pytest.mark.estcf1
    @pytest.mark.abc123
    def test_verify_expired_coupon(self):

        # go to home add add item to cart
        home_page = HomePage(self.driver)

        # go to home page
        home_page.go_to_home_page()
        home_page.click_first_add_to_cart_button()


        # make sure the cart is updated before going to cart
        header = Header(self.driver)
        header.wait_until_cart_item_count(1)


        # go to cart
        header.click_on_cart_on_right_header()
       

        # verify there are items in the cart
        cart_page = CartPage(self.driver)
        product_names = cart_page.get_all_product_names_in_cart()
        assert len(product_names) == 1, f"Expected 1 product in cart but found {len(product_names)}"


        # apply expired coupon
        expired_coupon_code = 'QUATROSEXPIRED1' # TODO: remove hard coding. this will only work on the dev site
        cart_page.apply_coupon(expired_coupon_code)
        displayed_msg = cart_page.get_error_message()
        # breakpoint()

        expected_msg = 'Coupon "q2371se9446oqueehfr" does not exist!'
        if displayed_msg != expected_msg:
            raise Exception(f"Test=expired coupon. Displayed error message does not match expected.")
        else:
            print("PASS")
        # verify the invalid coupon