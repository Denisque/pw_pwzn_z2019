import tkinter as tk
from functools import partial

from pwzn_work.lab_9.tools.calculator import Calculator


class CalculatorGUI(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.variables = {}
        self.state = tk.BooleanVar(value=True)
        self.init_variables()
        self.calculator = Calculator()

        self.screen = tk.Label(self, bg='white')
        self.screen.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.bottom_pad = self.init_bottom_pad()
        self.bottom_pad.pack(side=tk.BOTTOM)

    def init_variables(self):
        self.variables['var_1'] = ''
        self.variables['var_2'] = ''
        self.variables['operator'] = ''
        self.state.set(True)

    def init_bottom_pad(self):
        bottom_pad = tk.Frame(self)

        ## punkt 2
        pamiec = tk.Frame(bottom_pad)
        pamiec.pack(side=tk.LEFT)

        # MC
        tk.Button(
            pamiec, text='MC', width=5,
            command=self.calculator.clean_memory
        ).grid(row=0, column=0)
        # --
        tk.Button(
            pamiec, text='--', width=5,
            #command=self.calculator.clean_memory
        ).grid(row=1, column=0)
        # MR
        tk.Button(
            pamiec, text='MR', width=5,
            command=self.wczytej_z_pamieci
        ).grid(row=2, column=0)
        # M+
        tk.Button(
            pamiec, text='M+', width=5,
            command=self.calculator.memorize
        ).grid(row=3, column=0)
        # C
        tk.Button(
            pamiec, text='C', width=5,
            command=self.clear
        ).grid(row=4, column=0)

        ## klawiatura numeryczna
        num_pad = tk.Frame(bottom_pad)
        num_pad.pack(side=tk.LEFT)

        ii = 0
        for ii, num in enumerate(range(12, 0, -1)):
            if ii == 0:
                tk.Button(
                    num_pad, text=num-3, width=5,
                    command=partial(self.update_var, num-3)
                ).grid(row=ii // 3, column=(2-ii) % 3)
            elif ii == 1:
                tk.Button(
                    num_pad, text=num-3, width=5,
                    command=partial(self.update_var, num-3)
                ).grid(row=ii // 3, column=(2-ii) % 3)
            elif ii == 2:
                tk.Button(
                    num_pad, text=num-3, width=5,
                    command=partial(self.update_var, num-3)
                ).grid(row=ii // 3, column=(2-ii) % 3)
            elif ii == 3:
                tk.Button(
                    num_pad, text="--", width=5,
                    #command=partial(self.update_var, num)
                ).grid(row=ii // 3, column=(2-ii) % 3)
            elif ii == 4:
                tk.Button(
                    num_pad, text="--", width=5,
                    #command=partial(self.update_var, num)
                ).grid(row=ii // 3, column=(2-ii) % 3)
            elif ii == 5:
                tk.Button(
                    num_pad, text="--", width=5,
                    #command=partial(self.update_var, num)
                ).grid(row=ii // 3, column=(2-ii) % 3)
            else:
                tk.Button(
                    num_pad, text=num, width=5,
                    command=partial(self.update_var, num)
                ).grid(row=ii // 3, column=(2 - ii) % 3)
        # 0
        ii += 1
        tk.Button(
                num_pad, text='0', width=5,
                command=partial(self.update_var, '0')
        ).grid(row=ii // 3, column=ii % 3)
        # .
        ii += 1
        tk.Button(
            num_pad, text='.', width=5,
            command=partial(self.update_var_float, '.')
        ).grid(row=ii // 3, column=ii % 3)
        # =
        ii += 1
        tk.Button(
            num_pad, text='=', width=5,
            command=self.calculate_result
        ).grid(row=ii // 3, column=ii % 3)

        ## klawiatura operacji
        operation_pad = tk.Frame(bottom_pad)
        operation_pad.pack(side=tk.RIGHT)

        ii = 0
        op = list(self.calculator.operations.keys())
        op.insert(1, '--')
        for ii, operation in enumerate(op):
            if ii == 1:
                tk.Button(
                    operation_pad, text=operation, width=5,
                    #command=partial(self.set_operator, operation),
                ).grid(row=ii, column=0)
            else:
                tk.Button(
                    operation_pad, text=operation, width=5,
                    command=partial(self.set_operator, operation),
                ).grid(row=ii, column=0)

        ## punkt 3, dzialania z klawiatury
        klaw_pad = tk.Frame(bottom_pad)
        klaw_pad.bind_all('<Key>', self.key)

        return bottom_pad

    def key(self, event):
        kk = event.keysym
        oper = {'plus': '+', 'minus': '-', 'slash': '/', 'asterisk': '*'}
        if kk in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            self.update_var(int(kk))
        elif kk in oper.keys():
            self.set_operator(oper[f'{kk}'])
        elif kk in ("Return"):
            self.calculate_result()
        else:
            print("Zle podany symbol. Podaj liczbe, operator lub enter w celu obliczenia wyniku")

    def update_screen(self):
        text = f"{self.variables['var_1']}"
        if self.variables['operator']:
            text += f" {self.variables['operator']}"
        if self.variables['var_2']:
            text += f" {self.variables['var_2']}"
        self.screen['text'] = text

    def wczytej_z_pamieci(self):
        mem = self.calculator.memory
        state = self.state.get()
        if state:
            self.variables['var_1'] += str(mem)
            self.variables['var_1'] = self.variables['var_1'].lstrip('0')
        else:
            self.variables['var_2'] += str(mem)
            self.variables['var_2'] = self.variables['var_2'].lstrip('0')
        self.update_screen()

    def clear(self):
        state = self.state.get()
        if state:
            self.variables['var_1'] = ''
        else:
            self.variables['var_2'] = ''
        self.update_screen()

    def update_var_float(self, num):
        state = self.state.get()
        if state:
            self.variables['var_1'] += str(num)
            self.variables['var_1'] = self.variables['var_1'].lstrip('.')
        else:
            self.variables['var_2'] += str(num)
            self.variables['var_2'] = self.variables['var_2'].lstrip('.')
        self.update_screen()

    def update_var(self, num):
        state = self.state.get()
        if state:
            self.variables['var_1'] += str(num)
            self.variables['var_1'] = self.variables['var_1'].lstrip('0')
        else:
            self.variables['var_2'] += str(num)
            self.variables['var_2'] = self.variables['var_2'].lstrip('0')
        self.update_screen()

    def set_operator(self, operator):
        if self.variables['var_1']:
            self.variables['operator'] = operator
            self.state.set(not self.state.get())
            self.update_screen()

    def calculate_result(self):
        if self.variables['var_1'] and self.variables['var_2']:
            var_1 = float(self.variables['var_1'])
            var_2 = float(self.variables['var_2'])
            self.screen['text'] = self.calculator.run(
                self.variables['operator'], var_1, var_2
            )
            self.init_variables()


if __name__ == '__main__':
    root = tk.Tk()
    CalculatorGUI(root).pack()
    root.mainloop()