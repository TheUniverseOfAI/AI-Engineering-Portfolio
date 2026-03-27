from __future__ import annotations

from pathlib import Path
import csv
import textwrap

# =========================================================
# Config
# =========================================================

REPO_NAME = "ai-systems-atlas"

DOMAINS = [
    "01_foundations",
    "02_ml",
    "03_deep_learning",
    "04_nlp",
    "05_computer_vision",
    "06_time_series",
    "07_recommendation",
    "08_anomaly_detection",
    "09_rl",
    "10_genai_llm",
    "11_mlops_deployment",
    "12_fullstack_ai",
]

# Optional sample projects to generate immediately
SAMPLE_PROJECTS = [
    ("02_ml", "001_linear_regression_from_scratch", "Beginner ML project"),
    ("02_ml", "002_house_price_prediction", "Regression project"),
    ("04_nlp", "001_sentiment_analysis_baseline", "NLP classification project"),
    ("10_genai_llm", "001_rag_pdf_qa", "RAG starter project"),
]

PYTHON_VERSION = "3.12"


# =========================================================
# Helpers
# =========================================================

def write_file(path: Path, content: str, overwrite: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return
    path.write_text(content.strip() + "\n", encoding="utf-8")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def slug_to_title(slug: str) -> str:
    parts = slug.split("_", 1)
    core = parts[1] if len(parts) > 1 and parts[0].isdigit() else slug
    return core.replace("_", " ").title()


# =========================================================
# Root files
# =========================================================

def create_root(repo_root: Path) -> None:
    ensure_dir(repo_root)

    write_file(
        repo_root / "README.md",
        f"""
        # {REPO_NAME}

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
        """,
    )

    write_file(
        repo_root / ".gitignore",
        """
        # Python
        __pycache__/
        *.py[cod]
        *.pyo
        *.pyd
        .Python
        .pytest_cache/
        .mypy_cache/
        .ruff_cache/

        # Virtual environments
        .venv/
        venv/
        env/

        # Jupyter
        .ipynb_checkpoints/

        # OS / editor
        .DS_Store
        Thumbs.db
        .vscode/
        .idea/

        # Build artifacts
        build/
        dist/
        *.egg-info/

        # Local outputs
        outputs/
        models/
        data/raw/
        data/processed/

        # Env files
        .env
        """,
    )

    write_file(repo_root / ".python-version", PYTHON_VERSION)

    write_file(
        repo_root / "pyproject.toml",
        f"""
        [project]
        name = "{REPO_NAME}"
        version = "0.1.0"
        description = "AI/ML multi-project repository"
        requires-python = ">={PYTHON_VERSION}"
        dependencies = []

        [tool.uv]
        package = false
        """,
    )


# =========================================================
# Shared folders and docs
# =========================================================

def create_docs_and_shared(repo_root: Path) -> None:
    dirs = [
        "docs",
        "templates/project-template",
        "shared/utils",
        "shared/configs",
        "shared/datasets",
        "shared/scripts",
        "shared/components",
        "experiments/scratch",
        "experiments/archived",
        "registry",
        "domains",
    ]
    for d in dirs:
        ensure_dir(repo_root / d)

    write_file(
        repo_root / "docs" / "how-to-use-this-repo.md",
        """
        # How to Use This Repo

        ## Purpose
        This repo is designed to stay understandable even after long breaks.

        ## Rule
        Every project follows the same folder structure.

        ## Fast navigation
        - Use `registry/projects.csv` to find a project quickly
        - Read `PROJECT.md` before opening code
        - Use the standard run command:
          ```bash
          uv sync
          uv run python -m src.app
          ```
        """,
    )

    write_file(
        repo_root / "docs" / "project-map.md",
        """
        # Project Map

        Projects are grouped into domain folders inside `domains/`.

        Example:
        - `domains/02_ml/001_linear_regression_from_scratch`
        - `domains/04_nlp/001_sentiment_analysis_baseline`
        - `domains/10_genai_llm/001_rag_pdf_qa`
        """,
    )

    write_file(
        repo_root / "docs" / "naming-rules.md",
        """
        # Naming Rules

        ## Project naming
        Use:
        `NNN_short_descriptive_name`

        Examples:
        - `001_linear_regression_from_scratch`
        - `002_customer_churn_classification`
        - `015_text_classification_transformer`

        ## Why
        - easier memory
        - easier sorting
        - easier lookup
        """,
    )

    write_file(
        repo_root / "docs" / "quick-restart-checklist.md",
        """
        # Quick Restart Checklist

        1. Read the root `README.md`
        2. Open `registry/projects.csv`
        3. Pick one project
        4. Read its `PROJECT.md`
        5. Run:
           ```bash
           uv sync
           uv run python -m src.app
           ```
        6. Check `outputs/`
        7. Update project notes if needed
        """,
    )

    write_file(
        repo_root / "registry" / "tags.md",
        """
        # Tags

        Suggested tags:
        - beginner
        - intermediate
        - advanced
        - sklearn
        - pytorch
        - tensorflow
        - fastapi
        - rag
        - nlp
        - cv
        - deployment
        - tabular
        - time-series
        """,
    )


# =========================================================
# Domain folders
# =========================================================

def create_domains(repo_root: Path) -> None:
    domains_root = repo_root / "domains"
    for domain in DOMAINS:
        ensure_dir(domains_root / domain)


# =========================================================
# Project template
# =========================================================

def create_project_template(repo_root: Path) -> None:
    template_root = repo_root / "templates" / "project-template"

    dirs = [
        "src",
        "notebooks",
        "data/raw",
        "data/processed",
        "models",
        "outputs",
        "configs",
        "tests",
        "scripts",
    ]
    for d in dirs:
        ensure_dir(template_root / d)

    write_file(
        template_root / "README.md",
        """
        # Project Name

        ## What this project does

        ## Why it exists

        ## Folder structure

        ## Setup
        ```bash
        uv sync
        ```

        ## Run
        ```bash
        uv run python -m src.app
        ```

        ## Results

        ## What to study here

        ## Next improvements
        """,
    )

    write_file(
        template_root / "PROJECT.md",
        """
        # Project Card

        ## Goal
        Describe the project goal.

        ## Type
        Classical ML / Deep Learning / NLP / CV / GenAI

        ## Domain
        Classification / Regression / Forecasting / RAG / etc.

        ## Stack
        Python

        ## Dataset
        Add dataset name here.

        ## Entry Point
        `uv run python -m src.app`

        ## Quick Start
        ```bash
        uv sync
        uv run python -m src.app
        ```

        ## What To Review First
        1. README.md
        2. notebooks/
        3. src/app.py

        ## Output
        - metrics in `outputs/`
        - plots in `outputs/`

        ## Status
        planned

        ## Tags
        beginner
        """,
    )

    write_file(
        template_root / "pyproject.toml",
        f"""
        [project]
        name = "project-template"
        version = "0.1.0"
        description = "Template project"
        requires-python = ">={PYTHON_VERSION}"
        dependencies = []

        [tool.uv]
        package = false
        """,
    )

    write_file(template_root / ".python-version", PYTHON_VERSION)

    write_file(
        template_root / "src" / "__init__.py",
        """
        """,
    )

    write_file(
        template_root / "src" / "app.py",
        """
        def main() -> None:
            print("Project is running.")

        if __name__ == "__main__":
            main()
        """,
    )

    write_file(
        template_root / "configs" / "config.yaml",
        """
        project_name: project-template
        debug: true
        """,
    )

    write_file(
        template_root / "tests" / "test_smoke.py",
        """
        def test_smoke():
            assert True
        """,
    )

    write_file(
        template_root / "scripts" / "run.sh",
        """
        #!/usr/bin/env bash
        uv sync
        uv run python -m src.app
        """,
    )

    write_file(
        template_root / "scripts" / "run.ps1",
        """
        uv sync
        uv run python -m src.app
        """,
    )


# =========================================================
# Real projects
# =========================================================

def create_project(repo_root: Path, domain: str, project_slug: str, description: str = "") -> Path:
    project_root = repo_root / "domains" / domain / project_slug

    dirs = [
        "src",
        "notebooks",
        "data/raw",
        "data/processed",
        "models",
        "outputs",
        "configs",
        "tests",
        "scripts",
    ]
    for d in dirs:
        ensure_dir(project_root / d)

    title = slug_to_title(project_slug)

    write_file(
        project_root / "README.md",
        f"""
        # {title}

        ## What this project does
        {description or "Describe the project here."}

        ## Why it exists
        This project is part of the structured AI/ML repository.

        ## Folder structure
        - `src/` → code
        - `notebooks/` → exploration
        - `data/` → raw and processed data
        - `models/` → trained artifacts
        - `outputs/` → figures, metrics, logs
        - `configs/` → config files
        - `tests/` → tests
        - `scripts/` → helper run scripts

        ## Setup
        ```bash
        uv sync
        ```

        ## Run
        ```bash
        uv run python -m src.app
        ```

        ## Results

        ## What to study here

        ## Next improvements
        """,
    )

    write_file(
        project_root / "PROJECT.md",
        f"""
        # Project Card

        ## Goal
        {description or "Describe the goal of this project."}

        ## Type
        AI/ML Project

        ## Domain
        {domain}

        ## Stack
        Python

        ## Dataset
        Add dataset details here.

        ## Entry Point
        `uv run python -m src.app`

        ## Quick Start
        ```bash
        uv sync
        uv run python -m src.app
        ```

        ## What To Review First
        1. README.md
        2. notebooks/
        3. src/app.py

        ## Output
        - metrics in `outputs/`
        - plots in `outputs/`

        ## Status
        planned

        ## Tags
        add, tags, here
        """,
    )

    write_file(
        project_root / "pyproject.toml",
        f"""
        [project]
        name = "{project_slug}"
        version = "0.1.0"
        description = "{description or title}"
        requires-python = ">={PYTHON_VERSION}"
        dependencies = []

        [tool.uv]
        package = false
        """,
    )

    write_file(project_root / ".python-version", PYTHON_VERSION)

    write_file(project_root / "src" / "__init__.py", "")

    write_file(
        project_root / "src" / "app.py",
        f"""
        def main() -> None:
            print("Running project: {project_slug}")

        if __name__ == "__main__":
            main()
        """,
    )

    write_file(
        project_root / "configs" / "config.yaml",
        f"""
        project_name: {project_slug}
        debug: true
        """,
    )

    write_file(
        project_root / "tests" / "test_smoke.py",
        """
        def test_smoke():
            assert True
        """,
    )

    write_file(
        project_root / "scripts" / "run.sh",
        """
        #!/usr/bin/env bash
        uv sync
        uv run python -m src.app
        """,
    )

    write_file(
        project_root / "scripts" / "run.ps1",
        """
        uv sync
        uv run python -m src.app
        """,
    )

    return project_root


# =========================================================
# Registry
# =========================================================

def create_registry(repo_root: Path, sample_projects: list[tuple[str, str, str]]) -> None:
    registry_path = repo_root / "registry" / "projects.csv"
    registry_path.parent.mkdir(parents=True, exist_ok=True)

    rows = [
        {
            "id": slug.split("_", 1)[0] if "_" in slug else "",
            "name": slug,
            "domain": domain,
            "level": "",
            "status": "planned",
            "entry_point": "uv run python -m src.app",
            "tags": "",
            "description": description,
        }
        for domain, slug, description in sample_projects
    ]

    with registry_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "id",
                "name",
                "domain",
                "level",
                "status",
                "entry_point",
                "tags",
                "description",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


# =========================================================
# Main
# =========================================================

def main() -> None:
    repo_root = Path(REPO_NAME)

    create_root(repo_root)
    create_docs_and_shared(repo_root)
    create_domains(repo_root)
    create_project_template(repo_root)

    for domain, slug, description in SAMPLE_PROJECTS:
        create_project(repo_root, domain, slug, description)

    create_registry(repo_root, SAMPLE_PROJECTS)

    print(f"Created repository structure at: {repo_root.resolve()}")
    print()
    print("Next steps:")
    print(f"  cd {REPO_NAME}")
    print("  uv sync")
    print("  cd domains/02_ml/001_linear_regression_from_scratch")
    print("  uv sync")
    print("  uv run python -m src.app")


if __name__ == "__main__":
    main()