class Account:
    def __init__(self, accountid, accountnumber, accounttypeid, customerid, balance, creationdate, branchid, feeid):
        self._accountid = accountid
        self._accountnumber = accountnumber
        self._accounttypeid = accounttypeid
        self._customerid = customerid
        self._balance = balance
        self._creationdate = creationdate
        self._branchid = branchid
        self._feeid = feeid

    def get_id(self):
        return self._accountid

    def get_accountnumber(self):
        return self._accountnumber

    def get_accounttypeid(self):
        return self._accounttypeid

    def get_customerid(self):
        return self._customerid

    def get_balance(self):
        return self._balance

    def get_creationdate(self):
        return self._creationdate

    def get_branchid(self):
        return self._branchid

    def get_feeid(self):
        return self._feeid

    def set_accountid(self, accountid):
        self._accountid = accountid

    def set_accountnumber(self, accountnumber):
        self._accountnumber = accountnumber

    def set_accounttypeid(self, accounttypeid):
        self._accounttypeid = accounttypeid

    def set_customerid(self, customerid):
        self._customerid = customerid

    def set_balance(self, balance):
        self._balance = balance

    def set_creationdate(self, creationdate):
        self._creationdate = creationdate

    def set_branchid(self, branchid):
        self._branchid = branchid

    def set_feeid(self, feeid):
        self._feeid = feeid

