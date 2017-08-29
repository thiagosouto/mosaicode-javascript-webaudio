#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Random(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = "Random"
        self.label = "Random"
        self.color = "150:150:250:150"
        self.out_ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "label":"Float",
                "name":"float"}
            ]
        self.in_ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "label":"Generate",
                "name":"generate"}
            ]
        self.group = "Interface"

        self.properties = [{"name": "min",
                            "label": "Min",
                            "type": MOSAICODE_FLOAT,
                            "lower": -20000,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "max",
                            "label": "Max",
                            "type": MOSAICODE_FLOAT,
                            "lower": -20000,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            }
                           ]

        self.codes["declaration"] = """
// block_$id$ = $label$
var block_$id$_min = $prop[min]$;
var block_$id$_max = $prop[max]$;
var $out_ports[float]$ = [];

var $in_ports[generate]$ = function(value){
    value = Math.floor((Math.random() * (block_$id$_max - block_$id$_min)) + block_$id$_min);
    for (var i = 0; i < $out_ports[float]$.length ; i++){
        $out_ports[float]$[i](value);
    }
    return true;
    };

"""
