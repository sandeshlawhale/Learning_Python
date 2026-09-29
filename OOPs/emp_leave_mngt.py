class Employee:
    def __init__(self, name, emp_id, dept):
        self.name = name
        self.emp_id = emp_id
        self.dept = dept
        self._history = []

    def request_leave(self, days):
        if days <= 0:
            return "Leave days should be greater than 0"

        if days <= self._available_leave_days:
            self._history.append((days, self._available_leave_days - days))
            self._available_leave_days -= days

            return f"leave granted for {days} days, {self._available_leave_days} leaves remaining"

        return f"no leave granted as you have {self._available_leave_days} leaves remaining"

    @property
    def leave_balance(self):
        return self._available_leave_days

    @property
    def leave_history(self):
        res = "Leave History: \n"

        for leave, rem in self._history:
            res += f"{leave} days - {rem} leave remaining\n"

        return res


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, dept):
        super().__init__(name, emp_id, dept)
        self._available_leave_days = 20


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, dept):
        super().__init__(name, emp_id, dept)
        self._available_leave_days = 10

    def request_leave(self, days):
        if days > 5:
            return (
                "Cannot grant the leave for more than 5 days for a Part Time Employee"
            )

        return super().request_leave(days)


class Contractor(Employee):
    def __init__(self, name, emp_id, dept):
        super().__init__(name, emp_id, dept)
        self._available_leave_days = 0

    def request_leave(self, days):
        return "Leave request rejected: Contractors do not have paid leave"


# employees = [
#     FullTimeEmployee("Sandesh", 123, "Tech"),
#     PartTimeEmployee("Jane", 124, "HR"),
#     Contractor("John", 125, "Finance"),
# ]

# for employee in employees:
#     print(employee.request_leave(6))
#     print(employee.leave_balance)

emp = Contractor("Sandesh", 123, "Tech")

print(emp.request_leave(6))
print(emp.request_leave(7))
print(emp.request_leave(5))
print(emp.request_leave(8))

print(emp.leave_history)
