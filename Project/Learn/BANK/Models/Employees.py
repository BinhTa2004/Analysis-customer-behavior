class Employee:
    def __init__(self, employeeid, firstname, lastname, position, hiredate, phone, email):
        self._employeeid = employeeid
        self._firstname = firstname
        self._lastname = lastname
        self._position = position
        self._hiredate = hiredate
        self._phone = phone
        self._email = email

    def get_id(self):
        return self._employeeid

    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self._lastname

    def get_position(self):
        return self._position

    def get_hiredate(self):
        return self._hiredate

    def get_phone(self):
        return self._phone

    def get_email(self):
        return self._email

    def set_emplyeeid(self, employeeid):
        self.employeeid = employeeid

    def set_firstname(self, firstname):
        self._firstname = firstname

    def set_lastname(self, lastname):
        self._lastname = lastname

    def set_position(self, position):
        self._position = position

    def set_hiredate(self, hiredate):
        self._hiredate = hiredate

    def set_phone(self, phone):
        self._phone = phone

    def set_email(self, email):
        self._email = email

