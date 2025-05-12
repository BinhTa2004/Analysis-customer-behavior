class Branch:
    def __init__(self, branchid, branchname, branchlocation, managerid):
        self._branchid = branchid
        self._branchname = branchname
        self._branchlocation = branchlocation
        self._managerid = managerid

    def get_id(self):
        return self._branchid

    def get_branchname(self):
        return self._branchname

    def get_branchlocation(self):
        return self._branchlocation

    def get_managerid(self):
        return self._managerid

    def set_branchid(self, branchid):
        self._branchid = branchid

    def set_branchname(self, branchname):
        self._branchname = branchname

    def set_branchlocation(self, branchlocation):
        self._branchlocation = branchlocation

    def set_managerid(self, managerid):
        self._managerid = managerid

