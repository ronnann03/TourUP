# TourUP — Arquitectura del Sistema

> Documento de referencia. Actualizar ante cualquier cambio estructural.

---

## Vision general

TourUP es un directorio inteligente de museos y actividades culturales de Lima, Peru.
El sistema combina un knowledge graph (vault) con un motor de recomendacion para
conectar al viajero con las actividades que mejor se adaptan a su perfil.

```
┌─────────────────────────────────────────────────┐
│                  TENANT: viajero                │
│                                                 │
│   ┌─────────────┐       ┌──────────────────┐    │
│   │ partnerScout│──────▶│  Perfil viajero  │    │
│   │  (motor de  │       │  (intereses,     │    │
│   │  recomend.) │       │   presupuesto,   │    │
│   └──────┬──────┘       │   disponibilidad)│    │
│          │              └──────────────────┘    │
│          │ consulta                             │
│          ▼                                      │
│   ┌─────────────────────────────────────────┐   │
│   │        Knowledge Graph (vault)          │   │
│   │  Peru → Lima → Distrito → Museo →       │   │
│   │  Sala → Actividad (nivel 1–6)           │   │
│   │  graphify-out/graph.json                │   │
│   └─────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

---

## Tenants

| Tenant   | Estado | Descripcion |
|----------|--------|-------------|
| viajero  | activo | Turista / usuario final. Accede a recomendaciones via partnerScout |

> Tenants futuros: TBD (museo, admin)

---

## Modulo: partnerScout

**Tenant:** viajero
**Rol:** Motor de recomendacion personalizada de actividades culturales

### Que hace
- Recibe el perfil del viajero (intereses, presupuesto, disponibilidad)
- Consulta el knowledge graph para extraer actividades candidatas
- Rankea y filtra segun criterios del perfil
- Devuelve un shortlist de actividades recomendadas

### Inputs
| Campo | Fuente |
|-------|--------|
| Actividades disponibles | `graphify-out/graph.json` (nodos nivel 6) |
| Perfil del viajero | Entrada del usuario (TBD — formulario / API) |

### Outputs
- Lista ordenada de actividades con: museo, distrito, tipo, fecha, costo
- Wikilinks a las notas canonicas en `wiki/`

### Estado
- [ ] Especificacion de perfil del viajero
- [ ] Logica de scoring / ranking
- [ ] Integracion con el grafo
- [ ] API / interfaz de salida

---

## Capa de datos: Knowledge Graph

| Nivel | Tipo       | Ejemplo                  |
|-------|------------|--------------------------|
| 1     | pais       | Peru                     |
| 2     | ciudad     | Lima                     |
| 3     | distrito   | Miraflores, Barranco     |
| 4     | museo      | MALI, MAC Lima           |
| 5     | sala       | Sala 1, Sala permanente  |
| 6     | actividad  | Noche MALI, Filmoteca    |

**Fuentes de datos:**
- `wiki/Peru/Lima/<Distrito>/<Museo>/` — notas canonicas en Markdown
- `sources/` — datos brutos CSV
- `inbox/` — entrada al pipeline de ingesta

**Grafo compilado:** `graphify-out/graph.json` (69 nodos, 66 edges — junio 2026)

---

## Agentes del sistema

| Agente    | Rol |
|-----------|-----|
| curator   | Curar contenido y detectar nodos huerfanos |
| qa        | Verificar frontmatter, links y consistencia del grafo |
| suggester | Proponer nuevas notas basadas en el grafo |

Definidos en `AGENTS.md`.

---

## QA

Pipeline automatico en `.github/workflows/qa.yml`. Corre en cada push/PR a `main`:

| Check | Script | Que valida |
|-------|--------|------------|
| Grafo | `qa/validate_graph.py` | IDs unicos, edges validos, nodos huerfanos |
| Vault | `qa/validate_vault.py` | Frontmatter completo, campos obligatorios, wikilinks, slugs unicos |

---

## Decisiones de diseno

| Decision | Razon |
|----------|-------|
| Un solo tenant (viajero) | Scope inicial — simplifica autorizacion y modelo de datos |
| partnerScout en tenant viajero | La recomendacion es una funcion del consumidor, no del proveedor |
| Knowledge graph como fuente unica | Evita duplicacion — el vault es la fuente de verdad |
| Markdown + frontmatter YAML | Compatible con Obsidian, versionable en git, legible por agentes |
