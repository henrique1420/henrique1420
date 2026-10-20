from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
NS = "http://www.w3.org/2000/svg"

ET.register_namespace("", NS)

reduce_css = """
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
  .s { display: none !important; }
}
"""

static_css = """
* { animation: none !important; transition: none !important; }
.s { display: none !important; }
"""

for theme in ("light", "dark"):
    path = DIST / f"snake-{theme}.svg"
    if not path.is_file() or path.stat().st_size == 0:
        raise RuntimeError(f"Missing SVG: {path.name}")

    original = path.read_text(encoding="utf-8")
    if "<!DOCTYPE" in original or "<!ENTITY" in original:
        raise RuntimeError("Unexpected XML declaration.")

    tree = ET.fromstring(original)
    if tree.tag != f"{{{NS}}}svg":
        raise RuntimeError("Invalid SVG root.")

    for element in tree.iter():
        local = element.tag.split("}")[-1]
        if local in ("script", "foreignObject"):
            raise RuntimeError(f"Unexpected SVG element: {local}")
        for attribute in element.attrib:
            if attribute.split("}")[-1].lower().startswith("on"):
                raise RuntimeError("Unexpected SVG event handler.")

    tree.set("role", "img")
    tree.set("aria-labelledby", "snake-title snake-description")

    title = ET.Element(f"{{{NS}}}title", {"id": "snake-title"})
    title.text = "Henrique Oliveira — GitHub contribution calendar"
    tree.insert(0, title)

    description = ET.Element(
        f"{{{NS}}}desc", {"id": "snake-description"}
    )
    description.text = (
        "Generated from actual GitHub contribution data using Platane/snk. "
        "The animation does not represent additional contributions."
    )
    tree.insert(1, description)

    style = ET.SubElement(tree, f"{{{NS}}}style")
    style.text = reduce_css
    animated = ET.tostring(tree, encoding="unicode")
    ET.fromstring(animated)
    path.write_text(animated + "\n", encoding="utf-8")

    style.text = static_css
    frozen = ET.tostring(tree, encoding="unicode")
    ET.fromstring(frozen)
    (DIST / f"snake-{theme}-static.svg").write_text(
        frozen + "\n", encoding="utf-8"
    )

print("Validated animated and static SVGs for both themes.")
