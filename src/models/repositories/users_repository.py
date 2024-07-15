from sqlite3 import Connection
from typing import Dict, Tuple


class UsersRepository:

    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_user(self, user_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO user
                    (id, name, email, password, is_admin)
                VALUES
                    (?, ?, ?, ?, ?)
            ''', (
                user_infos['id'],
                user_infos['name'],
                user_infos['email'],
                user_infos['password'],
                user_infos['is_admin'],
            )
        )
        
        self.__conn.commit()
    
    def find_user_by_id(self, user_id: str) -> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM user WHERE id = ?''', (user_id,)
        )

        user = cursor.fetchone()

        return user

    def find_user_by_email(self, user_email: str) -> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM user WHERE email = ?''', (user_email,)
        )

        user = cursor.fetchone()

        return user

    def find_user_by_name(self, user_name: str) -> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM user WHERE name = ?''', (user_name,)
        )

        user = cursor.fetchone()

        return user
