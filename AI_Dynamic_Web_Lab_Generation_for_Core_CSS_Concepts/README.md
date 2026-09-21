# AI: Dynamic Web Lab Generation for Core CSS Concepts

Interactive single-file HTML/CSS/JS labs generated with sequential AI prompting to visualize the CSS Box Model, the `display` property, Flexbox and Grid.

**AI tool used:** Claude (Anthropic), via claude.ai. Each lab is one self-contained `.html` file with no dependencies.

## Files

| File | What it is |
| --- | --- |
| `box-model-lab-initial.html` | Output of prompt 1. Box 1 and Box 2, sliders for padding, margin, border-width and width (one value for all sides), and a `display` dropdown (block, inline-block, inline). Content, padding, border and margin each have their own colour. |
| `box-model-lab-refined.html` | Output of prompt 2 (refinement). Adds separate top/right/bottom/left sliders for margin, padding and border, plus a corner-radius slider. Also has a "Link all sides" toggle and a reset button. |
| `flexbox-grid-playground.html` | Output of prompt 3. A container with five items and dropdowns for `display`, `flex-direction`, `justify-content`, `align-items` and `grid-template-columns`, updating in real time. |

## How to run

Open any `.html` file in a browser. No build step or server needed.

## Prompts used

### 1. Initial Box Model lab

```
Act as a frontend web developer. Using your Canvas tool, Generate an interactive website that can be used for understanding the CSS Box Model and its relationship with the display property.

The page must have:

1. Two div elements, 'Box 1' and 'Box 2', so I can see how they interact. 'Box 1' will be the one we control.
2. The CSS must use different background colors for the content area, the padding area, and the margin area of 'Box 1' (e.g., using background-clip: content-box). The border should be a solid line.
3. A control panel with:
- Sliders to control the padding, margin, border-width, and width of 'Box 1'.
- Labels next to the sliders that show the current pixel value.
- A Dropdown (select) to change the display property of 'Box 1' to: block, inline-block, and inline.
4. JavaScript that listens to all sliders and the dropdown, and updates the CSS properties of 'Box 1' in real-time.
```

### 2. Refinement (side-specific controls)

```
Implement sliders to adjust the margin, padding, and border for each side (top, right, bottom, left) individually, and add a separate slider for the corner radius.
```

### 3. Flexbox and Grid playground

```
Act as a frontend web developer. Using your Canvas tool, generate an interactive website that can be used as a playground for CSS Flexbox and Grid.

The page should have:

1. A `div` element acting as the container.
2. Several `div` elements inside acting as the items (e.g., 5 items).
3. Dropdown menus (selects) that allow me to change the CSS properties of the container.
4. I need to be able to change:
- display (to switch between block, flex, and grid)
- flex-direction (row, column)
- justify-content (flex-start, center, space-between, etc.)
- align-items (flex-start, center, stretch, etc.)
- grid-template-columns (e.g., 1fr 1fr, 1fr 1fr 1fr)
5. The JavaScript must update the container's CSS in real-time when I change a dropdown.
```

## What changed between the initial and refined Box Model lab

- The four uniform sliders became twelve per-side sliders (margin, padding, border) plus corner radius, generated from one config array instead of hand-written markup.
- The margin overlay now takes a separate offset for each side.
- For `display: inline`, top and bottom margin are ignored, matching how browsers treat inline boxes.

## What each lab shows

- **Box model:** total footprint = content + padding + border + margin. The generated-CSS panel and size readout update as you drag.
- **display:** `block` takes the full row, `inline-block` sits beside Box 2 and keeps width and vertical margin, `inline` ignores width and vertical margin.
- **Flexbox/Grid:** `justify-content` works along the main axis, `align-items` across it, and `flex-direction: column` swaps the two. Options that do not apply to the current `display` value are greyed out.
