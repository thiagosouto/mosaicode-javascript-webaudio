#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class FloatValue(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = "Double value"
        self.label = "FloatValue"
        self.color = "50:150:250:150"
        self.ports = [{"type":"mosaicode_lib_javascript_webaudio.extensions.ports.float",
                "label":"Float",
                "conn_type":"Output",
                "name":"float"},
                {"type":"mosaicode_lib_javascript_webaudio.extensions.ports.float",
                "label":"Float",
                "conn_type":"Input",
                "name":"input"}
                ]
        self.group = "Interface"

        self.properties = [{"name": "value",
                            "label": "Value",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "min",
                            "label": "Min",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "max",
                            "label": "Max",
                            "type": MOSAICODE_FLOAT,
                            "lower": 00,
                            "upper": 20000,
                            "step": 1,
                            "value": 10
                            },
                           {"name": "label",
                            "label": "Label",
                            "type": MOSAICODE_STRING,
                            "value": "Label"
                            }
                           ]

        self.codes["declaration"] = """
// block_$id$ = Float Value
var block_$id$_value = $prop[value]$;
var $port[float]$ = [];

var $port[input]$ = function(value){
    document.getElementById("block_$id$").value = value;
    change$id$_value(value);
    return true;
    };

"""
        self.codes["execution"] = """
function change$id$_value(){
    value = document.getElementById("block_$id$").value;
    for (var i = 0; i < $port[float]$.length ; i++){
        $port[float]$[i](value);
    }
};
"""
        self.codes["html"] = """
$prop[label]$ <input type="number" id="block_$id$" value="$prop[value]$" min="$prop[min]$"
        max="$prop[max]$" onChange="change$id$_value();"><br>
"""

