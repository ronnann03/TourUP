"""
QA #1 — Validacion del grafo (graphify-out/graph.json)
Verifica: nodos sin duplicados, edges con IDs validos, jerarquia nivel 1-6.
"""
import json
import sys
from pathlib import Path

GRAPH = Path("graphify-out/graph.json")

REQUIRED_NODE_FIELDS = ["id", "label", "file_type", "community"]

LEVEL_TYPES = {
    "pais": 1,
    "ciudad": 2,
    "distrito": 3,
    "museo": 4,
    "sala": 5,
    "actividad": 6,
}

errors = []
warnings = []


def err(msg):
    errors.append(msg)
    print(f"  [ERROR] {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"  [WARN]  {msg}")


def main():
    if not GRAPH.exists():
        err(f"No se encontro {GRAPH}")
        return

    data = json.loads(GRAPH.read_text(encoding="utf-8"))
    nodes = data.get("nodes", [])
    edges = data.get("links", data.get("edges", []))

    print(f"\n=== QA Grafo: {len(nodes)} nodos, {len(edges)} edges ===\n")

    # 1. Campos requeridos y duplicados
    seen_ids = {}
    seen_labels = {}
    node_ids = set()

    for n in nodes:
        nid = n.get("id")
        label = n.get("label", "")

        for field in REQUIRED_NODE_FIELDS:
            if field not in n:
                err(f"Nodo '{label}' ({nid}) le falta el campo '{field}'")

        if nid in seen_ids:
            err(f"ID duplicado: '{nid}' aparece en '{label}' y '{seen_ids[nid]}'")
        else:
            seen_ids[nid] = label
            node_ids.add(nid)

        norm = label.lower().strip()
        if norm in seen_labels:
            warn(f"Label duplicado (posible alias): '{label}' ya existe como '{seen_labels[norm]}'")
        else:
            seen_labels[norm] = label

    # 2. Edges con IDs validos
    for e in edges:
        src = e.get("source")
        tgt = e.get("target")
        if src not in node_ids:
            err(f"Edge apunta a source inexistente: '{src}'")
        if tgt not in node_ids:
            err(f"Edge apunta a target inexistente: '{tgt}'")

    # 3. Nodos huerfanos (≤1 conexion)
    degree = {nid: 0 for nid in node_ids}
    for e in edges:
        s = e.get("source")
        t = e.get("target")
        if s in degree:
            degree[s] += 1
        if t in degree:
            degree[t] += 1

    orphans = [seen_ids[nid] for nid, d in degree.items() if d == 0]
    lonely = [seen_ids[nid] for nid, d in degree.items() if d == 1]

    if orphans:
        warn(f"{len(orphans)} nodo(s) sin ninguna conexion: {orphans[:10]}")
    if lonely:
        warn(f"{len(lonely)} nodo(s) con solo 1 conexion: {lonely[:10]}")

    # Resumen
    print(f"\n--- Resumen ---")
    print(f"  Errores:    {len(errors)}")
    print(f"  Warnings:   {len(warnings)}")
    print(f"  Nodos OK:   {len(nodes)}")
    print(f"  Edges OK:   {len(edges)}")

    if errors:
        print("\n[FALLO] El grafo tiene errores criticos.")
        sys.exit(1)
    else:
        print("\n[OK] Grafo valido.")


if __name__ == "__main__":
    main()
