import ydb


def blocking_query(session, query):
    return session.transaction().execute(
        query,
        commit_tx=True,
        settings=ydb.BaseRequestSettings().with_timeout(3).with_operation_timeout(2)
    )


class Cars_reader:
    route = "NaN"

    def set_route(self, value):
        self.route = value

    start = "NaN"

    def set_start(self, value):
        self.start = value

    end = "NaN"

    def set_end(self, value):
        self.end = value

    stops = "0"

    def set_stops(self, value):
        self.stops = value

    number = "NaN"

    def set_number(self, value):
        self.number = value

    model = "NaN"

    def set_model(self, value):
        self.model = value

    def select_all_cars(self, session):
        query = '''SELECT TROLLEYBUS.TROLL_ID as number, TROLLEYBUS.MODEL as model, ROUTE.ROUTE_ID as route, ROUTE.FIRST_END || ' - ' || ROUTE.SECOND_END as line
    FROM TROLLEYBUS INNER JOIN ROUTE ON TROLLEYBUS.ROUTE_ID = ROUTE.ROUTE_ID''';
        return blocking_query(session, query)

    def select_routes(self, session):
        query = '''SELECT ROUTE_ID as route FROM ROUTE'''
        return blocking_query(session, query)

    def list_by_lyne(self, session):
        query = """SELECT TROLLEYBUS.TROLL_ID as number, TROLLEYBUS.MODEL as model, ROUTE.ROUTE_ID as route, ROUTE.FIRST_END || ' - ' || ROUTE.SECOND_END as line     FROM TROLLEYBUS INNER JOIN ROUTE ON TROLLEYBUS.ROUTE_ID = ROUTE.ROUTE_ID WHERE ROUTE.ROUTE_ID = CAST('""" + self.route + """' AS INT16);"""
        return blocking_query(session, query)

    def is_lyne(self, session):
        query = """SELECT COUNT(ROUTE_ID) as C FROM ROUTE WHERE ROUTE_ID = CAST('""" + self.route + """' AS INT16);"""
        return blocking_query(session, query)

    def insert_route(self, session):
        query = """UPSERT INTO `ROUTE` ( `ROUTE_ID`, `FIRST_END`, `SECOND_END`, `STOPS` ) VALUES (   CAST(""" + self.route + """ AS INT16), '""" + self.start + """','""" + self.end + """', CAST(""" + self.stops + """ AS INTEGER) );"""
        return blocking_query(session, query)

    def insert_troll(self, session):
        query = """UPSERT INTO `TROLLEYBUS` ( `TROLL_ID`, `MODEL`, `ROUTE_ID` ) VALUES (   CAST(""" + self.number + """ AS INT16), '""" + self.model + """', CAST(""" + self.route + """ AS INT16) );"""
        return blocking_query(session, query)

    def delete_troll(self, session):
        query = """DELETE FROM TROLLEYBUS WHERE TROLL_ID = CAST(""" + str(self.number) + """AS INT16);"""
        return blocking_query(session, query)

    def is_trolls(self, session):
        query = """SELECT COUNT(TROLL_ID) as C FROM TROLLEYBUS WHERE ROUTE_ID = CAST('""" + self.route + """' AS INT16);"""
        return blocking_query(session, query)

    def delete_route(self, session):
        query = """DELETE FROM ROUTE WHERE ROUTE_ID = CAST(""" + str(self.route) + """AS INT16);"""
        return blocking_query(session, query)


reader = Cars_reader()