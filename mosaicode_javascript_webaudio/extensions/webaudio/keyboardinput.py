#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the KeyboardInput class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class KeyboardInput(BlockModel):

    # --------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = "Keyboard Input"
        self.label = "Keyboard Input"
        self.color = "50:150:250:150"
        self.ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "label":"Float Output",
                "conn_type":"Output",
                "name":"float_output"},
                {"type":"mosaicode_javascript_webaudio.extensions.ports.char",
                "label":"Char Output",
                "conn_type":"Output",
                "name":"char_output"}
            ]
        self.group = "Interface"

        self.codes["declaration"] = """
// block_$id$ = KeyBoard Input
var $port[char_output]$ = [];
var $port[float_output]$ = [];
"""
        self.codes["execution"] = """
document.onkeypress = function(evt){
    evt = evt || window.event;
    var value = evt.keyCode || evt.which;
    for (var i = 0; i < $port[float_output]$.length ; i++){
        $port[float_output]$[i](value);
    }
    value = String.fromCharCode(value);
    for (var i = 0; i < $port[char_output]$.length ; i++){
        $port[char_output]$[i](value);
    }
};
"""
