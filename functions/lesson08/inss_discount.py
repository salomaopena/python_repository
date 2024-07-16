# Hi guys!
# In this lesson I will show you how to calculate INSS discount


def calculate_inss(salary):
    if salary <= 1045:
        return salary * 0.08
    elif salary <= 2089.6:
        return salary * 0.09
    elif salary <= 3134.4:
        return salary * 0.12
    elif salary <= 6268.8:
        return salary * 0.14
    else:
        return salary * 0.20
    


salary = float(input("Enter your salary: "))
inss_discount = calculate_inss(salary)

print(f"O seu INSS: {inss_discount:.2f} Kwanzas ")
print(f"O seu salário após o INSS: {salary - inss_discount:.2f} kwanzas")

# This program calculates the INSS discount based on the Brazilian INSS table