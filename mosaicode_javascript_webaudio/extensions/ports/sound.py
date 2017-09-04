from mosaicode.model.port import Port

class Sound(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "javascript"
        self.label = "SOUND"
        self.color = "#F00"
        self.multiple = True
        self.code = "$output$.connect($input$);\n"
        self.var_name = "block_$id$_$conn_type$$port_number$"
