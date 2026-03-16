from {{project_name}}.example_file import add_two

def test_the_obvious():
    # GIVEN
    # two numbers
    A = 1
    B = 2

    # WHEN
    # those two numbers are added
    result = add_two(A,B)

    # THEN
    # the result is them added together
    assert result == 3
