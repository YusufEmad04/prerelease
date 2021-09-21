import time

passengers = []
uniquePassengerNum = 100
uniqueBookingNum = 100


class Passenger:
    uniqueNum = 0
    name = 0
    bookingDetails = 0
    def __init__(self,name,uniqueNum):
        self.name=name
        self.uniqueNum=str(uniqueNum)

    def book(self,uniqueBookingNum,startingTime,codes,totalPrice):
        self.bookingDetails = dict()
        self.bookingDetails["uniqueBookingNum"] = uniqueBookingNum
        self.bookingDetails["startingTime"] = startingTime
        self.bookingDetails["codes"] = codes
        self.bookingDetails["totalPrice"] = totalPrice


def start(num):
    if num == 1:
        createAcc()
    elif num == 2:
        book()
    elif num == 3:
        for i in passengers:
            print("Name : {}, unique id : {}, booking details {}".format(i.name,i.uniqueNum,i.bookingDetails))
    else:
        print("please enter 1, 2 or 3\n")


def validTime(time):

    x = time.split(":")
    return not (len(x) != 2 or int(x[0]) > 23 or int(x[1]) >59)

def validCode(code,stage):
    if stage == 1:

        try:
            return not (len(code) != 2 or int(code[1]) > 5 or int(code[1]) < 1 or (code[0] not in ["c", "C"]))
        except:
            return False

    elif stage == 2:

        try:
            return not (len(code) != 2 or int(code[1]) > 5 or int(code[1]) < 1 or (code[0] not in ["m", "M"]))
        except:
            return False


    elif stage == 3:
        try:
            return not (len(code) != 2 or int(code[1]) > 5 or int(code[1]) < 1 or (code[0] not in ["F", "f"]))
        except:
            return False



def createAcc():
    name = input("Enter your name :\n")
    global uniquePassengerNum
    valid = int(input("Your name : {} \nYour passenger account number : {}\n1) Confirm\n2) Cancel\n".format(name,uniquePassengerNum)))
    if valid == 1 :
        x = Passenger(name, uniquePassengerNum)
        print("Your name : {} \nYour passenger account number : {}".format(name,uniquePassengerNum))
        uniquePassengerNum += 1
        passengers.append(x)
    elif valid == 2:
        pass
    else :
        print("You entered a wrong number")


def book():
    index =0
    stage13 = [1.50,3.00,4.50,6.00,8.00]
    stage2 =[5.75,12.50,22.25,34.50,45.0]
    uniqueN = input("Enter your passenger account number :\n")
    exist = False
    for i in range(len(passengers)):
        if passengers[i].uniqueNum == uniqueN:
            exist = True
        index = i

    if exist:
        v = True
        tim = input("Enter start time :\n")
        if not validTime(tim):
            while v:
                tim = input("Enter start time correctly :\n")
                v =not validTime(tim)

        v = True
        code1 = input("Enter code for journey stage 1 :\nC1  |  1.50$\nC2  |  3.00$\nC3  |  4.50$\nC4  |  6.00$\nC5  "
                      "|  8.00$\n")

        if not validCode(code1,1):
            while v:
                code1 = input("Enter code for journey stage 1 correctly :\n")
                v = not validCode(code1,1)

        v = True

        code2 = input("Enter code for journey stage 2 :\nM1  |  5.75$\nM2  |  12.50$\nM3  |  22.25$\nM4  |  34.50$\nM5  "
                      "|  45.00$\n")
        if not validCode(code2,2):
            while v:
                code2 = input("Enter code for journey stage 2 correctly :\n")
                v = not validCode(code2, 2)

        v = True

        code3 = input("Enter code for journey stage 3 :\nF1  |  1.50$\nF2  |  3.00$\nF3  |  4.50$\nF4  |  6.00$\nF5  "
                      "|  8.00$\n")
        if not validCode(code3, 3):
            while v:
                code3 = input("Enter code for journey stage 3 correctly :\n")
                v = not validCode(code3, 3)

        print(code1,code2,code3)
        global uniqueBookingNum
        total_price = stage13[int(code1[1])-1] + stage2[int(code2[1])-1] + stage13[int(code3[1])-1]
        discount = 0
        if int(tim.split(":")[0]) > 10:
            discount = 0.4
        elif int(tim.split(":")[0]) == 10:
            if int(tim.split(":")[1]) > 0:
                discount = 0.4
        else :
            discount = 0

        disc = ""
        if discount == 0.4:
            disc = "40%"
            total_price /= 0.4
        else:
            disc = "No discount"
        confirm = input("Your booking details :\nName : {}\nTime : {}\nStage 1 code : {}\nStage 2 code : {}\nStage 3 code : {}\nYour "
                        "booking number : {}\nTotal Price : {}$\nDiscount : {}\n\n\n1)Confirm   2)Cancel\n".format(passengers[index].name,tim,code1,code2,code3,uniqueBookingNum ,total_price,disc))
        v = True
        if confirm == "1":
            passengers[index].book(uniqueBookingNum,tim,[code1,code2,code3],total_price)
            print("Trip has been booked successfully!")
        elif confirm == "2":
            pass
        else:
            while v:
                confirm = input("Enter 1 or 2\n")
                v = not (confirm in ["1","2"])

        uniqueBookingNum +=1

    else:
        print("not found")

def main():
    while True:
        x = input("\n\n1) Create a new account\n2) Book a trip\n3) View all passengers\n")
        try:
            start(int(x))
        except:
            print("Enter a number")

main()
