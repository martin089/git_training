import pytest
from src.applications.api.github_api_client import GitHubAPIClient


def pytest_html_report_title(report):
    report.title = "Search github topics!"

@pytest.fixture
def git_hub_api_cliet():
    api = GitHubAPIClient()
    api.login()

    yield api

    api.logout()