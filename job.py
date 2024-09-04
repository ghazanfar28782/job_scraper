# job.py

class Job:
    def __init__(self, title, company, location):
        self._title = title
        self._company = company
        self._location = location

    # Getter and Setter for title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    # Getter and Setter for company
    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    # Getter and Setter for location
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
