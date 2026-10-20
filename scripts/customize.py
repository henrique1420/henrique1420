from pathlib import Path
import json
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
config = json.loads((ROOT / "profile.config.json").read_text(encoding="utf-8"))
readme = (ROOT / "README.md").read_text(encoding="utf-8")

def url(value):
    if not isinstance(value, str):
        raise ValueError("URLs must be strings.")
    if not value:
        return ""
    if re.search(r'[\s<>"()]', value):
        raise ValueError("URL contains unsupported characters.")
    parsed = urlsplit(value)
    if (
        parsed.scheme != "https"
        or not parsed.hostname
        or parsed.username
        or parsed.password
    ):
        raise ValueError("Use a public HTTPS URL without credentials.")
    return value

def replace_block(name, content):
    global readme
    pattern = (
        rf"<!-- {name}:START -->.*?"
        rf"<!-- {name}:END -->"
    )
    replacement = (
        f"<!-- {name}:START -->\n"
        f"{content}\n"
        f"<!-- {name}:END -->"
    )
    readme, count = re.subn(
        pattern, lambda _: replacement, readme, flags=re.S
    )
    if count != 1:
        raise ValueError(f"Expected exactly one {name} block.")

contacts = ["[GitHub](https://github.com/henrique1420)"]

for key, label in (("website", "HenrStudio"), ("linkedin", "LinkedIn")):
    value = url(config.get(key, ""))
    if value:
        contacts.append(f"[{label}]({value})")

email = config.get("email", "")
if not isinstance(email, str):
    raise ValueError("Email must be a string.")
if email:
    if not re.fullmatch(r"[^@\s<>()]+@[^@\s<>()]+\.[^@\s<>()]+", email):
        raise ValueError("Invalid email.")
    contacts.append(f"[Email](mailto:{email})")

replace_block("CONTACT", " · ".join(contacts))

projects = config.get("projects", {})
for key in ("vozlink", "escala_justa", "henrstudio"):
    value = url(projects.get(key, ""))
    replace_block(
        key.upper(),
        f"[Explore project]({value})" if value else "",
    )

enabled = config.get("snake_enabled", False)
if not isinstance(enabled, bool):
    raise ValueError("snake_enabled must be true or false.")

base = "https://raw.githubusercontent.com/henrique1420/henrique1420/output"

snake = f"""<picture>
  <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="{base}/snake-dark-static.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="{base}/snake-light-static.svg">
  <source media="(prefers-color-scheme: dark)" srcset="{base}/snake-dark.svg">
  <img src="{base}/snake-light.svg" width="100%" alt="Snake animation generated from Henrique's actual GitHub contribution calendar.">
</picture>

[View the static contribution graphic]({base}/snake-light-static.svg)."""

replace_block("SNAKE", snake if enabled else "")

(ROOT / "README.md").write_text(readme, encoding="utf-8")
print("README updated. No Git commands or network requests were executed.")
