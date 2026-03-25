import os
from github import Github # type: ignore

g = Github(os.getenv("GITHUB_TOKEN"))
repo = g.get_repo("your-username/SwiftChain-Frontend")

issues = [

    # AUTH
    {
        "title": "Implement User Registration UI",
        "body": """
## Description
Build registration page for users (customers, drivers, admins).

## Location
Frontend - features/auth

## Tasks
- Create form using React Hook Form
- Validate inputs
- Connect to backend API
- Handle errors and loading states

## Acceptance Criteria
- User can register successfully
- API integration works
- Toast notifications displayed
- No mock data used

## PR Requirements
- Assignment required
- Follow CONTRIBUTING.md
- No hardcoded values
- Closes #[issue_id]
""",
        "labels": ["frontend", "high"]
    },

    # DELIVERY
    {
        "title": "Implement Delivery List Page",
        "body": """
## Description
Create a page to display all deliveries with filtering and sorting.

## Location
Frontend - features/deliveries

## Tasks
- Fetch deliveries from API
- Display list UI
- Add filters and sorting
- Handle empty states

## Acceptance Criteria
- Data fetched from backend
- Filters work correctly
- UI is responsive
- No mock data

##  PR Requirements
- Assignment required
- Follow CONTRIBUTING.md
- No hardcoded values
- Closes #[issue_id]
""",
        "labels": ["frontend", "high"]
    },

]

for issue in issues:
    repo.create_issue(
        title=issue["title"],
        body=issue["body"],
        labels=issue["labels"]
    )