class Loan:
    def __init__(self, loanid, customerid, loanamount, interestrate, startdate, enddate, status, feeid):
        self._loanid = loanid
        self._customerid = customerid
        self._loanamount = loanamount
        self._interestrate = interestrate
        self._startdate = startdate
        self._enddate = enddate
        self._status = status
        self._feeid = feeid

    def get_id(self):
        return self._loanid

    def get_customerid(self):
        return self._customerid

    def get_loanamount(self):
        return self._loanamount

    def get_interestrate(self):
        return self._interestrate

    def get_startdate(self):
        return self._startdate

    def get_enddate(self):
        return self._enddate

    def get_status(self):
        return self._status

    def get_feeid(self):
        return self._feeid

    def set_loanid(self, loanid):
        self._loanid = loanid

    def set_customerid(self, customerid):
        self._customerid = customerid

    def set_loanamount(self, loanamount):
        self._loanamount = loanamount

    def set_interestrate(self, interestrate):
        self._interestrate = interestrate

    def set_startdate(self, startdate):
        self._startdate = startdate

    def set_enddate(self, enddate):
        self._enddate = enddate

    def set_status(self, status):
        self._status = status

    def set_feeid(self, feeid):
        self._feeid = feeid

