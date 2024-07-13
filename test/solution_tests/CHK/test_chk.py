from lib.solutions.CHK import checkout_solution as checkout


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
        assert checkout.checkout('FF') == 20
        assert checkout.checkout('FFF') == 20
        assert checkout.checkout('FFFF') == 30
        assert checkout.checkout('HHHHH') == 45
        assert checkout.checkout('HHHHHHHHHH') == 80
        assert checkout.checkout('HHHHHHHHH') == 85
        assert checkout.checkout('NNNM') == 120
        assert checkout.checkout('NNM') == 95
        assert checkout.checkout('PPPPP') == 200
        assert checkout.checkout('PPPPPP') == 250
        assert checkout.checkout('QQQ') == 80
        assert checkout.checkout('RRRQ') == 150
        assert checkout.checkout('RRRQQ') == 180
        assert checkout.checkout('UUUU') == 120
        assert checkout.checkout('UUU') == 120
        assert checkout.checkout('VV') == 90
        assert checkout.checkout('VVV') == 130
        assert checkout.checkout('VVVV') == 180
        assert checkout.checkout('VVVVV') == 220
        assert checkout.checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 965
        




