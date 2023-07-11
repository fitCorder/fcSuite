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

NODE_CLASS_MAPPINGS = {
    "fcFloatMatic": fcFloatMatic,
    "fcFloat": fcFloat,
    "fcInteger": fcInteger,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "fcFloatMatic": "fcFloatMatic",
    "fcFloatNode": "fcFloat",
    "fcIntegerNode": "fcInteger",
}
