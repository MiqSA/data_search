import re
from datetime import datetime

class DateTransform:
    def __init__(self, date):
        self.patterns = {
            0: r"([A-Za-z]* \d{2} \d{4})",
            1: r"(\d{2} [A-Za-z]* \d{4})",
            2: r"(\d{4}-\d{2}-\d{2}T\w+)",
            3: r"([A-Za-z]* \d{2})"}
        self.formats = [
            '%B %d %Y',
            '%d %b %Y',
            ['%Y-%m-%dT%H', '%Y-%m-%dT%H:%M:%S'],
            '%b %d']
        self.date = date

    def get_format(self):
        for pattern in self.patterns:
            finded = re.findall(self.patterns[pattern], self.date)
            if len(finded)>0:
                if pattern == 2:
                    return self.formats[2][1] if self.date.count(':')>1 else self.formats[2][0]
                return self.formats[pattern]
        return None

    def str_to_datetime(self, format_finded):
        return datetime.strptime(self.date, format_finded)
    
    def main(self):
        try:
            format_finded = self.get_format()
            return self.str_to_datetime(format_finded)
        except Exception as err:
            print('Error', err)


class CheckAndSave:
    def __init__(self, data):
        self.data = data

    def check_str_field(self, field):
        if isinstance(field, str):
            return field.lower()
        if field is None:
            return ''
        return str(field)

    def main(self):
        uri = self.check_str_field(self.data['uri'])
        title = self.check_str_field(self.data['title'])
        date = self.data['date']
        valid_date = DateTransform(date).main()

        from models import Data
        model = Data(uri=uri, title=title, date_added=valid_date).save()