# cat-cog

**Cognitive assessment and visual scoring powered by LLMs.**

`cat-cog` provides LLM-powered evaluation of hand-drawn images for neuropsychological testing. It builds on [cat-stack](https://github.com/chrissoria/cat-stack), the shared classification engine for the [CatLLM](https://github.com/chrissoria/cat-llm) ecosystem.

## Installation

```bash
pip install cat-cog
```

This automatically installs `cat-stack` (the LLM classification engine).

## CERAD Constructional Praxis Scoring

Score hand-drawn shapes (circle, diamond, overlapping rectangles, cube) using LLM vision models. The function sends images to the LLM, classifies drawing features, then applies CERAD scoring rules.

```python
from cat_cog import cerad_drawn_score

# Score circle drawings (max score: 2)
results = cerad_drawn_score(
    shape="circle",
    image_input="./circle_drawings/",
    api_key=OPENAI_KEY,
    user_model="gpt-4o",
)
print(results[["image_file", "score"]])
```

### Supported shapes

| Shape | Max Score | Features Assessed |
|-------|-----------|-------------------|
| circle | 2 | Closure, circularity |
| diamond | 3 | 4 sides, equal sides, resemblance |
| rectangles | 2 | Overlap, crossing pattern |
| cube | 4 | Front face, internal lines, parallel faces, 3D quality |

### Using with multiple models

All `cat_stack.classify()` parameters are available via `**kwargs`:

```python
results = cerad_drawn_score(
    shape="cube",
    image_input="./cube_drawings/",
    api_key=OPENAI_KEY,
    models=[
        ("gpt-4o", "openai", OPENAI_KEY),
        ("claude-sonnet-4-20250514", "anthropic", ANTHROPIC_KEY),
    ],
)
```

## Future

- Fine-tuned vision models for shape quality assessment (circle classifier, etc.)
- Additional cognitive screening instruments (clock drawing tests, etc.)

## Ecosystem

| Package | Domain |
|---------|--------|
| **cat-stack** | General-purpose classification engine (base) |
| **cat-cog** | Cognitive assessment & visual scoring (this package) |
| **cat-survey** | Survey response classification |
| **cat-vader** | Social media text |
| **cat-ademic** | Academic papers & PDFs |
| **cat-pol** | Political text |

## License

GPL-3.0-or-later
