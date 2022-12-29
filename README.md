Necesitamos instalar los siguientes comandos:
pip install pytest
pip install pytest-html
pip install requests
pip install selenium

Por el momento los navegadores son solo firefox ó chrome. 
Para ejecutar los test en un navegador de preferencia se debe agregar el parametro --browser=firefox ó --browser=chrome

Agregue unas 'mark' para ejecutar los test de forma grupal:
py.test -v -m login --browser=firefox --html=report.html
py.test -v -m shoppingcart --browser=firefox --html=report.html

Podemos ejecutarlos por archivo:
py.test -v -k test_sign_in.py --browser=firefox --html=report.html
py.test -v -k test_shopping_cart.py --browser=firefox --html=report.html 

Y con el siguiente comando se ejecutan todos los test.
py.test -v -m all --browser=firefox --html=report.html


PD: En el archivo home_page.py tuve que agregar una logica no muy agradable, por que swaglabs retiene la actividad del usuario en la pagina, intente limpiando la cache y cookies pero no tuve manera de arreglarlo.
    def add_to_cart(self):
        """Add to cart"""
        if self.element_is_present(*self.locator.REMOVE_FROM_CART_BACKPACK):
            self.find_element(*self.locator.REMOVE_FROM_CART_BACKPACK).click()
        self.add_to_cart_backpack()















