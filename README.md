# Bitcoin Data Fetcher

This repository contains a script to fetch Bitcoin data and a GitHub Actions workflow to automate the process.

## GitHub Actions Workflow

The repository includes a GitHub Actions workflow that:
- Runs automatically every 49 minutes
- Can be triggered manually
- Fetches Bitcoin data using the `fetchData.py` script

## Setup

### GitHub Secrets

To run the workflow, you need to set up the following secrets in your GitHub repository:

| Secret Name      | Description                        |
| ---------------- | ---------------------------------- |
| `BACKEND_URL`    | URL of the backend API             |
| `TOKEN_ENDPOINT` | Endpoint for token authentication  |
| `DATA_ENDPOINT`  | Endpoint for fetching Bitcoin data |
| `USERNAME`       | Username for API authentication    |
| `ADMIN_PASSWORD` | Password for API authentication    |

### Manual Trigger

To manually trigger the workflow:
1. Go to the "Actions" tab in your GitHub repository
2. Select the "Fetch Bitcoin Data" workflow
3. Click "Run workflow"
4. Click the green "Run workflow" button

## Local Development

To run the script locally:

1. Create a `.env.local` file with the following variables:
```
backend_url=your_backend_url
token_endpoint=your_token_endpoint
data_endpoint=your_data_endpoint
username=your_username
admin_password=your_password
```

2. Install dependencies:
```bash
pip install requests python-dotenv
```

3. Run the script:
```bash
python fetchData.py 