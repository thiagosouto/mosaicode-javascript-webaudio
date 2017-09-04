#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Button class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Button(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = "Button"
        self.label = "Button"
        self.color = "50:150:250:150"
        self.ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "label":"Click",
                "conn_type":"Output",
                "name":"click"}
            ]
        self.properties = [{"name": "value",
                            "label": "Value",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "label",
                            "label": "Label",
                            "type": MOSAICODE_STRING,
                            "value": "Label"
                            }
                           ]
        self.group = "Interface"

        self.codes["declaration"] = """
// block_$id$ = $label$
var block_$id$_value = $prop[value]$;
var $port[click]$ = [];
"""

        self.codes["execution"] = """
function click_$id$(){
    value = document.getElementById("block_$id$").value;
    for (var i = 0; i < $port[click]$.length ; i++){
        $port[click]$[i](value);
    }
};
"""

        self.codes["html"] = """
<button type="button" value="$prop[value]$" onClick="click_$id$();"
id="block_$id$">$prop[label]$</button><br>
"""

