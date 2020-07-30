try:
    from tkinter import *
except NameError:
    from Tkinter import *

try:
    input = raw_input
except NameError:
    pass

import getpass

class Login:
    def __init__(self, title='Login'):
        self.title = title
        self.values = {}
        self.fields = []
        
    def prompt(self):
        for field in self.fields:
            if field['key'] not in self.values.keys() or self.values[field['key']] is None:
                self.display()
    
    def get_value(self, key):
        self.prompt()
        
        return self.values[key]
                
    def add_prompt(self, key, label, prompt_type='TEXT', default=None):
        prompt = {
                  'key': key,
                  'label': label,
                  'type': prompt_type,
                  'default': default
                  }
        self.fields.append(prompt)

    
class GUILogin(Login):
    def display(self):
        root = Tk()
        root.title(self.title)
        root.geometry('600x200+100+100')
        
        for field in self.fields:
            box = Entry(root)
            field['entry'] = box
            box.config(width=50)
            if field['type'] == 'PASSWORD':
                box.config(show = '*')
            elif field['default'] is not None:
                box.insert(0, field['default'])
            
        def onenter(evt):
            for field in self.fields:
                b = field['entry']
                if b.get() == '':
                    b.focus()
                    return
                else:
                    self.values[field['key']] = b.get()
            
            root.destroy()
        
        def onokclick():
            for field in self.fields:
                b = field['entry']
                if b.get() == '':
                    b.focus()
                    return
                else:
                    self.values[field['key']] = b.get()
            
            root.destroy()

        row = 0
        
        for field in self.fields:
            Label(root, text=field['label']).grid(row=row)
            field['entry'].grid(row=row, column=1)
            row = row + 1
        
        for field in self.fields:
            if field['default'] is None:
                field['entry'].focus()
                break
            
        root.bind('<Return>', onenter)
        Button(root, command=onokclick, text = 'OK').grid(row=row, column=1)
        root.attributes('-topmost', 1)
        root.focus()
        root.mainloop()

class CLILogin(Login):
    def display(self):
        print(self.title)
        
        for field in self.fields:
            if field['type'] == 'PASSWORD':
                self.values[field['key']] = getpass.getpass("Please Enter your %s: " % field['label'])
            else:
                self.values[field['key']] = self.__prompt__(field['label'], field['default'])

    def __prompt__(self, prompt, default):
        if default is not None:
            default_prompt = ' [' + default + ']'
        else:
            default_prompt = ''
            
        return input('Please Enter your %s%s: ' % (prompt, default_prompt)) or default


class Factory:
    def get_login(self, login_type='CLI', title='Login'):
        if login_type == 'GUI':
            return GUILogin(title)
        else:
            return CLILogin(title)
    
