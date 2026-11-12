from employee import employee_details

def test_employee_details_Harshita():
    result = employee_details("Harshita", "E123", "IT", 50000)

    expected_result = (
        "Employee Name: Harshita\n"
        "Employee ID: E123\n"
        "Department: IT\n"
        "Salary: 50000\n"
    )

    assert result == expected_result