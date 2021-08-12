from TicketBooking.models import Hall, Customer, Shows


show1 = Shows("kill", 9, 11)
show2 = Shows("killer", 12, 14)
show3 = Shows("killed", 14, 16)
show4 = Shows("alive", 16, 18)
show5 = Shows("live", 18, 20)
show6 = Shows("be", 20, 22)
show7 = Shows("more", 10, 12)
show8 = Shows("hehe", 10, 12)

shows_list = [show7, show2, show1, show3, show4, show5, show6, show8]

hall1 = Hall(1, "ram", 20, [show1, show2, show6])
hall2 = Hall(2, "lakshman", 25, [show3, show4, show8])
hall3 = Hall(3, "sita", 20, [show3, show5, show7])

halls_list = [hall1, hall2, hall3]


def book_movie(customer, ):
    check_seats = get_available_seats(customer.get_show_name())


def get_available_seats(show_name):
    available_seats = []
    for hall in halls_list:
        temp = {}
        shows = hall.get_shows()
        for show in shows:
            if show.get_show_name() == str(show_name):
                temp['hall_id'] = hall.get_id()
                temp['seats'] = hall.get_seats()
                available_seats.append(temp)
    print(f"Available halls for show:{show_name} are: {available_seats}")
    return available_seats


def input_hall_selection(hall_id, seat_number):
    for hall in halls_list:
        if hall.get_id() == hall_id:
            for seat in seat_number:
                hall.update_seat_status(seat, False)


def run():
    print(f'Welcome to Wave Cinema!')
    print('Shows available:')
    for show in shows_list:
        print(f'{show.get_show_name()}, show timing: {show.get_start_time()}''\n')
    show_name = input("Please select your show: ")
    customer_name = input("Please enter your name: ")
    customer_mobile = input("Please enter your number: ")
    customer = Customer(customer_name, customer_mobile, show_name)
    book_movie(customer)
    hall_id = input("Please enter chosen hall id: ")
    seat_number = input("Please enter chosen seats: ")
    customer.set_hall_id(hall_id)
    customer.set_seat_id(seat_number)
    input_hall_selection(hall_id, [int(seat_number)])
    print(f'Seats Booked!!')
    print(f"Seats confirmation:{customer.get_show_name()},hall:{customer.get_hall_id()},seat:{customer.get_seat_id()}")


if __name__ == '__main__':
    run()
