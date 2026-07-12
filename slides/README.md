Slides folder — simple slide source and conversion notes.

We provide a simple Markdown slide source `simple_slides.md` that can be converted to PowerPoint or PDF.

To convert with Pandoc (if installed):

```bash
pandoc slides/simple_slides.md -t pptx -o release/promptlab_pitch.pptx
```

Or use Marp / Reveal.js for HTML slides.

