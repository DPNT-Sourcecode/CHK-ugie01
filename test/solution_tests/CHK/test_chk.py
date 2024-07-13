from solutions.CHK import checkout_solution as checkout


class TestSum():
    def test_checkout(self):
        # Test the checkout function
        assert checkout.checkout('A') == 50
        assert checkout.checkout('AAA') == 130
        assert checkout.checkout('AAAA') == 180
        assert checkout.checkout('AAAAA') == 200
        assert checkout.checkout('AAAAAA') == 250
        assert checkout.checkout('AAAAAAAA') == 330
        assert checkout.checkout('B') == 30
        assert checkout.checkout('BB') == 45
        assert checkout.checkout('BBB') == 75
        assert checkout.checkout('EEB') == 80
        assert checkout.checkout('EEEB') == 120
        assert checkout.checkout('EEBB') == 110
        



