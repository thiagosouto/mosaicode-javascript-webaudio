#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Inc(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = "Increment"
        self.label = "Increment"
        self.color = "150:150:250:150"
        self.out_ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "label":"Float",
                "name":"float"}
            ]
        self.in_ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "label":"Count",
                "name":"count"},
                {"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "label":"Value",
                "name":"value"}
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
                           {"name": "step",
                            "label": "Step",
                            "type": MOSAICODE_FLOAT,
                            "lower": -20000,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            }
                           ]

        self.codes["declaration"] = """
// block_$id$ = $label$
var block_$id$_value = $prop[value]$;
var block_$id$_step = $prop[step]$;
var $out_ports[float]$ = [];

var $in_ports[count]$ = function(value){
    block_$id$_value += block_$id$_step;
    for (var i = 0; i < $out_ports[float]$.length ; i++){
        $out_ports[float]$[i](block_$id$_value);
    }
    return true;
    };

var $in_ports[value]$ = function(value){
    block_$id$_value = value;
    return true;
    };

"""
