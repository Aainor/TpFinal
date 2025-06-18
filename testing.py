from nicegui import ui
@ui.page('/')
def index():
    ui.label('Hola mundo')
ui.run()