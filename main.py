import win32gui, win32con, win32api

def draw_text(text):
    hdc = win32gui.GetDC(0)
    
    logfont = win32gui.LOGFONT()
    logfont.lfFaceName = "微软雅黑"
    logfont.lfHeight = -36
    hfont = win32gui.CreateFontIndirect(logfont)
    win32gui.SelectObject(hdc, hfont)

    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)

    rect = (10, screen_height + 240, 200, screen_height + 100)
    win32gui.DrawText(hdc, text, -1, rect, win32con.DT_LEFT | win32con.DT_BOTTOM | win32con.DT_SINGLELINE | win32con.DT_NOCLIP)
    win32gui.ReleaseDC(0, hdc)

def get_lock_status():
    caps_lock = win32api.GetKeyState(0x14) & 1 == 1
    num_lock = win32api.GetKeyState(0x90) & 1 == 1
    return caps_lock, num_lock

def main():
    prev_caps_lock, prev_num_lock = get_lock_status()
    try:
        while True:
            caps_lock, num_lock = get_lock_status()
            if caps_lock != prev_caps_lock:
                draw_text(f'Caps Lock: {"On" if caps_lock else "Off"}')
                prev_caps_lock = caps_lock
            if num_lock != prev_num_lock:
                draw_text(f'Num Lock: {"On" if num_lock else "Off"}')
                prev_num_lock = num_lock
            win32api.Sleep(100)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
