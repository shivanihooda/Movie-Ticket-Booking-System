class Hall:
    def __init__(self, hall_id, name, max_seats, shows):
        self.__id = hall_id
        self.__name = name
        self.__number_of_seats = max_seats
        self.__shows = shows
        self.__seats = [True] * max_seats

    def update_seat_status(self, seat_number, value):
        if seat_number < self.__number_of_seats:
            self.__seats[seat_number-1] = value
        else:
            print("Invalid seat!")

    def get_shows(self):
        return self.__shows

    def get_id(self):
        return self.__id

    def get_seats(self):
        return self.__seats


class Shows:
    def __init__(self, show_name, show_start_time, show_end_time):
        self.__show_name = show_name
        self.__start_time = show_start_time
        self.__end_time = show_end_time

    def get_show_name(self):
        return self.__show_name

    def get_start_time(self):
        return self.__start_time


class Customer:
    def __init__(self, name, number, show_name=None, hall_id=None, seat_id=None):
        self.__name = name
        self.__mobile = number
        self.__show_name = show_name
        self.__hall_id = hall_id
        self.__seat_id = seat_id

    def get_show_name(self):
        return self.__show_name

    def set_hall_id(self, hall_id):
        self.__hall_id = hall_id

    def get_hall_id(self):
        return self.__hall_id

    def set_seat_id(self, seat_id):
        self.__seat_id = seat_id

    def get_seat_id(self):
        return self.__seat_id
