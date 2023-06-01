class Quirk:
    def __init__(self):
        self.name = input("What is the quirk called? ")
        self.internal_name = input("What is the internal name of this quirk? ")
        self.num_abilities = int(input("How many abilities does it have? "))

        self.ability_text = ""
        for i in range(self.num_abilities):
            print(f"\nAbility {i + 1}:")
            ability = Ability()
            text = ability.text.replace("{name}", self.name)
            self.ability_text += text

        self.syr_filename = input("What is the filename of the syringe texture of this quirk? ")
        self.origin = input("Is this quirk custom, or from the anime? ")
        self.quote = input("Paste in a quote from the MHA wiki describing this quirk, or write a brief description yourself: ")
        self.text = self.insert_to_template()

    def insert_to_template(self):
        f = open("quirk-template.markdown", "r")
        text = f.read()
        f.close()
        text = text.replace("{name}", self.name)
        text = text.replace("{int_name}", self.internal_name)
        text = text.replace("{num_abilities}", str(self.num_abilities))
        text = text.replace("{syr_filename}", self.syr_filename)
        text = text.replace("{origin}", self.origin)
        text = text.replace("{quote}", self.quote)
        text = text.replace("{abilities}", self.ability_text)
        return text



class Ability:
    def __init__(self):
        self.name = input("What is this ability called? ")
        self.lvl = input("At what level is this ability unlocked? ")
        self.type = input("What type of ability is this? [Z/X/C/V/fifth/sixth/seventh/eighth] ")
        self.desc = input("Briefly describe this ability (Starting with, \"This ability\"): ")
        self.text = self.insert_to_template()

    def insert_to_template(self):
        f = open("ability_template.markdown", "r")
        text = f.read()
        f.close()
        text = text.replace("{a_name}", self.name)
        text = text.replace("{a_type}", self.type)
        text = text.replace("{a_lvl}", self.lvl)
        text = text.replace("{a_desc}", self.desc)
        return text


quirk = Quirk()
print(quirk.text)