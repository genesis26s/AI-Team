class CLIParser:
    """
    Parses user input and determines whether it is
    a CLI command or a normal AI request.
    """

    COMMAND_PREFIX = "/"

    def is_command(self, text: str) -> bool:

        if not text:
            return False

        return text.strip().startswith(self.COMMAND_PREFIX)

    def parse(self, text: str):

        text = text.strip()

        if not self.is_command(text):
            return {
                "type": "chat",
                "input": text,
            }

        parts = text.split()

        command = parts[0][1:].lower()

        arguments = parts[1:]

        return {
            "type": "command",
            "command": command,
            "args": arguments,
            "raw": text,
        }


parser = CLIParser()
