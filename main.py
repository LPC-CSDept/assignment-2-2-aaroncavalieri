def main():
    ##################################################
   
    celcius = input("Temperature in degrees celcius: ")
    farenheit = (9/5) * int(celcius) + 32

    print (f'Farenheit: {float(farenheit):.2f}')

    ##################################################
    pass


if __name__ == '__main__':
    main()
