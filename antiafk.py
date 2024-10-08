import ctypes as ct
import ctypes.wintypes as cw
import time
import random

# Windows constants
LRESULT = ct.c_long
WH_KEYBOARD_LL = 13
WH_MOUSE_LL = 14
WM_KEYDOWN = 0x0100
WM_MOUSEMOVE = 0x0200
WM_LBUTTONDOWN = 0x0201
WM_RBUTTONDOWN = 0x0204

class KBDLLHOOKSTRUCT(ct.Structure):
    _fields_ = [
        ("vk_code", cw.DWORD),
        ("scan_code", cw.DWORD),
        ("flags", cw.DWORD),
        ("time", cw.DWORD),
        ("extra_info", ct.POINTER(cw.ULONG)),
    ]

class MSLLHOOKSTRUCT(ct.Structure):
    _fields_ = [
        ("point", cw.POINT),
        ("mouse_data", cw.DWORD),
        ("flags", cw.DWORD),
        ("time", cw.DWORD),
        ("extra_info", ct.POINTER(cw.ULONG)),
    ]

class ActivityTimer:
    def __init__(self):
        self.timeout = 30  # Inactivity timeout in seconds
        self.last_activity_time = time.time()
        self.running = True
        self.user32 = ct.windll.user32
        self.keyboard_hook = None
        self.mouse_hook = None
        self.start_time = 0
        self.duration = 0
        self.start_pos = (0, 0)
        self.control_point = (0, 0)
        self.end_pos = (0, 0)
        self.is_moving = False
        self.next_move_time = 0
        self.use_bezier = True
        self.screen_size = self.get_screen_size()

    def keyboard_proc(self, n_code, w_param, l_param):
        if n_code == 0 and w_param == WM_KEYDOWN:
            self.on_activity()
        return self.user32.CallNextHookEx(self.keyboard_hook, n_code, w_param, l_param)

    def mouse_proc(self, n_code, w_param, l_param):
        if n_code == 0 and w_param in (WM_MOUSEMOVE, WM_LBUTTONDOWN, WM_RBUTTONDOWN):
            self.on_activity()
        return self.user32.CallNextHookEx(self.mouse_hook, n_code, w_param, l_param)

    def on_activity(self):
        self.last_activity_time = time.time()
        self.is_moving = False

    def check_inactivity(self):
        current_time = time.time()
        if current_time - self.last_activity_time > self.timeout and not self.is_moving and current_time >= self.next_move_time:
            self.start_cursor_move()

    def get_screen_size(self):
        return (self.user32.GetSystemMetrics(0), self.user32.GetSystemMetrics(1))

    def get_random_point(self):
        return (random.randint(0, self.screen_size[0]), random.randint(0, self.screen_size[1]))

    def set_cursor_pos(self, x, y):
        self.user32.SetCursorPos(int(x), int(y))

    def get_cursor_pos(self):
        point = cw.POINT()
        self.user32.GetCursorPos(ct.byref(point))
        return (point.x, point.y)

    @staticmethod
    def quadratic_bezier(p0, p1, p2, t):
        return tuple((1-t)**2 * p0[i] + 2*(1-t)*t * p1[i] + t**2 * p2[i] for i in range(2))

    def start_cursor_move(self):
        self.start_time = time.time()
        self.duration = random.uniform(0.5, 1.0)
        self.start_pos = self.get_cursor_pos()
        self.end_pos = self.get_random_point()
        self.control_point = self.get_random_point()
        self.is_moving = True
        self.use_bezier = random.choice([True, False])

    def update_cursor_pos(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        
        if elapsed_time >= self.duration:
            self.set_cursor_pos(*self.end_pos)
            self.is_moving = False
            self.next_move_time = current_time + random.uniform(0, 5)
        else:
            t = elapsed_time / self.duration
            if self.use_bezier:
                current_pos = self.quadratic_bezier(self.start_pos, self.control_point, self.end_pos, t)
            else:
                current_pos = tuple(self.start_pos[i] + (self.end_pos[i] - self.start_pos[i]) * t for i in range(2))
            self.set_cursor_pos(*map(int, current_pos))

    def run(self):
        # Set up keyboard and mouse hooks
        self.keyboard_callback = ct.CFUNCTYPE(LRESULT, ct.c_int, cw.WPARAM, ct.POINTER(KBDLLHOOKSTRUCT))(self.keyboard_proc)
        self.mouse_callback = ct.CFUNCTYPE(LRESULT, ct.c_int, cw.WPARAM, ct.POINTER(MSLLHOOKSTRUCT))(self.mouse_proc)

        self.keyboard_hook = self.user32.SetWindowsHookExA(WH_KEYBOARD_LL, self.keyboard_callback, None, 0)
        self.mouse_hook = self.user32.SetWindowsHookExA(WH_MOUSE_LL, self.mouse_callback, None, 0)

        if not self.keyboard_hook or not self.mouse_hook:
            print("Failed to set hooks")
            return

        try:
            msg = cw.MSG()
            while self.running:
                # Process Windows messages
                if self.user32.PeekMessageA(ct.byref(msg), None, 0, 0, 1) != 0:
                    self.user32.TranslateMessage(ct.byref(msg))
                    self.user32.DispatchMessageA(ct.byref(msg))
                
                self.check_inactivity()
                if self.is_moving:
                    self.update_cursor_pos()
                
                time.sleep(0.01)  # Small sleep to reduce CPU usage
        except KeyboardInterrupt:
            print("Program interrupted by user")
        finally:
            # Clean up hooks
            if self.keyboard_hook:
                self.user32.UnhookWindowsHookEx(self.keyboard_hook)
            if self.mouse_hook:
                self.user32.UnhookWindowsHookEx(self.mouse_hook)

if __name__ == "__main__":
    timer = ActivityTimer()
    timer.run()