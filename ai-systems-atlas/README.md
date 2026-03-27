# ai-systems-atlas

        A structured collection of AI/ML projects designed for:
        - easy restart after a long break
        - fast project lookup
        - consistent execution with `uv`

        ## Repo map

        - `docs/` → guidance and restart notes
        - `templates/` → reusable project skeleton
        - `shared/` → common utilities and assets
        - `registry/` → project index
        - `domains/` → all projects grouped by domain

        ## Quick restart

        1. Open `docs/quick-restart-checklist.md`
        2. Open `registry/projects.csv`
        3. Pick a project
        4. Read that project's `PROJECT.md`
        5. Run the project using:
           ```bash
           uv sync
           uv run python -m src.app
           ```

        ## Standard idea

        Every project should feel identical from the outside.
