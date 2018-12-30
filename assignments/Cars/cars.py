import csv
import os

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        '''Получаем расширение файла с фото'''
        return os.path.splitext(self.photo_file_name)


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = "car"


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_width = body_whl[0]
        self.body_height = body_whl[1]
        self.body_length = body_whl[2]
        self.car_type = "truck"
        

    def get_body_volume(self):
        '''Получаем объем грузовика'''
        return self.body_height * self.body_width * self.body_length
          


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = "spec_machine"


def get_params_from_str(param):
    res = [0, 0, 0]

    if param == "":
        return res

    param_list = param.split("x")
    #print("param list: ", param_list)
    if len(param_list) != 3:
        return None

    try:
        for i in range(len(param_list)):
            res[i] = float(param_list[i])
    except TypeError:
        return None

    return res
    

def get_obj_from_row(row):
    if len(row) != 7:
        return None

    ctype = row[0]
    name = row[1]
    scount = row[2]
    pfile = row[3]
    bwhl = row[4]
    carry = row[5]
    extra = row[6]

    try:
        carry = float(carry)
    except TypeError:
        return None

    if ctype == "car":
        '''car setup'''
        try:
            scount = int(scount)
        except TypeError:
            return None

        return Car(name, pfile, carry, scount)
    elif ctype == "truck":
        '''truck setup'''
        bwhl = get_params_from_str(bwhl)
        if not bwhl:
            return None
        return Truck(name, pfile, carry, bwhl)
        
    elif ctype == "spec_machine":
        '''spec_machine setup'''
        return SpecMachine(name, pfile, carry, extra)
    else:
        return None

def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            print(row)
            obj = get_obj_from_row(row)
            if obj:
                car_list.append(obj)

    return car_list

'''def _main():
    print(get_car_list("coursera_week3_cars.csv"))

    #print(cars[1].get_body_volume())

if __name__ == "__main__":
    _main()'''