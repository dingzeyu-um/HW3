class FortuneCookieJar:
    def __init__(self, fortunes):
        self.fortune_slips = fortunes
        self.name_roster = []
        self.dealt_indices = []
    
    def __str__(self):
        if not self.fortune_slips:
            return ""
        return "-".join(self.fortune_slips)