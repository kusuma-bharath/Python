while 1 :
    try:
        number = int(input("Enter your favourite number !! \n"))
        print(18/number)
        break
    except ValueError:
        print("Enter proper number not invalid text")
    except ZeroDivisionError:
        print("You can't choose Zero")
    except:
        print("Some exception occurred")
        break
    finally:
        print("LOOP COMPLETED")
