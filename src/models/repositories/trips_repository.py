from typing import Dict
from sqlite3 import Connection

# Setup actions with Db (insert, select, update, delete, ...)
class TripsRepository:
    
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_trip(self, trip_infos: Dict) -> None:
        # cursor is responsible for communicating and performing actions with our database
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO trips
                    (id, destination, start_date, end_date, owner_name, owner_email)
                VALUES
                    (?, ?, ?, ?, ?, ?)
            ''', (
                trip_infos['id'],
                trip_infos['destination'],
                trip_infos['start_date'],
                trip_infos['end_date'],
                trip_infos['owner_name'],
                trip_infos['owner_email'],
            )
        )

        self.__conn.commit()

    def find_trip_by_id(self, trip_id: str):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM trips WHERE id = ?''', (trip_id,)
        )

        trip = cursor.fetchone() # Get and return only one trip
        
        return trip

    def update_trip_status(self, trip_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                UPDATE trips
                    SET status = 1
                WHERE 
                    id = ?
            ''', (trip_id,)
        )

        self.__conn.commit()
