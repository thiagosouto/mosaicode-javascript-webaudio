from mosaicode.model.port import Port

class String(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "javascript"
        self.label = "STR"
        self.color = "#000"
        self.multiple = True
        self.code = "$output$.push($input$);\n"
        self.var_name = "block_$id$_$conn_type$$port_number$"
