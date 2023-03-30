To use this test suite, the following commands need to be installed:

pip install pytest
pip install pytest-html
pip install requests
pip install selenium
Currently, the only supported browsers are Firefox and Chrome. To execute tests in a preferred browser, add the parameter "--browser=firefox" or "--browser=chrome".

You can add "marks" to execute tests in groups:

py.test -v -m login --browser=firefox --html=report.html
py.test -v -m shoppingcart --browser=firefox --html=report.html
You can also execute tests by file:

py.test -v -k test_sign_in.py --browser=firefox --html=report.html
py.test -v -k test_shopping_cart.py --browser=firefox --html=report.html
To execute all tests, use the following command:

py.test -v -m all --browser=firefox --html=report.html