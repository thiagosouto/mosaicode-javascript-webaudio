#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Float(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = "O que vai no help"
        self.label = "Float"
        self.color = "150:50:150:150"
        self.group = "Types"
        self.ports = [{"type":"mosaicode_lib_javascript_webaudio.extensions.ports.float",
                        "conn_type":"Output",
                        "name":"thiago",
                        "label":"Value"}
                        ]

        self.properties = [{"name": "ronne",
                            "label": "Value",
                            "value": "0",
                            "type": MOSAICODE_FLOAT
                            }]

        self.codes["onload"] = """
load_float$id$();
        """

        self.codes["declaration"] = """
var $port[thiago]$ = [];

function load_float$id$(){
    for (var i = 0 ; i < $port[thiago]$.length ; i++)
        $port[thiago]$[i]($prop[ronne]$);
};

"""
