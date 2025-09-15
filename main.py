import random


class FortuneCookieJar:
    def __init__(self, fortunes):
        self.fortune_slips = fortunes
        self.name_roster = []
        self.dealt_indices = []

    def __str__(self):
        if not self.fortune_slips:
            return ""
        return "-".join(self.fortune_slips)

    def assign_fortune(self, name):
        if name in self.name_roster:
            pos = self.name_roster.index(name)
            existing_fortune = self.fortune_slips[self.dealt_indices[pos]]
            return f"That name already has a fortune: {existing_fortune}"

        available_indices = []
        for i in range(len(self.fortune_slips)):
            if i not in self.dealt_indices:
                available_indices.append(i)

        if not available_indices:
            return "The jar is empty—no fortunes left to assign."

        chosen_index = random.choice(available_indices)

        self.name_roster.append(name)
        self.dealt_indices.append(chosen_index)

        return self.fortune_slips[chosen_index]


def main():
    fortunes = [
        "Follow Your Inner Voice",
        "Opportunity Knocks Softly",
        "Trust the Process",
        "Ask for Help",
        "Change is Coming",
        "Enjoy the Little Things",
    ]

    jar = FortuneCookieJar(fortunes)
    print(jar.assign_fortune("bob"))
    print(jar.assign_fortune("bob"))


main()
