import requests

from . import variables

class DTCLIPTextEncode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"text": ("STRING", {"multiline": True}), "clip": ("CLIP", )}}
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = "DoubTech/Conditioning"

    def encode(self, clip, text):
        print("DTCLIPTextEncode: " + text)
        return ([[clip.encode(variables.apply(text)), {}]], )

class StringFormat:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "string": ("STRING", {"multiline": False}),
            "format": ("STRING", {"multiline": True}),
        }}

    RETURN_TYPES = (["STRING"])
    FUNCTION = "encode"

    CATEGORY = "DoubTech/Variables"


    @classmethod
    def IS_CHANGED(s, clip, text):
        return True

    def encode(self, string, format):
        result = format.replace("$(string)", string)
        return (result,)

class StringFormatSingleLine:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "string": ("STRING", {"multiline": False}),
            "format": ("STRING", {"multiline": False, "default": "$(string)"}),
        }}

    RETURN_TYPES = ("STRING")
    FUNCTION = "encode"

    CATEGORY = "DoubTech/Variables"


    @classmethod
    def IS_CHANGED(s, clip, text):
        return True

    def encode(self, string, format):
        string = format.replace("$(string)", string)
        return (string,)

class IntVariable:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "variable": ("STRING", {"multiline": False}),
            "value": ("INT", ),
            "clip": ("CLIP", )}
        }
    RETURN_TYPES = ("CLIP","INT")
    FUNCTION = "encode"

    CATEGORY = "DoubTech/Variables"


    @classmethod
    def IS_CHANGED(s, variable, value):
        return True

    def encode(self, clip, variable, value):
        variables.state[variable] = value
        return (clip,value,)

class FloatVariable:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "variable": ("STRING", {"multiline": False}),
            "value": ("FLOAT", ),
            "clip": ("CLIP", )}
        }
    RETURN_TYPES = ("CLIP","FLOAT")
    FUNCTION = "encode"

    CATEGORY = "DoubTech/Variables"


    @classmethod
    def IS_CHANGED(s, variable, value):
        return True

    def encode(self, clip, variable, value):
        variables.state[variable] = value
        return (clip,value,)

class StringVariable:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "variable": ("STRING", {"multiline": False}),
            "value": ("STRING", {"multiline": True}),
            "clip": ("CLIP", )}
        }
    RETURN_TYPES = ("CLIP","STRING")
    FUNCTION = "encode"

    CATEGORY = "DoubTech/Variables"


    @classmethod
    def IS_CHANGED(s, variable, value):
        return True

    def encode(self, clip, variable, value):
        variables.state[variable] = value
        return (clip,value,)

class DTSingleLineStringVariable:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "variable": ("STRING", {"multiline": False}),
            "value": ("STRING", {"multiline": False}),
            "clip": ("CLIP",)}
        }

    RETURN_TYPES = ("CLIP","STRING")
    FUNCTION = "encode"

    CATEGORY = "DoubTech/Variables"


    @classmethod
    def IS_CHANGED(s, variable, value):
        return True

    def encode(self, clip, variable, value):
        variables.state[variable] = value
        return (clip, value)
class DTSingleLineStringVariableNoClip:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "variable": ("STRING", {"multiline": False}),
            "value": ("STRING", {"multiline": False})}
        }


    @classmethod
    def IS_CHANGED(s, variable, value):
        return True

    RETURN_TYPES = ()
    FUNCTION = "encode"

    CATEGORY = "DoubTech/Variables"

    def encode(self, clip, variable, value):
        variables.state[variable] = value
        return (clip,)

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "StringVariable": StringVariable,
    "DTSingleLineStringVariable": DTSingleLineStringVariable,
    "DTCLIPTextEncode": DTCLIPTextEncode,
    "DTSingleLineStringVariableNoClip": DTSingleLineStringVariableNoClip,
    "StringFormat": StringFormat,
    "StringFormatSingleLine": StringFormatSingleLine,
    "IntVariable": IntVariable,
    "FloatVariable": FloatVariable,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "StringVariable": "String",
    "IntVariable": "Int",
    "FloatVariable": "Float",
    "DTSingleLineStringVariable": "Short String",
    "DTCLIPTextEncode": "CLIP Text Encode (With Variables)",

    "StringFormat": "String Format",
    "StringFormatSingleLine": "Short String Format",
}
