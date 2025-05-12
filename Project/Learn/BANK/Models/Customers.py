class Customer:
    def __init__(self, customerid, firstname, lastname, dateofbirth, phone, email, address):
        self._customerid = customerid
        self._firstname = firstname
        self._lastname = lastname
        self._dateofbirth = dateofbirth
        self._phone = phone
        self._email = email
        self._address = address

    def get_id(self):
        return self._customerid

    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self._lastname

    def get_dateofbirth(self):
        return self._dateofbirth

    def get_phone(self):
        return self._phone

    def get_email(self):
        return self._email

    def get_address(self):
        return self._address

    def set_customerid(self, customerid):
        self._customerid = customerid

    def set_firstname(self, firstname):
        self._firstname = firstname

    def set_lastname(self, lastname):
        self._lastname = lastname

    def set_dateofbirth(self, dateofbirth):
        self._dateofbirth = dateofbirth

    def set_phone(self, phone):
        self._phone = phone

    def set_email(self, email):
        self._email = email

    def set_address(self, address):
        self._address = address

