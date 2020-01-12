class OrganicTestFormatter:
    fields = ['Link', 'Uid', 'Cookie', 'Cart', 'Thank you page', 'Order', 'Requests', 'Statistics', 'Status']

    def __init__(self):
        self.values = {x: input(f'{x}: ') for x in self.fields}

    def make_table(self):
        table = ''
        for key, value in self.values.items():
            if key == 'Status':
                if self.values[key] == 'y':
                    table += f"[TR][TD][B]{key}[/B][/TD][TD][CENTER][COLOR=#00A650]ОК[/COLOR][/CENTER][/TD][/TR]\n"
                else:
                    table += f"[TR][TD][B]{key}[/B][/TD][TD][CENTER][COLOR=#FF0000]FAILED[/COLOR][/CENTER][/TD][/TR]\n"
            elif key in ['Cookie', 'Cart', 'Thank you page', 'Statistics', 'Status']:
                table += f"[TR][TD][B]{key}[/B][/TD][TD][CENTER][URL={value}]Cкриншот[/URL][/CENTER][/TD][/TR]\n"
            elif key in ['Requests', 'Linking', 'Linking2(after login)', 'Linking thank you']:
                table += f"[TR][TD][B]{key}[/B][/TD][TD][CODE]{value}[/CODE][/TD][/TR]\n"
            else:
                table += f"[TR][TD][B]{key}[/B][/TD][TD][CENTER]{value}[/CENTER][/TD][/TR]\n"
        return table


class BasicTestFormatter(OrganicTestFormatter):
    fields = OrganicTestFormatter.fields.copy()
    fields.insert(1, 'Redirect Link')

    def __init__(self):
        super().__init__()

class AdmitadContextFormatter(OrganicTestFormatter):
    fields = OrganicTestFormatter.fields.copy()
    fields.insert(1, 'Redirect Link')
    fields.insert(2, 'Context link')

    def __init__(self):
        super().__init__()


class CrossdeviceTestFormatter(OrganicTestFormatter):
    fields = OrganicTestFormatter.fields.copy()
    fields.insert(1, 'Redirect Link')
    fields.insert(4, 'Registration')
    fields.insert(5, 'Linking')
    fields.insert(6, 'Linking2(after login)')
    fields.insert(9, 'Linking thank you')

    def __init__(self):
        super().__init__()