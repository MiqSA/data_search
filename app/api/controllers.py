
from main.controllers import DateTransform

class Filters:
    def __init__(self):
        from models import Data
        self.data = Data()

    def search_in_list_title(self, value, data_list):
        return [info for info in data_list if value in info['title']]

    def search_in_list_datetime(self, start_date, end_date, data_list):
        start_date = DateTransform(start_date).main()
        end_date = DateTransform(end_date).main()
        res = [data for data in data_list if start_date <= data['date_added'] <= end_date]
        return res

    def all(self, start_date, end_date, uri, title):
        result = self.by_uri(uri)
        if len(result)==1:
            return result
        new_result = self.search_in_list_title(title, result) 
        if len(new_result)==1:
            return new_result
        return self.search_in_list_datetime(start_date, end_date, new_result)

    def by_title(self, title):
        return self.data.find_by_title(title)

    def by_uri(self, uri):
        return self.data.find_by_uri(uri)

    def by_date(self, start_date, end_date):
        if len(start_date)>1 and len(end_date)>1:
            return self.by_date_between(start_date, end_date)
        elif len(start_date)>1:
            return self.by_date_after(start_date)
        return self.by_date_before(end_date)

    def by_date_between(self, start_date, end_date):
        return self.data.find_by_date_between(start_date, end_date)

    def by_date_after(self, start_date):
        return self.data.find_by_date_after(start_date)
    
    def by_date_before(self, end_date):
        return self.data.find_by_date_before(end_date)
