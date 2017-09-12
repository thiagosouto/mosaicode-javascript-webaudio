#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Print class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Print(BlockModel):

    # --------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = "Print value"
        self.label = "Print"
        self.color = "50:150:250:150"
        self.ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "name":"float_value",
                "conn_type":"Input",
                "label":"Float Value"},
                {"type":"mosaicode_javascript_webaudio.extensions.ports.char",
                "conn_type":"Input",
                "name":"char_value",
                "label":"Char Value"},
                {"type":"mosaicode_javascript_webaudio.extensions.ports.color",
                "conn_type":"Input",
                "name":"color_value",
                "label":"Color Value"}
                ]
        self.group = "Interface"

        self.properties = [{"name": "label",
                            "label": "Label",
                            "value": "Label",
                            "type": MOSAICODE_STRING
                            }
                           ]

        self.codes["declaration"] = """
// $label$
var $port[float_value]$ = function(value){
    document.getElementById("block_$id$").innerHTML = value;
    return true;
    };
var $port[char_value]$ = $port[float_value]$;
var $port[color_value]$ = $port[float_value]$;
"""
        self.codes["html"] = """
$prop[label]$ <span id="block_$id$"></span><br>
"""
