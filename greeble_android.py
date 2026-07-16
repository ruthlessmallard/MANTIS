#!/usr/bin/env python3
"""
Greeble Tool - Android/Kivy Version
Touch-friendly, looks official, scares off copycats.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty
import random
import time

# Technical gibberish
VERBS = ["Calibrating", "Syncing", "Handshaking", "Negotiating", "Buffering",
         "Optimizing", "Aligning", "Polling", "Querying", "Validating"]
NOUNS = ["phase array", "Fresnel zone", "carrier signal", "packet stream",
         "quantum buffer", "harmonic resonance", "baseband", "sideband"]
ADJECTIVES = ["adaptive", "dynamic", "orthogonal", "differential", "coherent",
              "asynchronous", "bidirectional", "multi-path"]
SYSTEMS = ["autonomous subsystem", "CAN bus bridge", "sensor fusion module",
           "telemetry aggregator", "diagnostic relay", "safety interlock"]

MENU_OPTIONS = [
    ("Initialize Autonomous Link", "link"),
    ("Calibrate Sensor Array", "sensor"),
    ("Sync Fleet Telemetry", "fleet"),
    ("Validate Safety Interlocks", "safety"),
    ("Run Diagnostic Sweep", "diag"),
    ("Optimize Signal Path", "signal"),
    ("Reset Mesh Topology", "mesh"),
    ("Emergency Override", "danger"),
]

class LogLabel(Label):
    pass

class MantisApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.15, 1)
        return MainScreen()

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        # Header
        header = Label(
            text='[b]GREEBLE TOOL[/b]\nv2.7.1-RC3\nAutonomous Systems Interface',
            markup=True,
            font_size='18sp',
            size_hint_y=None,
            height=80,
            color=(0.3, 0.8, 1, 1)
        )
        self.add_widget(header)
        
        # Menu grid
        grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        for text, action in MENU_OPTIONS:
            btn = Button(
                text=text,
                size_hint_y=None,
                height=80,
                background_color=(0.2, 0.3, 0.4, 1)
            )
            btn.bind(on_press=lambda x, a=action: self.run_operation(a))
            grid.add_widget(btn)
        
        scroll = ScrollView()
        scroll.add_widget(grid)
        self.add_widget(scroll)
        
        # Quit button
        quit_btn = Button(
            text='EXIT',
            size_hint_y=None,
            height=60,
            background_color=(0.5, 0.2, 0.2, 1)
        )
        quit_btn.bind(on_press=self.quit_app)
        self.add_widget(quit_btn)
    
    def run_operation(self, action):
        self.clear_widgets()
        self.add_widget(OperationScreen(action, self))
    
    def quit_app(self, instance):
        App.get_running_app().stop()

class OperationScreen(BoxLayout):
    def __init__(self, action, main_screen, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.main_screen = main_screen
        
        # Title
        self.title = Label(
            text='[b]OPERATION IN PROGRESS[/b]',
            markup=True,
            font_size='20sp',
            size_hint_y=None,
            height=40,
            color=(0.3, 0.8, 1, 1)
        )
        self.add_widget(self.title)
        
        # Log area
        self.log_label = Label(
            text='Initializing...',
            font_size='12sp',
            size_hint_y=None,
            valign='top',
            halign='left',
            text_size=(None, None),
            color=(0.8, 0.9, 0.8, 1)
        )
        self.log_label.bind(texture_size=self._update_text_size)
        
        scroll = ScrollView()
        scroll.add_widget(self.log_label)
        self.add_widget(scroll)
        
        # Progress bar
        self.progress = ProgressBar(max=100, value=0, size_hint_y=None, height=30)
        self.add_widget(self.progress)
        
        # Password area (initially hidden)
        self.password_box = BoxLayout(orientation='vertical', size_hint_y=None, height=0)
        self.password_label = Label(text='Enter authorization code:', size_hint_y=None, height=30)
        self.password_input = TextInput(
            multiline=False,
            password=True,
            size_hint_y=None,
            height=50
        )
        self.submit_btn = Button(
            text='AUTHORIZE',
            size_hint_y=None,
            height=60,
            background_color=(0.2, 0.6, 0.3, 1)
        )
        self.submit_btn.bind(on_press=self.check_password)
        
        self.password_box.add_widget(self.password_label)
        self.password_box.add_widget(self.password_input)
        self.password_box.add_widget(self.submit_btn)
        self.add_widget(self.password_box)
        
        # Back button (hidden during operation)
        self.back_btn = Button(
            text='CANCEL',
            size_hint_y=None,
            height=60,
            background_color=(0.5, 0.3, 0.2, 1)
        )
        self.back_btn.bind(on_press=self.go_back)
        self.add_widget(self.back_btn)
        
        # Start the fake operation
        self.log_lines = []
        self.step = 0
        Clock.schedule_once(self.run_step, 0.5)
    
    def _update_text_size(self, instance, value):
        instance.text_size = (instance.width, None)
    
    def add_log(self, text):
        self.log_lines.append(text)
        self.log_label.text = '\n'.join(self.log_lines[-20:])  # Keep last 20 lines
    
    def run_step(self, dt):
        if self.step < 6:
            # Generate gibberish
            templates = [
                f"{random.choice(VERBS)} {random.choice(ADJECTIVES)} {random.choice(NOUNS)}...",
                f"Querying {random.choice(SYSTEMS)}...",
                f"Latency: {random.uniform(2.5, 45.3):.2f}ms",
                f"Signal: -{random.randint(45, 85)} dBm",
                f"Channel {random.randint(1, 165)}: {random.choice(['clear', 'optimal'])}",
            ]
            self.add_log(random.choice(templates))
            self.progress.value = (self.step / 6) * 100
            self.step += 1
            Clock.schedule_once(self.run_step, random.uniform(0.3, 0.8))
        else:
            self.progress.value = 100
            self.add_log("STATUS: LINK ESTABLIZED")
            self.add_log(f"Session: {''.join(random.choices('0123456789ABCDEF', k=16))}")
            self.show_password_prompt()
    
    def show_password_prompt(self):
        self.back_btn.disabled = True
        self.password_box.height = 140
        self.password_box.opacity = 1
        self.password_input.focus = True
    
    def check_password(self, instance):
        # Any password works
        self.clear_widgets()
        self.add_widget(SuccessScreen(self.main_screen))
    
    def go_back(self, instance):
        self.main_screen.clear_widgets()
        self.main_screen.add_widget(MainScreen())

class SuccessScreen(BoxLayout):
    def __init__(self, main_screen, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20
        self.main_screen = main_screen
        
        # Big success message
        self.add_widget(Label(text='', size_hint_y=0.2))
        
        success = Label(
            text='[b]✓ OPERATION SUCCESSFUL[/b]',
            markup=True,
            font_size='28sp',
            color=(0.2, 0.9, 0.4, 1)
        )
        self.add_widget(success)
        
        message = Label(
            text='Work safe.\nWatch your step.\nYour family wants you home.',
            font_size='16sp',
            halign='center',
            color=(0.9, 0.9, 0.9, 1)
        )
        self.add_widget(message)
        
        self.add_widget(Label(text='', size_hint_y=0.3))
        
        done_btn = Button(
            text='DONE',
            size_hint_y=None,
            height=80,
            background_color=(0.2, 0.5, 0.8, 1)
        )
        done_btn.bind(on_press=self.finish)
        self.add_widget(done_btn)
    
    def finish(self, instance):
        self.main_screen.clear_widgets()
        self.main_screen.add_widget(MainScreen())

if __name__ == '__main__':
    MantisApp().run()
