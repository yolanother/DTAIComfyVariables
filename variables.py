state = dict()
generated_prompt = None


def apply(text, defaultStateField=None):
    global state

    def replace_variable(match):
        variable = match.group(0)  # Get the full variable text, e.g., "$(name)" or "$(name:default_value)"
        variable = variable[2:-1]  # Remove the "$( ... )" surrounding parentheses

        parts = variable.split(":")
        name = parts[0]
        default_value = parts[1] if len(parts) > 1 else None

        if name in state:
            return str(state[name])  # Replace with the value from the state dictionary
        elif default_value is not None:
            return default_value  # Replace with the default value

        if variable == "undefined" or variable == None:
            return ""
        return variable  # No replacement, return the original variable text

    import re
    pattern = r"\$\(.*?\)"  # Regular expression pattern to match the variable text

    try:
        text = re.sub(pattern, replace_variable, text)
    except Exception as e:
        print(e)

    if (text == '' or text is None) and defaultStateField is not None and defaultStateField in state:
        text = state[defaultStateField]

    return text
