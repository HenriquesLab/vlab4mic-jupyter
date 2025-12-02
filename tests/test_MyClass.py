from mypackage.my_package import MyClass

def test_MyClass():

    # initialize your class
    my_class = MyClass()

    # run the main method of the class
    example_output = my_class.run()

    # assert example output is 1
    assert example_output == 1
