import math
import sys

class fcFloatMatic:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": '', "multiline": True}),
                "seed": ("INT", {"default": 0, "min": -1, "max": 0xffffffffffffffff, "step": 1}),
                "increment_step": ("INT", {"default": 1, "min": 1, "max": 0xffffffffffffffff, "step": 1}),
            },
            "optional": {
                "max_value": ("INT", {"default": 1, "min": 1, "max": 0xffffffffffffffff, "step": 1}),
            }
        }

    RETURN_TYPES = ("FLOAT", "STRING")  # Modified to return only FLOAT and STRING
    FUNCTION = "process_text"

    CATEGORY = "fc"
    
    def process_text(self, text, seed=0, increment_step=1, max_value=None):
        import io
        new_text = []
        for line in io.StringIO(text):
            if not line.strip().startswith('#'):
                line = line.replace("\n", '')
                if line.strip():
                    float_line = list(map(float, line.split()))
                    new_text.extend(float_line)

        output = math.floor(seed / increment_step) % (max_value or len(new_text))
        if output < 0 or output >= len(new_text):
            print(f"Invalid float index `{output}`")
            return (0.0, "Invalid float index")
        else:
            selected_float = new_text[output]
            seed += 1  # Increment the seed
            return (selected_float, str(selected_float))  # Removed second integer output

class fcFloat:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Value": ("FLOAT", {"default": 0.0, "min": -sys.float_info.max, "max": sys.float_info.max, "step": 0.1}),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    CATEGORY = "fc"
    FUNCTION = "get_value"

    def get_value(self, Value):
        return (Value,)

class fcInteger:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Value": ("FLOAT", {
                        "default": 1.0,
                        "min": -sys.float_info.max,
                        "max": sys.float_info.max,
                        "step": 1.0
                    },
                )
            },
        }

    RETURN_TYPES = ("INT",)
    CATEGORY = "fc"
    FUNCTION = "get_value"

    def get_value(self, Value):
        return (int(Value),)

class fcHex:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                'hex_code': ('STRING', {'default': ''}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "find_nearest_color"
    CATEGORY = "fc"  # Assuming the category is similar to other classes

    @staticmethod
    def hex_to_rgb(hex_code):
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def color_distance(hex1, hex2):
        rgb1 = fcHex.hex_to_rgb(hex1)
        rgb2 = fcHex.hex_to_rgb(hex2)
        return math.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(rgb1, rgb2)))

    def find_nearest_color(self, hex_code):
        colors = {
    "Brown": ["#654321", "#a52a2a"],
    "Hazel": ["#81613C", "#6B4226"],
    "Blue": ["#7BC8F6", "#0000FF"],
    "Green": ["#90EE90", "#008000"],
    "Gray": ["#C0C0C0", "#808080"],
    "Amber": ["#FFBF00", "#B8860B"],
    "Red": ["#FF0000", "#8B0000"],
    "Orange": ["#FFA500", "#FF4500"],
    "Yellow": ["#FFFF00", "#FFD700"],
    "Purple": ["#800080", "#4B0082"],
    "Pink": ["#FFC0CB", "#FF69B4"],
    "White": ["#FFFFFF", "#F8F8FF"],
    "Black": ["#000000", "#0A0A0A"],
    "Cyan": ["#00FFFF", "#40E0D0"],
    "Magenta": ["#FF00FF", "#FF1493"],
    "Teal": ["#008080", "#20B2AA"],
    "Gold": ["#FFD700", "#DAA520"]
}


        nearest_color = None
        min_distance = float('inf')

        for color, hex_range in eye_colors.items():
            for hex_range_color in hex_range:
                distance = self.color_distance(hex_code, hex_range_color)
                if distance < min_distance:
                    min_distance = distance
                    nearest_color = color

        return nearest_color

NODE_CLASS_MAPPINGS = {
    "fcFloatMatic": fcFloatMatic,
    "fcFloat": fcFloat,
    "fcInteger": fcInteger,
    "fcHex": fcHex,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "fcFloatMatic": "fcFloatMatic",
    "fcFloatNode": "fcFloat",
    "fcIntegerNode": "fcInteger",
    "fcHex": "fcHex",
}


