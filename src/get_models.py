# coding: utf-8

from sqlalchemy.orm import Session

from models.tables import ScheduleDaily, Scenario
from settings.config import logger
from src.init_db import session


def insert_task(session: Session, **kwargs) -> ScheduleDaily:
    """
    Кладем таску
    :param session: сессия с БД
    :param id: номер воркера
    :return: Первое свободное задание
    """
    try:

        session.add(
            Scenario(
                **kwargs
            )
        )

        session.commit()

    except Exception as e:
        logger.error(f"Failed get task \n {e}")
        session.rollback()
    return True

if __name__ == '__main__':
    from io import BytesIO

    with open("../../test.pkl", 'rb') as fh:
        buf = BytesIO(fh.read())

    insert_task(
        session=session,
        name_scenario="test",
        pickle=buf.getvalue()
    )