"""
QA #3 — Validacion del vault (wiki/)
Verifica: frontmatter completo, campos obligatorios, tags correctos, wikilinks, slugs unicos.
"""
import re
import sys
from pathlib import Path

WIKI = Path("wiki")

# Campos obligatorios segun tipo de nota
REQUIRED_ACTIVIDAD = [
    "type", "title", "parent", "museo", "distrito",
    "ciudad", "pais", "tipo_actividad", "fecha", "costo", "tags",
]
REQUIRED_MUSEO = ["type", "title", "distrito", "ciudad", "pais", "tags"]
REQUIRED_DISTRITO = ["type", "title", "ciudad", "pais", "tags"]

WIKILINK_RE = re.compile(r"\[\[(.+?)\]\]")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

errors = []
warnings = []


def err(path, msg):
    errors.append((str(path), msg))
    print(f"  [ERROR] {path.name}: {msg}")


def warn(path, msg):
    warnings.append((str(path), msg))
    print(f"  [WARN]  {path.name}: {msg}")


def parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"')
    return fm


def check_actividad(path, fm):
    for field in REQUIRED_ACTIVIDAD:
        if field not in fm:
            err(path, f"falta campo obligatorio: '{field}'")

    tags_raw = fm.get("tags", "")
    if "actividad" not in tags_raw:
        err(path, "tags debe incluir 'actividad'")
    if "nivel-6" not in tags_raw:
        err(path, "tags debe incluir 'nivel-6'")

    for field in ["museo", "distrito", "ciudad", "pais"]:
        val = fm.get(field, "")
        if val and not WIKILINK_RE.search(val):
            warn(path, f"campo '{field}' no usa wikilink: {val}")

    fecha = fm.get("fecha", "")
    if not fecha:
        err(path, "campo 'fecha' esta vacio")


def check_museo(path, fm):
    for field in REQUIRED_MUSEO:
        if field not in fm:
            err(path, f"falta campo obligatorio: '{field}'")
    if fm.get("type") != "museo":
        err(path, f"type esperado 'museo', encontrado '{fm.get('type')}'")


def check_distrito(path, fm):
    for field in REQUIRED_DISTRITO:
        if field not in fm:
            err(path, f"falta campo obligatorio: '{field}'")
    if fm.get("type") != "distrito":
        err(path, f"type esperado 'distrito', encontrado '{fm.get('type')}'")


def main():
    md_files = list(WIKI.rglob("*.md"))
    print(f"\n=== QA Vault: {len(md_files)} archivos .md ===\n")

    seen_slugs = {}
    act_files = [f for f in md_files if f.name.startswith("Act - ")]
    museo_files = [f for f in md_files if not f.name.startswith("Act - ")
                   and f.stem not in ("Actividades", "Salas")]

    # Slugs unicos en actividades
    for f in act_files:
        slug = f.stem
        if slug in seen_slugs:
            err(f, f"slug duplicado: '{slug}' ya existe en {seen_slugs[slug]}")
        else:
            seen_slugs[slug] = f

    # Validar cada archivo
    for f in md_files:
        text = f.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)

        if fm is None:
            err(f, "no tiene frontmatter YAML valido")
            continue

        node_type = fm.get("type", "")

        if f.name.startswith("Act - "):
            if node_type != "actividad":
                err(f, f"type esperado 'actividad', encontrado '{node_type}'")
            check_actividad(f, fm)
        elif node_type == "museo":
            check_museo(f, fm)
        elif node_type == "distrito":
            check_distrito(f, fm)
        # Actividades.md y Salas.md son indices — no se validan con schema estricto

    # Resumen
    print(f"\n--- Resumen ---")
    print(f"  Archivos revisados:  {len(md_files)}")
    print(f"  Actividades (Act-):  {len(act_files)}")
    print(f"  Errores:             {len(errors)}")
    print(f"  Warnings:            {len(warnings)}")

    if errors:
        print("\n[FALLO] El vault tiene errores criticos.")
        sys.exit(1)
    else:
        print("\n[OK] Vault valido.")


if __name__ == "__main__":
    main()
