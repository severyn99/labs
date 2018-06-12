class ChildrenClass:
    totalNumberOfChildren = 0

    def __init__(self, location="LNU", subject="English", number_of_children=100, price=550, tutor="Ihor"):

        self.location = location
        self.subject = subject
        self.number_of_children = number_of_children
        self.price = price
        self.tutor = tutor

        ChildrenClass.totalNumberOfChildren += number_of_children

    def to_string(self):
            print("Location: " + self.location + " Subject:", self.subject,
                  " Number of children:", self.number_of_children, " Price:", self.price, " Tutor:", self.tutor)

    def print_sum(self):
            print("Current number of children", self.number_of_children, "in the class at " + self.location)

    @staticmethod
    def print_static_sum():
            print("Total number of children: ", ChildrenClass.totalNumberOfChildren)


if __name__ == '__main__':
    nu_lp = ChildrenClass("NU LP", "Maths", 21, 710)
    lnu = ChildrenClass()
    lisoteh = ChildrenClass("Lisoteh", "Ukrainian", 80, 100, "Liubomyr")

    print("\n")
    nu_lp.to_string()
    lnu.to_string()
    lisoteh.to_string()

    print("\n")
    nu_lp.print_sum()
    lnu.print_sum()
    lisoteh.print_sum()

    print("\n")
    ChildrenClass.print_static_sum()
