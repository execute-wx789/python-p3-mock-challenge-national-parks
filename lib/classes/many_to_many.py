class NationalPark:

    def __init__(self, name):
        self.name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]
    
    def visitors(self):
        return list({trip.visitor for trip in Trip.all if trip.national_park is self})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitorHold = [trip.visitor for trip in Trip.all if trip.national_park is self]
        sumsOfMaxVisits = max([visitorHold.count(visitor) for visitor in visitorHold if visitorHold.count(visitor)])
        for visitor in visitorHold:
            if visitorHold.count(visitor) == sumsOfMaxVisits:
                return visitor

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not hasattr(self,"name"):
            self._name = name


class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self,start_date):
        if isinstance(start_date,str) and len(start_date) >= 7:
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self,end_date):
        if isinstance(end_date,str) and len(end_date) >= 7:
            self._end_date = end_date


class Visitor:

    def __init__(self, name):
        self.name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]
    
    def national_parks(self):
        return list({trip.national_park for trip in Trip.all if trip.visitor is self})
    
    def total_visits_at_park(self, park):
        return [trip.national_park for trip in Trip.all if trip.visitor is self].count(park)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if isinstance(name,str) and 1 < len(name) < 15:
            self._name = name