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
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.animation import Animation
import random
from datetime import datetime

# Technical gibberish dictionaries - full set from terminal version
VERBS = ["Calibrating", "Syncing", "Handshaking", "Negotiating", "Buffering",
         "Optimizing", "Aligning", "Polling", "Querying", "Validating",
         "Propagating", "Transcoding", "Multiplexing", "Demodulating"]

NOUNS = ["phase array", "Fresnel zone", "carrier signal", "packet stream",
         "quantum buffer", "harmonic resonance", "baseband", "sideband",
         "cryptographic nonce", "handshake token", "CRC checksum",
         "latency profile", "attenuation curve", "spectral density"]

ADJECTIVES = ["adaptive", "dynamic", "orthogonal", "differential", "coherent",
              "asynchronous", "bidirectional", "multi-path", "low-latency",
              "high-gain", "wideband", "narrowband", "spread-spectrum"]

SYSTEMS = ["autonomous subsystem", "CAN bus bridge", "sensor fusion module",
           "telemetry aggregator", "diagnostic relay", "safety interlock",
           "beacon transponder", "mesh node", "gateway controller"]

MENU_OPTIONS = [
    ("Initialize Autonomous Link", "link"),
    ("Calibrate Sensor Array", "sensor"),
    ("Sync Fleet Telemetry", "fleet"),
    ("Validate Safety Interlocks", "safety"),
    ("Run Diagnostic Sweep", "diag"),
    ("Optimize Signal Path", "signal"),
    ("Reset Mesh Topology", "mesh"),
    ("Emergency Override (DANGER)", "danger"),
]

