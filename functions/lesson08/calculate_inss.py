# Hi guys,
# In this lesson I will show you how to calculate INSS with another way

def calculate_inss(salary): 
    ranges = [1045.00, 2089.60, 3134.40, 6268.80]
    rates = [0.08, 0.09, 0.12, 0.14]

    for i in range(len(ranges)):
        if salary <= ranges[i]:
            return salary * rates[i]
    return salary * 0.20

salary = float(input("Informe o Salário: "))
inss_discount = calculate_inss(salary)

print(f"O seu INSS: {inss_discount:.2f} Kwanzas ")
print(f"O seu salário após o INSS: {salary - inss_discount:.2f} kwanzas")

# This program calculates the INSS discount using a list of ranges and rates