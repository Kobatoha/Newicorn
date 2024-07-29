def start_stop():
    print('press start_stop')


def lock_window():
    print('press lock_window')


def save_settings():
    print('press save_settings')
    status_bar_message('save_settings')


def load_settings():
    print('press load_settings')


def status_bar_message(message):
    if message:
        return message
    return 'status_bar_message'