class MantisApp(App):
    def build(self):
        Window.clearcolor = (0.05, 0.05, 0.08, 1)
        self.main_screen = MainScreen()
        return self.main_screen

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        # Header
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=100)
        title = Label(
            text='[b]G R E E B L E   T O O L[/b]',
            markup=True,
            font_size='22sp',
            color=(0.3, 0.8, 1, 1),
            size_hint_y=0.5
        )
        subtitle = Label(
            text='v2.7.1-RC3 | Autonomous Systems Diagnostic Interface',
            font_size='12sp',
            color=(0.6, 0.7, 0.8, 1),
            size_hint_y=0.25
        )
        session = Label(
            text=f'Session: {datetime.now().strftime("%Y-%m-%d %H:%M")}',
            font_size='10sp',
            color=(0.5, 0.5, 0.6, 1),
            size_hint_y=0.25
        )
        header.add_widget(title)
        header.add_widget(subtitle)
        header.add_widget(session)
        self.add_widget(header)
        
        # Separator
        sep = Label(size_hint_y=None, height=2)
        self.add_widget(sep)
        
        # Menu grid
        grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        for text, action in MENU_OPTIONS:
            btn = Button(
                text=text,
                size_hint_y=None,
                height=70,
                background_color=(0.15, 0.25, 0.35, 1),
                background_normal='',
                color=(0.9, 0.9, 0.9, 1)
            )
            btn.bind(on_press=lambda x, a=action: self.run_operation(a))
            grid.add_widget(btn)
        
        scroll = ScrollView()
        scroll.add_widget(grid)
        self.add_widget(scroll)
        
        # Quit button
        quit_btn = Button(
            text='EXIT SYSTEM',
            size_hint_y=None,
            height=60,
            background_color=(0.4, 0.15, 0.15, 1),
            background_normal='',
            color=(0.9, 0.9, 0.9, 1)
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
        self.padding = 15
        self.spacing = 10
        self.main_screen = main_screen
        self.action = action
        self.log_lines = []
        self.step = 0
        self.max_steps = random.randint(4, 7)
        self.progress_anim = None
        
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
        
        # Target info
        target = random.choice(SYSTEMS).upper()
        self.target_label = Label(
            text=f'Target: {target}',
            font_size='12sp',
            size_hint_y=None,
            height=25,
            color=(0.6, 0.7, 0.8, 1)
        )
        self.add_widget(self.target_label)
        
        # Log area with border effect
        log_container = BoxLayout(orientation='vertical', padding=5)
        log_container.background_color = (0.08, 0.08, 0.12, 1)
        
        self.log_label = Label(
            text='> Initializing sequence...',
            font_size='11sp',
            size_hint_y=None,
            valign='top',
            halign='left',
            text_size=(None, None),
            color=(0.7, 0.85, 0.7, 1),
            markup=True
        )
        self.log_label.bind(texture_size=self._update_text_size)
        
        scroll = ScrollView()
        scroll.add_widget(self.log_label)
        log_container.add_widget(scroll)
        self.add_widget(log_container)
        
        # Progress bar container
        progress_box = BoxLayout(orientation='vertical', size_hint_y=None, height=50, padding=(0, 10))
        self.progress = ProgressBar(max=100, value=0, height=20)
        self.progress_label = Label(
            text='0%',
            font_size='12sp',
            size_hint_y=None,
            height=20,
            color=(0.6, 0.8, 1, 1)
        )
        progress_box.add_widget(self.progress)
        progress_box.add_widget(self.progress_label)
        self.add_widget(progress_box)
        
        # Password area (initially hidden)
        self.password_box = BoxLayout(orientation='vertical', size_hint_y=None, height=0, opacity=0)
        
        auth_header = Label(
            text='[b]AUTHORIZATION REQUIRED[/b]',
            markup=True,
            font_size='14sp',
            size_hint_y=None,
            height=30,
            color=(1, 0.8, 0.3, 1)
        )
        
        self.password_label = Label(
            text='Enter override code to proceed:',
            size_hint_y=None,
            height=25,
            color=(0.8, 0.8, 0.8, 1)
        )
        
        self.password_input = TextInput(
            multiline=False,
            password=True,
            size_hint_y=None,
            height=50,
            background_color=(0.1, 0.1, 0.15, 1),
            foreground_color=(0.9, 0.9, 0.9, 1),
            cursor_color=(0.3, 0.8, 1, 1),
            padding=(10, 10)
        )
        
        self.submit_btn = Button(
            text='AUTHORIZE',
            size_hint_y=None,
            height=55,
            background_color=(0.2, 0.5, 0.3, 1),
            background_normal='',
            color=(0.9, 0.9, 0.9, 1)
        )
        self.submit_btn.bind(on_press=self.check_password)
        
        self.password_box.add_widget(auth_header)
        self.password_box.add_widget(self.password_label)
        self.password_box.add_widget(self.password_input)
        self.password_box.add_widget(self.submit_btn)
        self.add_widget(self.password_box)
        
        # Back button
        self.back_btn = Button(
            text='CANCEL OPERATION',
            size_hint_y=None,
            height=55,
            background_color=(0.4, 0.25, 0.15, 1),
            background_normal='',
            color=(0.9, 0.9, 0.9, 1)
        )
        self.back_btn.bind(on_press=self.go_back)
        self.add_widget(self.back_btn)
        
        # Start the operation sequence
        Clock.schedule_once(self.run_step, 0.3)
    
    def _update_text_size(self, instance, value):
        instance.text_size = (instance.width, None)
    
    def add_log(self, text):
        self.log_lines.append(f'> {text}')
        # Keep last 15 lines
        display_text = '\n'.join(self.log_lines[-15:])
        self.log_label.text = display_text
    
    def random_gibberish_line(self):
        """Generate a line of plausible technical nonsense"""
        templates = [
            f"{random.choice(VERBS)} {random.choice(ADJECTIVES)} {random.choice(NOUNS)}...",
            f"{random.choice(VERBS)} {random.choice(SYSTEMS)} handshake...",
            f"{random.choice(ADJECTIVES).capitalize()} {random.choice(NOUNS)} detected: {random.randint(1000, 9999)}ms",
            f"Querying {random.choice(SYSTEMS)}... [{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}]",
            f"CRC validation: 0x{random.randint(0x1000, 0xFFFF):04X}",
            f"Latency check: {random.uniform(2.5, 45.3):.2f}ms (acceptable)",
            f"Signal strength: -{random.randint(45, 85)} dBm",
            f"Channel {random.randint(1, 165)}: {random.choice(['clear', 'congested', 'optimal'])}",
        ]
        return random.choice(templates)
    
    def animate_progress(self, target_value, duration=0.5):
        """Animate progress bar to target value"""
        current = self.progress.value
        step_count = int(duration * 30)  # 30 fps
        step_size = (target_value - current) / step_count
        
        def update_progress(dt, steps_remaining=[step_count]):
            if steps_remaining[0] > 0:
                self.progress.value += step_size
                self.progress_label.text = f'{int(self.progress.value)}%'
                steps_remaining[0] -= 1
                return True
            else:
                self.progress.value = target_value
                self.progress_label.text = f'{int(target_value)}%'
                return False
        
        Clock.schedule_interval(update_progress, 1/30)
    
    def run_step(self, dt):
        if self.step < self.max_steps:
            # Generate gibberish
            self.add_log(self.random_gibberish_line())
            
            # Animate progress
            target_pct = ((self.step + 1) / self.max_steps) * 80  # Save 20% for final steps
            self.animate_progress(target_pct, random.uniform(0.3, 0.6))
            
            self.step += 1
            Clock.schedule_once(self.run_step, random.uniform(0.4, 0.9))
        else:
            # Final progress
            self.animate_progress(100, 0.8)
            Clock.schedule_once(self.show_final_status, 1.0)
    
    def show_final_status(self, dt):
        self.add_log("[color=00ff00]STATUS: LINK ESTABLISHED[/color]")
        self.add_log(f"Encryption: AES-{random.choice([128, 256, 512])}-GCM")
        self.add_log(f"Session key: {''.join(random.choices('0123456789ABCDEF', k=32))}")
        Clock.schedule_once(self.show_password_prompt, 0.5)
    
    def show_password_prompt(self, dt):
        self.back_btn.disabled = True
        self.back_btn.opacity = 0.3
        
        # Animate password box appearance
        self.password_box.height = 200
        anim = Animation(opacity=1, duration=0.3)
        anim.start(self.password_box)
        
        self.password_input.focus = True
    
    def check_password(self, instance):
        # Any password works - just show accepting state briefly
        self.submit_btn.text = 'VERIFYING...'
        self.submit_btn.disabled = True
        Clock.schedule_once(self.show_success, 0.8)
    
    def show_success(self, dt):
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
        self.spacing = 15
        self.main_screen = main_screen
        
        # Top spacer
        self.add_widget(Label(size_hint_y=0.15))
        
        # Success icon/text
        success_box = BoxLayout(orientation='vertical', size_hint_y=None, height=200)
        
        check = Label(
            text='[b]✓[/b]',
            markup=True,
            font_size='60sp',
            color=(0.2, 0.9, 0.4, 1),
            size_hint_y=0.4
        )
        
        success_text = Label(
            text='[b]AUTHORIZATION ACCEPTED[/b]',
            markup=True,
            font_size='16sp',
            color=(0.2, 0.9, 0.4, 1),
            size_hint_y=0.2
        )
        
        success_box.add_widget(check)
        success_box.add_widget(success_text)
        self.add_widget(success_box)
        
        # Main message box
        message_box = BoxLayout(orientation='vertical', padding=20, size_hint_y=None, height=180)
        
        header = Label(
            text='[b]OPERATION SUCCESSFUL[/b]',
            markup=True,
            font_size='20sp',
            color=(0.3, 0.8, 1, 1),
            size_hint_y=0.3
        )
        
        message = Label(
            text='Work safe.\nWatch your step.\nYour family wants you home for dinner.',
            font_size='14sp',
            halign='center',
            color=(0.85, 0.85, 0.85, 1),
            size_hint_y=0.7
        )
        
        message_box.add_widget(header)
        message_box.add_widget(message)
        self.add_widget(message_box)
        
        # Middle spacer
        self.add_widget(Label(size_hint_y=0.2))
        
        # Done button
        done_btn = Button(
            text='RETURN TO MAIN MENU',
            size_hint_y=None,
            height=70,
            background_color=(0.2, 0.45, 0.7, 1),
            background_normal='',
            color=(0.9, 0.9, 0.9, 1)
        )
        done_btn.bind(on_press=self.finish)
        self.add_widget(done_btn)
        
        # Bottom text
        safety = Label(
            text='Remember: Safety third.',
            font_size='11sp',
            color=(0.5, 0.5, 0.6, 1),
            size_hint_y=None,
            height=30
        )
        self.add_widget(safety)
    
    def finish(self, instance):
        self.main_screen.clear_widgets()
        self.main_screen.add_widget(MainScreen())

if __name__ == '__main__':
    MantisApp().run()
