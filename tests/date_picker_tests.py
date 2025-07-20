import pytest

@pytest.mark.parametrize(
    "date_input, should_pass",
    [
        ("09/10/2025", True),       # ✅ Valid date
        ("02/30/2025", False),      # ❌ Invalid calendar date
        ("13/01/2025", False),      # ❌ Invalid month
        ("09/10/2030", False),      # ❌ Out of range
        ("9/10/2025", False),       # ❌ Wrong format
        ("09-10-2025", False),      # ❌ Wrong separator
        ("07/21/2024", True),       # ✅ Another valid date
    ]
)
def test_date_picker(setup_home_page, date_input, should_pass):
    home_page = setup_home_page
    register_page = home_page.perform_skip_sign_in()
    date_picker_page = register_page.open_widgets_datepicker()
    if should_pass:
        date_picker_page.set_date_in_picker(date_input)
        actual_date = date_picker_page.get_date_value()
        assert actual_date == date_input, f"❌ Expected {date_input}, got {actual_date}"

    else:
        with pytest.raises(ValueError):
            date_picker_page.set_date_in_picker(date_input)
