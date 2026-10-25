from {{project_name}}.example_file import add_two


def test_the_obvious():
    # GIVEN
    # two numbers
    a = 1
    b = 2

    # WHEN
    # those two numbers are added
    result = add_two(a, b)

    # THEN
    # the result is them added together
    assert result == 3
