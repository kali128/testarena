from utils import Functions as f


class Task:

    def __init__(self, title='NEW TASK',
                 description='New task description', environments='', versions='', date=str(f.get_date(1))):
        self.title = title
        self.description = description
        self.environments = environments
        self.versions = versions
        self.date = date
