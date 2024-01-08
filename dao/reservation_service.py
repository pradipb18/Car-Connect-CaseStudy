
from interfaces.IReservationService import IReservationService
from exception.exceptions import ReservationNotFoundException
from decimal import Decimal


class ReservationService(IReservationService):
    def __init__(self, db_conn_util, connection_string):
        self._db_conn_util = db_conn_util
        self._connection_string = connection_string

    def GetReservationById(self, reservation_id):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Reservation WHERE ReservationID = %s", (reservation_id,))
            reservation_data = cursor.fetchone()

            if reservation_data:
                return reservation_data
            else:
                raise ReservationNotFoundException(f"Reservation with ID {reservation_id} not found.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def GetReservationsByCustomerId(self, customer_id):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Reservation WHERE CustomerID = %s", (customer_id,))
            reservations_data = cursor.fetchall()

            if reservations_data:
                return reservations_data
            else:
                raise ReservationNotFoundException(f"No reservations found for Customer ID {customer_id}.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def CreateReservation(self, reservationData,):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO Reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                reservationData['customer_id'],
                reservationData['vehicle_id'],
                reservationData['start_date'],
                reservationData['end_date'],
                Decimal(reservationData['total_cost']),
                reservationData['status']
            ))

            connection.commit()
            print("Reservation created successfully.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def UpdateReservation(self, reservation_data):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("""
                UPDATE Reservation
                SET CustomerID = %s,
                    VehicleID = %s,
                    StartDate = %s,
                    EndDate = %s,
                    TotalCost = %s,
                    Status = %s
                WHERE ReservationID = %s
            """, (
                reservation_data['customer_id'],
                reservation_data['vehicle_id'],
                reservation_data['start_date'],
                reservation_data['end_date'],
                reservation_data['total_cost'],
                reservation_data['status'],
                reservation_data['reservation_id']
            ))

            connection.commit()
            print("Reservation updated successfully.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def CancelReservation(self, reservation_id):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("""
                UPDATE Reservation
                SET Status = 'Cancelled'
                WHERE ReservationID = %s
            """, (reservation_id,))

            connection.commit()
            print(f"Reservation with ID {reservation_id} has been cancelled.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def GetReservationsList(self):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Reservation")
            reservations_data = cursor.fetchall()

            if reservations_data:
                return reservations_data
            else:
                raise ReservationNotFoundException("No reservations found.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()
