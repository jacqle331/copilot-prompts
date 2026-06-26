# Contributing

Thanks for helping grow this prompt library! Here's how to add a prompt.

## Quick steps

1. Copy [`prompts/_TEMPLATE.md`](./prompts/_TEMPLATE.md) to a new file in `prompts/`.
2. Name the file using `kebab-case`, e.g. `summarize-meeting-notes.md`.
3. Fill in every section of the template.
4. Open a pull request.

## Guidelines

- **Keep it reusable.** Use `{{placeholders}}` for anything the user should swap in.
- **Be specific.** A good prompt states the role, task, context, and desired output format.
- **Test it first.** Make sure the prompt actually produces good results before submitting.
- **One prompt per file.** This keeps things easy to browse and link to.
- **No secrets or private data.** Don't include credentials, internal links, or personal information.

## Pull request checklist

- [ ] File lives in `prompts/` and uses `kebab-case`.
- [ ] All template sections are filled in.
- [ ] Prompt has been tested and works.
- [ ] No sensitive or private information included.
