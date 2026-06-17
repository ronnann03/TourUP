# Graph Report - C:\Users\Ronaldinhoo\Desktop\TourUP  (2026-06-16)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 69 nodes · 66 edges · 12 communities (8 shown, 4 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 8 edges (avg confidence: 1.0)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `aebec40f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]

## God Nodes (most connected - your core abstractions)
1. `Lugar de la Memoria LUM` - 14 edges
2. `Lima` - 7 edges
3. `Cercado de Lima` - 6 edges
4. `Museo de Arte Italiano` - 6 edges
5. `Museo Jose Carlos Mariategui` - 6 edges
6. `Museo Nacional de la Cultura Peruana` - 6 edges
7. `Museo de Sitio Pucllana` - 6 edges
8. `MAC Lima` - 5 edges
9. `MALI` - 5 edges
10. `Miraflores` - 4 edges

## Surprising Connections (you probably didn't know these)
- `Pueblo Libre` --references--> `Lima`  [EXTRACTED]
  wiki/Peru/Lima/Pueblo Libre/MNAAHP/Actividades.md → CLAUDE.md
- `Ate Vitarte` --references--> `Lima`  [EXTRACTED]
  wiki/Peru/Lima/Ate Vitarte/Museo de Sitio Puruchuco/Actividades.md → CLAUDE.md
- `Barranco` --references--> `Lima`  [EXTRACTED]
  wiki/Peru/Lima/Barranco/MAC Lima/Actividades.md → CLAUDE.md
- `Cercado de Lima` --references--> `Lima`  [EXTRACTED]
  wiki/Peru/Lima/Cercado de Lima/MALI/Actividades.md → CLAUDE.md
- `Lurin` --references--> `Lima`  [EXTRACTED]
  wiki/Peru/Lima/Lurin/Museo de Sitio Pachacamac/Actividades.md → CLAUDE.md

## Import Cycles
- None detected.

## Communities (12 total, 4 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.18
Nodes (11): Recorridos guiados y talleres de ceramica y tejido, Talleres de educacion patrimonial para ninos y jovenes, Tramas andinas. Ciencia paisaje arqueologia y saberes ancestrales, Visitas guiadas por el complejo inca, Ate Vitarte, Barranco, Lima, Lurin (+3 more)

### Community 1 - "Community 1"
Cohesion: 0.14
Nodes (14): 80 anos de Naciones Unidas, Anudando la tierra con Pancho Basurco, Cine Piru. Un viaje de oro, Clausura del Festival de Cine Al Este 2026, Fiesta de la Musica 2026 Orquesta de Camara UNM, Memorias afectivas Husares de Junin, Musica y poesia con Jose Maria Salazar, Musica y poesia con Leda Quintana (+6 more)

### Community 3 - "Community 3"
Cohesion: 0.18
Nodes (12): Miercoles de Filmoteca Ciclo Nora de Izcue, Noche MALI visitas mediadas y actividades especiales, Nueva exposicion en Sala 1 primer piso, Recorrido virtual en visitavirtual.cultura.pe, Talleres visitas guiadas ferias y presentaciones artisticas, Visitas guiadas a coleccion de arte italiano, Actividades — Museo de Arte Italiano, Recorrido Virtual — Museo de Arte Italiano (+4 more)

### Community 4 - "Community 4"
Cohesion: 0.33
Nodes (7): Experiencia sonora con instrumentos originales de mas de 1500 anos, Visitas guiadas al complejo arqueologico, Experiencia Sonora — Museo de Sitio Pucllana, Actividades — Museo de Sitio Pucllana, Visita Guiada — Museo de Sitio Pucllana, Miraflores, Museo de Sitio Pucllana

### Community 5 - "Community 5"
Cohesion: 0.33
Nodes (6): Charlas y ciclos de lectura sobre pensamiento social, Recorridos por la casa-museo y exposiciones temporales, Charla — Museo Jose Carlos Mariategui, Actividades — Museo Jose Carlos Mariategui, Recorrido — Museo Jose Carlos Mariategui, Museo Jose Carlos Mariategui

### Community 6 - "Community 6"
Cohesion: 0.33
Nodes (6): Talleres ligados a festividades y danzas tradicionales, Visitas guiadas sobre arte popular y diversidad cultural, Actividades — Museo Nacional de la Cultura Peruana, Taller — Museo Nacional de la Cultura Peruana, Visita Guiada — Museo Nacional de la Cultura Peruana, Museo Nacional de la Cultura Peruana

### Community 7 - "Community 7"
Cohesion: 0.40
Nodes (5): Contemporaneo 1. Materia Alquimia Dispositivo Flujo, El Peru en clave CARETAS. 75 anos de historia fotografica, Semana de la Educacion Artistica 2026, Unsex me La deconstruccion de Lady Macbeth, MAC Lima

### Community 8 - "Community 8"
Cohesion: 0.50
Nodes (4): Talleres para familias y experiencias sensoriales, Visitas guiadas a salas de arqueologia, MNAAHP, Pueblo Libre

## Knowledge Gaps
- **50 isolated node(s):** `TourUP`, `Curator Agent`, `QA Agent`, `Suggester Agent`, `Peru` (+45 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lima` connect `Community 0` to `Community 8`, `Community 3`, `Community 4`?**
  _High betweenness centrality (0.657) - this node is a cross-community bridge._
- **Why does `Cercado de Lima` connect `Community 3` to `Community 0`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.501) - this node is a cross-community bridge._
- **Why does `Miraflores` connect `Community 4` to `Community 0`, `Community 1`?**
  _High betweenness centrality (0.423) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Museo de Arte Italiano` (e.g. with `Recorrido Virtual — Museo de Arte Italiano` and `Visita Guiada — Museo de Arte Italiano`) actually correct?**
  _`Museo de Arte Italiano` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Museo Jose Carlos Mariategui` (e.g. with `Charla — Museo Jose Carlos Mariategui` and `Recorrido — Museo Jose Carlos Mariategui`) actually correct?**
  _`Museo Jose Carlos Mariategui` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TourUP`, `Curator Agent`, `QA Agent` to the rest of the system?**
  _50 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._