from shiny import ui, render, App

ui = ui.page_fluid(
    ui.input_text("t_entry","Input text:",value="Hello World"),
    ui.output_ui("t_out",class_="display-6 text-left") #left justified, 7 will be <p>
)

def server(input,output,session):
    @output
    @render.ui
    def t_out():
        return input.t_entry()

#must be named `app`
app = App(ui,server)