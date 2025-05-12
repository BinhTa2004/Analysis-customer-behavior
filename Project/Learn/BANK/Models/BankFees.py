class BankFees:
    def __init__(self, feeid, feetype, amount, description, applicabledate):
        self._feeid = feeid
        self._feetype = feetype
        self._amount = amount
        self._description = description
        self._applicabledate = applicabledate

    def get_id(self):
        return self._feeid

    def get_feetype(self):
        return self._feetype

    def get_amount(self):
        return self._amount

    def get_description(self):
        return self._description

    def get_applicabledate(self):
        return self._applicabledate

    def set_feeid(self, feeid):
        self._feeid = feeid

    def set_feetype(self, feetype):
        self._feetype = feetype

    def set_amount(self, amount):
        self._amount = amount

    def set_description(self, description):
        self._description = description

    def set_applicabledate(self, applicabledate):
        self._applicabledate = applicabledate


