class Transaction:
    def __init__(self, transactionid, accountid, transactiondate, transactiontype, amount, description, feeid):
        self._transactionid = transactionid
        self._accountid = accountid
        self._transactiondate = transactiondate
        self._transactiontype = transactiontype
        self._amount = amount
        self._description = description
        self._feeid = feeid

    def get_id(self):
        return self._transactionid

    def get_accountid(self):
        return self._accountid

    def get_transactiondate(self):
        return self._transactiondate

    def get_transactiontype(self):
        return self._transactiontype

    def get_amount(self):
        return self._amount

    def get_description(self):
        return self._description

    def get_feeid(self):
        return self._feeid

    def set_transactionid(self, transactionid):
        self._transactionid = transactionid

    def set_accountid(self, accountid):
        self._accountid = accountid

    def set_transactiondate(self, transactiondate):
        self._transactiondate = transactiondate

    def set_transactiontype(self, transactiontype):
        self._transactiontype = transactiontype

    def set_amount(self, amount):
        self._amount = amount

    def set_description(self, description):
        self._description = description

    def set_feeid(self, feeid):
        self._feeid = feeid

