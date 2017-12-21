#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Midi2Freq class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class MulSoundFloat(BlockModel):

    # --------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = " Mul Sound Float"
        self.label = "Mul Sound Float"
        self.color = "250:250:0:150"
        self.group = "Sound"

        self.ports = [{"type": "mosaicode_lib_javascript_webaudio.extensions.ports.sound",
                       "name": "sound_input",
                       "conn_type": "Input",
                       "label": "Sound"},
                      {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.float",
                       "name": "float_input",
                       "conn_type": "Input",
                       "label": "Float Value"},
                      {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.sound",
                       "label": "Sound",
                       "conn_type": "Output",
                       "name": "output"}
                      ]

        self.codes["function"] = """
MulSoundFloat = function(context, float_value) {
    var that = this;
    this.float = float_value;
    this.context = context;
    this.node = context.createScriptProcessor(1024, 1, 1);
    this.node.onaudioprocess = function(e) { that.process(e) };
}

MulSoundFloat.prototype.process = function(e) {
    var in0 = e.inputBuffer.getChannelData(0);
    var out = e.outputBuffer.getChannelData(0);
    for (var i = 0; i < in0.length; ++i) {
        out[i] = in0[i] * this.float;
    }
}
"""
        self.codes["declaration"] = """
// block_$id$ = $label$

var block_$id$_float = 0;
var $port[float_input]$ = function(value){
    block_$id$_float = parseFloat(value);
    return true;
    };

var block_$id$_obj = new MulSoundFloat(context, block_$id$_float);
var $port[sound_input]$ = block_$id$_obj.node;
var $port[output]$ = block_$id$_obj.node;
"""
