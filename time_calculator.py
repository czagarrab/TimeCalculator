import flet as ft
from flet import (
    Page,
    Container,
    Column,
    Row,
    Text,
    TextField,
    UserControl,
    ElevatedButton,
    colors,
    border_radius
)

class TimeCalculatorApp(UserControl):

    # Build
    def build(self):
        # Params
        self.selected_border_color = colors.RED
        self.value_ms = 0
        self.actual_operator = None
        self.new_value = True
        self.negative = False

        self.hours = TextField(
                                prefix_style=ft.TextStyle(color=colors.WHITE, size=28),
                                value='00',
                                label='Hrs',
                                color=colors.WHITE,
                                width='150',
                                text_size=40,
                                text_align=ft.TextAlign.RIGHT,
                                read_only=True,
                                on_focus=self.on_text_focus,
                                data='h_tf'
                            )
        self.minutes = TextField(
                                value='00',
                                label='Mins',
                                color=colors.WHITE,
                                width='80',
                                text_size=40,
                                text_align=ft.TextAlign.CENTER,
                                read_only=True,
                                on_focus=self.on_text_focus,
                                data='m_tf'
                            )
        self.seconds = TextField(
                                value='00',
                                label='Segs',
                                color=colors.WHITE,
                                width='80',
                                text_size=40,
                                text_align=ft.TextAlign.CENTER,
                                read_only=True,
                                on_focus=self.on_text_focus,
                                data='s_tf'
                            )
        
        self.reset()
        return Container(
            width=390,
            height=410,
            bgcolor=colors.BLACK,
            padding=20,

            # Content
            content=Column(
                controls=[
                    # Result display
                    Row(
                        controls=[
                            self.hours,
                            Text(
                                value=':',
                                width='5',
                                size="40",
                                color=colors.WHITE,
                            ),
                           self.minutes,
                            Text(
                                value=':',
                                size="40",
                                width='1',
                                color=colors.WHITE,
                            ),
                            self.seconds,
                        ]),
                    # Buttons 7, 8, 9, AC
                    Row(
                        controls=[
                            ElevatedButton(
                                text="7",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                width="80",
                                height="60",
                                # on_click=self.button_clicked,
                                data="7",
                                style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            ),
                            ElevatedButton(
                                text="8",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                width="80",
                                height="60",
                                # on_click=self.button_clicked,
                                data="8",
                                style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            ),
                            ElevatedButton(
                                text="9",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                width="80",
                                height="60",
                                # on_click=self.button_clicked,
                                data="9",
                                style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            ),
                            ElevatedButton(
                                text="AC",
                                bgcolor=colors.ORANGE_400,
                                color=colors.WHITE,
                                width="80",
                                height="60",
                                # on_click=self.button_clicked,
                                data="AC",
                                style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            ),
                        ]
                    ),
                    # Buttons 4, 5, 6, +
                    Row(
                        controls=[
                            ElevatedButton(
                                text="4",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                width="80",
                                height="60",
                                # on_click=self.button_clicked,
                                data="4",
                                 style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            ),
                            ElevatedButton(
                                text="5",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                width="80",
                                height="60",
                                # on_click=self.button_clicked,
                                data="5", style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            ),
                            ElevatedButton(
                                text="6",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                width="80",
                                height="60",
                                # on_click=self.button_clicked,
                                data="6",
                                 style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            ),
                            ElevatedButton(
                                text="+",
                                bgcolor=colors.ORANGE_400,
                                color=colors.WHITE,
                                width="80",
                                height="60",
                                # on_click=self.button_clicked,
                                data="+",
                                style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            ),
                        ]
                    ),
                    # Buttons 1, 2, 3, -
                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                width="80",
                                height="60",
                                # on_click=self.button_clicked,
                                data="1",
                                style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            ),
                            ElevatedButton(
                                text="2",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                width="80",
                                height="60",
                                # on_click=self.button_clicked,
                                data="2",
                                style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            ),
                            ElevatedButton(
                                text="3",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                 width="80",
                                height="60",
                                # on_click=self.button_clicked,
                                data="3",
                                style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            ),
                            ElevatedButton(
                                text="-",
                                bgcolor=colors.ORANGE_400,
                                color=colors.WHITE,
                                width="80",
                                height="60",
                                # on_click=self.button_clicked,
                                data="-",
                                style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            ),
                        ]
                    ),
                    # Buttons 0, =
                    Row(
                        controls=[
                            ElevatedButton(
                                text="0",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                 width="260",
                                height="60",
                                # on_click=self.button_clicked,
                                data="0",
                                style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            ),
                            ElevatedButton(
                                text="=",
                                bgcolor=colors.ORANGE_800,
                                color=colors.WHITE,
                                width="80",
                                height="60",
                                # on_click=self.button_clicked,
                                data="=",
                                style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(radius=10),
                                ),
                                on_focus=self.on_focus_evt,
                                on_click=self.on_click_evt
                            )
                        ]
                    )
                ]
            )
        )
    
    def addNumber(self, data):
        if data == '':
            return        
        h = self.hours.value
        m = self.minutes.value
        s = self.seconds.value
        if self.new_value:        
            h = '00'
            m = '00'
            s = '00'
            self.new_value = False
        if self.actual_operator == 'substract':
            self.hours.prefix_text = '-'
        else:
            self.hours.prefix_text = ''

        if data in ('1','2','3','4','5','6','7','8','9'):
            # Actual focus: hours
            if self.actualFocus == 'H':
                h = h.lstrip("0")
                aux = h + data
                if len(aux) > 4:
                    m = data
                    self.actualFocus = 'M'
                    self.minutes.border_color = self.selected_border_color
                    self.hours.border_color = None 
                else:
                    h = aux
            # Actual focus: minutes
            elif self.actualFocus == 'M':
                m = m.lstrip("0")
                aux = m + data
                if len(aux) > 2:
                    self.actualFocus = 'S'
                    s = data
                    self.seconds.border_color = self.selected_border_color
                    self.minutes.border_color = None 
                elif int(aux) <= 59:
                    m = aux
                else:
                    self.actualFocus = 'S'
                    s = data
                    self.seconds.border_color = self.selected_border_color
                    self.minutes.border_color = None 
            # Actual focus: seconds
            else:
                s = s.lstrip("0")
                aux = s + data
                if len(aux) <= 2:
                    s = aux
                else:
                    s = data
                if int(s) > 59:
                    s = data
        elif data == '0':
            # Actual focus: hours
            if self.actualFocus == 'H':
                if h == '00':
                    m = data
                    self.actualFocus = 'M'
                    self.minutes.border_color = self.selected_border_color
                    self.hours.border_color = None 
                    return

                aux = h + data
                if len(aux) > 4:
                    m = data
                    self.actualFocus = 'M'
                    self.minutes.border_color = self.selected_border_color
                    self.hours.border_color = None 
                else:
                    h = aux
            # Actual focus: minutes
            elif self.actualFocus == 'M':
                aux = m + data
                if len(aux) > 2:
                    self.actualFocus = 'S'
                    s = data
                    self.seconds.border_color = self.selected_border_color
                    self.minutes.border_color = None 
                elif int(aux) <= 59:
                    m = aux
                else:
                    self.actualFocus = 'S'
                    s = data
                    self.seconds.border_color = self.selected_border_color
                    self.minutes.border_color = None 
            # Actual focus: seconds
            else:
                aux = s + data
                if len(aux) <= 2:
                    s = aux
                else:
                    s = data
                if int(s) > 59:
                    s = data


        if len(h) == 1:
            h = '0' + h
        if len(m) == 1:
            m = '0' + m
        if len(s) == 1:
            s = '0' + s

        self.hours.value = h
        self.minutes.value = m
        self.seconds.value = s

    def on_keyboard(self,e: ft.KeyboardEvent):
        if e.key in ('1','2','3','4','5','6','7','8','9', '0'):
            self.addNumber(e.key)
        elif e.key == 'Backspace':
            if self.actualFocus == 'H':
                self.hours.value = '00'
            elif self.actualFocus == 'M':
                self.minutes.value = '00'
                self.actualFocus = 'H'
                self.hours.border_color = self.selected_border_color
                self.minutes.border_color = None
            else:
                self.seconds.value = '00'
                self.actualFocus = 'M'
                self.minutes.border_color = self.selected_border_color
                self.seconds.border_color = None
        elif e.key == 'Tab':
            if self.actualFocus == 'H':
                self.actualFocus = 'M'
                self.minutes.border_color = self.selected_border_color
                self.hours.border_color = None
            elif self.actualFocus == 'M':
                self.actualFocus = 'S'
                self.seconds.border_color = self.selected_border_color
                self.minutes.border_color = None
            else:
                self.actualFocus = 'H'
                self.hours.border_color = self.selected_border_color
                self.seconds.border_color = None
        elif e.key == 'Arrow Left':
            if self.actualFocus == 'M':
                self.actualFocus = 'H'
                self.hours.border_color = self.selected_border_color
                self.minutes.border_color = None
            elif self.actualFocus == 'S':
                self.actualFocus = 'M'
                self.minutes.border_color = self.selected_border_color
                self.seconds.border_color = None
        elif e.key == 'Arrow Right':
            if self.actualFocus == 'H':
                self.actualFocus = 'M'
                self.minutes.border_color = self.selected_border_color
                self.hours.border_color = None
            elif self.actualFocus == 'M':
                self.actualFocus = 'S'
                self.seconds.border_color = self.selected_border_color
                self.minutes.border_color = None
        elif e.key == '+':
            self.calculate('sum')
        elif e.key == '-':
            self.calculate('substract')
        elif e.key == 'Enter' or e.key == '=':
            self.calculate('result=0')
        self.update()
    
    # On focus
    def on_focus_evt(self, e):
        self.hours.focus()

    def on_text_focus(self, e):
        data = e.control.data
        self.hours.border_color = None
        self.minutes.border_color = None 
        self.seconds.border_color = None 
        if data == 'h_tf':
            self.actualFocus = 'H'
            self.hours.border_color = self.selected_border_color
        elif data == 'm_tf':
            self.actualFocus = 'M'
            self.minutes.border_color = self.selected_border_color
        else:
            self.actualFocus = 'S'
            self.seconds.border_color = self.selected_border_color
        self.update()

    
    def on_click_evt(self, e):
        data = e.control.data
        if data == 'AC':
            self.reset()
        elif data == '+':
            self.calculate('sum')
        elif data == '-':
            self.calculate('substract')
        elif data == '=':
            self.calculate('result')
        else:
            self.addNumber(data)
        self.update()
    
    def calculate(self, operator):
        value = self.text_to_ms()
        if self.actual_operator is None:
            self.value_ms = value
            self.actual_operator = operator
        else:
            if self.actual_operator == 'sum':
                self.value_ms = self.value_ms + value
                self.ms_to_text()
            elif self.actual_operator == 'substract':
                self.value_ms = self.value_ms - value
                self.ms_to_text()
        self.actual_operator = operator
        self.new_value = True
        self.actualFocus = 'H'
        self.hours.border_color = self.selected_border_color
        self.minutes.border_color = None 
        self.seconds.border_color = None

    def text_to_ms(self):
        h = int(self.hours.value) * 60 * 60 * 1000
        m = int(self.minutes.value) * 60 * 1000
        s = int(self.seconds.value) * 1000
        return h + m + s
    
    def ms_to_text(self):    
        val = self.value_ms
        if val < 0:
            self.hours.prefix_text = '-'
            val = val * -1
        else:
            self.hours.prefix_text = ''
        h = int(val / 60 / 60 / 1000)
        val = val - (h * 60 * 60 * 1000)
        m = int(val / 60 / 1000)
        val = val - (m * 60 * 1000)
        s = int(val / 1000)
        h = str(h)
        m = str(m)
        s = str(s)
        if len(h) == 1:
            h = '0' + h
        if len(m) == 1:
            m = '0' + m
        if len(s) == 1:
            s = '0' + s
        if len(h) > 4:
            dlg = ft.AlertDialog(title=ft.Text("Advertencia!"), content=ft.Text('El valor resultante supera el lìmite de 9999 horas'))
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()
            self.reset()
            self.update()
            return
        self.hours.value = h
        self.minutes.value = m
        self.seconds.value = s
        self.update()

    # Reset values
    def reset(self):
        self.actualFocus = 'H'
        self.hours.value = '00'
        self.minutes.value = '00'
        self.seconds.value = '00'
        self.hours.border_color = self.selected_border_color
        self.minutes.border_color = None 
        self.seconds.border_color = None 
        self.hours.prefix_text= ''
        self.value_ms = 0
        self.actual_operator = None