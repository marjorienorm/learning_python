temperature = float( input( print("What is the current temperature: ") ) )
forecast = input( print("What is the forecast - rain, sun or windy"))

if temperature > 95:
    print("It is too hot!")
    print("Stay inside!")
elif temperature < 30:
    print("It is too cold!")
    print("Stay inside!")
else:
    print("Go outside and have some fun!")
    print("Have a good day!")