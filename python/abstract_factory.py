"""Ejemplo: Sistema de Reservaciones para Transporte
Supongamos que queremos construir un sistema para reservar viajes, que puede manejar tanto vuelos como trenes. Cada medio de transporte tiene su propio tipo de asiento y ticket (boleto).

El Abstract Factory nos permite crear familias de objetos (asientos y boletos) que son específicos para cada medio de transporte (avión o tren) sin necesidad de cambiar el código cliente que los utiliza.
"""

from abc import ABC, abstractmethod
from random import randint

# abc es un módulo que proporciona herramientas para crear clases abstractas. Una clase abstracta es una clase que no se puede instanciar y que se utiliza como superclase.

# Abstract Factory
## Interfaces Abstractas


class Seat(ABC):
    @abstractmethod
    def get_seat_info(self):
        """Devuelve información sobre el asiento."""
        pass


class Ticket(ABC):
    @abstractmethod
    def get_ticket_info(self):
        """Devuelve información sobre el boleto."""
        pass


## Implementaciones Concretas
class AirplaneSeat(Seat):
    def get_seat_info(self):
        return f"Airplane Seat {randint(1, 100)}"


class AirplaneTicket(Ticket):
    def get_ticket_info(self):
        return f"Airplane Ticket {randint(1000, 9999)}"


class TrainSeat(Seat):
    def get_seat_info(self):
        return f"Train Seat {randint(1, 100)}"


class TrainTicket(Ticket):
    def get_ticket_info(self):
        return f"Train Ticket {randint(1000, 9999)}"


class BusSeat(Seat):
    def get_seat_info(self):
        return f"Bus Seat {randint(1, 50)}"


class BusTicket(Ticket):
    def get_ticket_info(self):
        return f"Bus Ticket {randint(1000, 9999)}"


class StadiumSeat(Seat):
    def get_seat_info(self):
        return f"Stadium Seat {randint(1, 50000)}"


class StadiumTicket(Ticket):
    def get_ticket_info(self):
        return f"Stadium Ticket {randint(1000, 99999)}"


# Fabrica Abstracta
class Factory(ABC):
    @abstractmethod
    def create_seat(self):
        """Crea un asiento."""
        pass

    @abstractmethod
    def create_ticket(self):
        """Crea un boleto."""
        pass


# Fabricas Concretas
class AirplaneFactory(Factory):
    def create_seat(self):
        return AirplaneSeat()

    def create_ticket(self):
        return AirplaneTicket()


class TrainFactory(Factory):
    def create_seat(self):
        return TrainSeat()

    def create_ticket(self):
        return TrainTicket()


class BusFactory(Factory):
    def create_seat(self):
        return BusSeat()

    def create_ticket(self):
        return BusTicket()


class StadiumFactory(Factory):
    def create_seat(self):
        return StadiumSeat()

    def create_ticket(self):
        return StadiumTicket()


# Cliente
class Reservation:
    def __init__(self, factory):
        self.factory = factory

    def make_reservation(self):
        self.seat = self.factory.create_seat()
        self.ticket = self.factory.create_ticket()
        return self.seat.get_seat_info(), self.ticket.get_ticket_info()

    def __repr__(self):
        return f"Seat: {self.seat.get_seat_info()}, Ticket: {self.ticket.get_ticket_info()}"


def client(factory: Factory):
    reservation = Reservation(factory)
    seat_info, ticket_info = reservation.make_reservation()
    print(f"Reservación completada:\n - {seat_info}\n - {ticket_info}")


# Usar el sistema para vuelos
print("Reserva para un vuelo:")
client(AirplaneFactory())

# Usar el sistema para trenes
print("\nReserva para un tren:")
client(TrainFactory())

# Usar el sistema para autobuses
print("\nReserva para un autobús:")
client(BusFactory())

# Usar el sistema para estadios
print("\nReserva para un estadio:")
client(StadiumFactory())
