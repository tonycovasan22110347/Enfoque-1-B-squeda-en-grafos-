class InformationValue:
    def __init__(self, prior_expected_value, new_expected_value):
        self.prior_expected_value = prior_expected_value
        self.new_expected_value = new_expected_value

    def calculate_value(self):
        return self.new_expected_value - self.prior_expected_value

prior_expected_value = 50  
new_expected_value = 70   

info_value = InformationValue(prior_expected_value, new_expected_value)
value = info_value.calculate_value()

print(f"El valor de la información es: {value}")
