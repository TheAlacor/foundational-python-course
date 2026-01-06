from rich.console import Console
from rich.text import Text
import time

console = Console()

message = "Hello, future Programmer"

for letter in message:
    console.print(Text(letter, style="Bold magenta"), end="")
    time.sleep(0.1)
