class OrganicTestFormatter:
    fields = ['Link', 'Uid', 'Cookie', 'Cart', 'Thank you page', 'Order', 'Requests', 'Statistics', 'Status', 'Comments']

    def __init__(self):
        self.values = {x: input(f'{x}: ') for x in self.fields}

    def make_table(self):
        table = ''
        for key, value in self.values.items():
            if value != '':
                if key == 'Status':
                    if self.values[key] == 'y':
                        table += f"[TR][TD][B]{key}[/B][/TD][TD][COLOR=#00A650]ОК[/COLOR][/TD][/TR]\n"
                    elif self.values[key] == 'n':
                        table += f"[TR][TD][B]{key}[/B][/TD][TD][COLOR=#FF0000]FAILED[/COLOR][/TD][/TR]\n"
                    else:
                        table += f"[TR][TD][B]{key}[/B][/TD][TD][COLOR=#FFF100]WAITING[/COLOR][/TD][/TR]\n"
                elif key in ['Cookie', 'Cart', 'Thank you page', 'Statistics', 'Status']:
                    table += f"[TR][TD][B]{key}[/B][/TD][TD][URL={value}]Cкриншот[/URL][/TD][/TR]\n"
                elif key in ['Requests', 'Linking', 'Linking2(after login)', 'Linking thank you']:
                    table += f"[TR][TD][B]{key}[/B][/TD][TD][CODE]{value}[/CODE][/TD][/TR]\n"
                else:
                    table += f"[TR][TD][B]{key}[/B][/TD][TD]{value}[/TD][/TR]\n"
            else:
                table += f"[TR][TD][B]{key}[/B][/TD][TD][/TD][/TR]\n"
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