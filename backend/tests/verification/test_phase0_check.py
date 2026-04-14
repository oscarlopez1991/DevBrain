"""
╔══════════════════════════════════════════════════════════════════════════╗
║                    PHASE 0 VERIFICATION TESTS                          ║
║                                                                        ║
║  These tests verify that your development environment is correctly     ║
║  configured and all infrastructure services are running.               ║
║                                                                        ║
║  Run: make verify-phase0                                               ║
║   or: cd backend && uv run pytest tests/verification/test_phase0_check.py -v  ║
║                                                                        ║
║  Target: 8/8 tests passing                                             ║
╚══════════════════════════════════════════════════════════════════════════╝

━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
pytest is Python's most popular testing framework. Key differences from
xUnit/NUnit in .NET:

- No [TestClass] attribute → just name the file test_*.py and class Test*
- No [TestMethod] attribute → just name the function test_*
- No Assert.AreEqual() → use plain Python `assert` statements
- Fixtures (setup/teardown) use decorators, not constructor/dispose
- pytest auto-discovers tests by naming convention

Run with -v for verbose output showing each test name and result.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import os
import subprocess
from pathlib import Path

import pytest

# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Helper to get the project root directory.
# Path(__file__) gives us the current test file's path.
# .parent.parent.parent navigates up: verification/ → tests/ → backend/
# .parent one more time gets us to the monorepo root (DevBrain/)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
BACKEND_DIR = Path(__file__).parent.parent.parent


class TestPhase0ProjectStructure:
    """Verify that the monorepo structure is correctly set up."""

    def test_root_readme_exists(self) -> None:
        """The project README.md must exist at the root."""
        readme = PROJECT_ROOT / "README.md"
        assert readme.exists(), (
            f"README.md not found at {readme}. "
            "This is the first file anyone sees on GitHub!"
        )

    def test_gitignore_exists(self) -> None:
        """.gitignore must exist to prevent committing secrets and artifacts."""
        gitignore = PROJECT_ROOT / ".gitignore"
        assert gitignore.exists(), ".gitignore not found at project root."

    def test_env_example_exists(self) -> None:
        """.env.example must exist as a template for environment variables."""
        env_example = PROJECT_ROOT / ".env.example"
        assert env_example.exists(), (
            ".env.example not found. New developers need this template!"
        )

    def test_env_example_contains_required_vars(self) -> None:
        """.env.example must contain all required environment variables."""
        env_example = PROJECT_ROOT / ".env.example"
        content = env_example.read_text()

        required_vars = [
            "DATABASE_URL",
            "REDIS_URL",
            "GOOGLE_API_KEY",
            "GROQ_API_KEY",
            "HUGGINGFACE_API_KEY",
            "AUTH_SECRET",
        ]

        for var in required_vars:
            assert var in content, (
                f"Missing {var} in .env.example. "
                "All required config vars must be documented."
            )

    def test_makefile_exists(self) -> None:
        """Makefile must exist as the project command interface."""
        makefile = PROJECT_ROOT / "Makefile"
        assert makefile.exists(), "Makefile not found at project root."

    def test_docker_compose_exists(self) -> None:
        """docker-compose.yml must exist for service orchestration."""
        compose = PROJECT_ROOT / "docker-compose.yml"
        assert compose.exists(), "docker-compose.yml not found."


class TestPhase0BackendStructure:
    """Verify the backend project scaffolding."""

    def test_pyproject_toml_exists(self) -> None:
        """pyproject.toml must exist with uv configuration."""
        pyproject = BACKEND_DIR / "pyproject.toml"
        assert pyproject.exists(), "backend/pyproject.toml not found."

    def test_pyproject_uses_uv_not_poetry(self) -> None:
        """
        pyproject.toml should NOT reference Poetry.
        We use uv exclusively for dependency management.
        """
        pyproject = BACKEND_DIR / "pyproject.toml"
        content = pyproject.read_text()
        assert "[tool.poetry]" not in content, (
            "Found [tool.poetry] in pyproject.toml. "
            "We use uv exclusively — remove Poetry configuration."
        )

    def test_main_app_exists(self) -> None:
        """The FastAPI entry point must exist."""
        main = BACKEND_DIR / "app" / "main.py"
        assert main.exists(), "backend/app/main.py not found."

    def test_config_exists(self) -> None:
        """The configuration module must exist."""
        config = BACKEND_DIR / "app" / "config.py"
        assert config.exists(), "backend/app/config.py not found."

    def test_backend_packages_exist(self) -> None:
        """All backend sub-packages must have __init__.py files."""
        packages = [
            "app",
            "app/api",
            "app/api/v1",
            "app/models",
            "app/schemas",
            "app/services",
            "app/ai",
            "app/core",
        ]
        for pkg in packages:
            init_file = BACKEND_DIR / pkg / "__init__.py"
            assert init_file.exists(), (
                f"Missing __init__.py in backend/{pkg}/. "
                "Python packages require this file."
            )

    def test_dockerfile_exists(self) -> None:
        """Backend Dockerfile must exist for containerization."""
        dockerfile = BACKEND_DIR / "Dockerfile"
        assert dockerfile.exists(), "backend/Dockerfile not found."


class TestPhase0FastAPIApp:
    """Verify the FastAPI application starts and responds correctly."""

    def test_fastapi_app_importable(self) -> None:
        """The FastAPI app must be importable without errors."""
        try:
            from app.main import app

            assert app is not None
        except ImportError as e:
            pytest.fail(
                f"Cannot import FastAPI app: {e}. "
                "Check that all dependencies are installed (uv sync)."
            )

    def test_settings_loadable(self) -> None:
        """Settings must load without errors (using defaults)."""
        try:
            from app.config import settings

            assert settings.APP_NAME == "DevBrain"
        except Exception as e:
            pytest.fail(f"Cannot load settings: {e}")

    def test_health_endpoint_exists(self) -> None:
        """The /health endpoint must be registered."""
        from app.main import app

        routes = [route.path for route in app.routes]
        assert "/health" in routes, (
            "/health endpoint not found. "
            "This is required for Docker healthcheck and monitoring."
        )


class TestPhase0DockerInfrastructure:
    """
    Verify Docker services are running.

    CHECK: These tests require `docker compose up -d` to be running.
    If they fail, run `make up` first, then re-run the verification.
    """

    @pytest.mark.skipif(
        os.environ.get("CI") == "true",
        reason="Docker services not available in CI",
    )
    def test_postgres_is_reachable(self) -> None:
        """PostgreSQL must be running and accepting connections."""
        try:
            result = subprocess.run(
                [
                    "docker",
                    "compose",
                    "exec",
                    "-T",
                    "postgres",
                    "pg_isready",
                    "-U",
                    "devbrain",
                ],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=str(PROJECT_ROOT),
            )
            assert result.returncode == 0, (
                f"PostgreSQL is not ready. Output: {result.stderr}\n"
                "Run `make up` to start Docker services."
            )
        except FileNotFoundError:
            pytest.skip("Docker not found. Install Docker Desktop.")
        except subprocess.TimeoutExpired:
            pytest.fail("PostgreSQL check timed out. Is Docker running?")

    @pytest.mark.skipif(
        os.environ.get("CI") == "true",
        reason="Docker services not available in CI",
    )
    def test_redis_is_reachable(self) -> None:
        """Redis must be running and responding to PING."""
        try:
            result = subprocess.run(
                [
                    "docker",
                    "compose",
                    "exec",
                    "-T",
                    "redis",
                    "redis-cli",
                    "ping",
                ],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=str(PROJECT_ROOT),
            )
            assert "PONG" in result.stdout, (
                f"Redis did not respond with PONG. Output: {result.stdout}\n"
                "Run `make up` to start Docker services."
            )
        except FileNotFoundError:
            pytest.skip("Docker not found. Install Docker Desktop.")
        except subprocess.TimeoutExpired:
            pytest.fail("Redis check timed out. Is Docker running?")

    @pytest.mark.skipif(
        os.environ.get("CI") == "true",
        reason="Docker services not available in CI",
    )
    def test_pgvector_extension_enabled(self) -> None:
        """The pgvector extension must be enabled in PostgreSQL."""
        try:
            result = subprocess.run(
                [
                    "docker",
                    "compose",
                    "exec",
                    "-T",
                    "postgres",
                    "psql",
                    "-U",
                    "devbrain",
                    "-d",
                    "devbrain",
                    "-c",
                    "SELECT extname FROM pg_extension WHERE extname = 'vector';",
                ],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=str(PROJECT_ROOT),
            )
            assert "vector" in result.stdout, (
                "pgvector extension not found in PostgreSQL.\n"
                "Check scripts/init-db.sql and restart with "
                "`make down-clean && make up`"
            )
        except FileNotFoundError:
            pytest.skip("Docker not found. Install Docker Desktop.")
        except subprocess.TimeoutExpired:
            pytest.fail("pgvector check timed out. Is Docker running?")
