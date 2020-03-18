import schemas
import logger
from datetime import datetime


class TestTagTag:
    start = '[TABLE]\n'
    end = '[/TABLE]'
    tests_to_do = ['Deeplink', 'Organic', 'One-Click', 'Context->Admitad', 'Admitad->Context', 'Crossdevice']
    integration_type = 'TAGTAG'
    ok = '[CENTER][COLOR=#00A650]ОК[/COLOR][/CENTER]'
    fail = '[CENTER][COLOR=#FF0000]FAILED[/COLOR][/CENTER]'
    wait = '[CENTER][COLOR=#F7941D]WAITING[/COLOR][/CENTER]'

    def __init__(self, company):
        self.integration = f"[TR][TD][/TD][TD][CENTER][B]{self.integration_type}[/B][/CENTER][/TD][/TR]\n"
        self.company_name = f"[TR][TD][/TD][TD][CENTER][B]{company}[/B][/CENTER][/TD][/TR]\n"
        while True:
            if input('Нужен ли дополнительный тест? y or n?: ') == 'y':
                self.tests_to_do.append(input('Введите название теста: '))
            else:
                break
        self.tests = {x: self._perform_test(x) for x in self.tests_to_do}

    def _perform_test(self, test_name):
        if input(f'Будет ли производиться тест {test_name}? Укажите y или n: ') == 'y':
            if test_name == 'Organic':
                test = schemas.OrganicTestFormatter()
            elif test_name == 'Crossdevice':
                test = schemas.CrossdeviceTestFormatter()
            elif test_name == 'Admitad->Context':
                test = schemas.AdmitadContextFormatter()
            else:
                test = schemas.BasicTestFormatter()
        else:
            return ''
        return f"[TR][TD][B]{(lambda x: self.ok if x == 'y' else ((lambda x: self.fail if x == 'n' else self.wait)(test.values['Status'])))(test.values['Status'])}[/B][/TD][TD][CENTER][B]{test_name}[/B][/CENTER][/TD][/TR]\n" + test.make_table()

    def make_test_table(self):
        test_table = self.start + self.company_name + self.integration
        for key in self.tests:
            test_table += self.tests[key]
        return test_table + self.end


if __name__ == '__main__':
    format_logger = logger.create_logger('Глашатай')
    company = input('Введите название компании: ')
    test = TestTagTag(company)
    with open(f'/home/dmatuytsya/tests/{company} {datetime.now()}.txt', 'w') as f:
        f.write(test.make_test_table())
    format_logger.info(f'Выполнен тест компании "{company}"')