# Automatedcipipelinetask


Automated CI Pipeline using Jenkins and GitHub

Project Overview

This project demonstrates how to automate the Continuous Integration (CI) process for a Python web application using Jenkins and GitHub.
Whenever a developer pushes code to GitHub, Jenkins automatically:

Fetches the latest source code.

Installs required dependencies.

Runs automated unit tests.

Packages the application into an artifact (artifact.zip).

Publishes the test reports and archives the build outputs.

The main goal is to ensure code quality, consistency, and faster development cycles by automating repetitive tasks that developers usually perform manually.

 Tools and Technologies Used

Tool	Purpose

GitHub	Code repository for version control
Jenkins	CI server to automate build and test processes
Python 3	Programming language for the sample application
Flask	Lightweight Python web framework
Pytest	Testing framework for automation tests
JUnit Plugin (Jenkins)	To visualize test reports
Virtual Environment (venv)	To isolate Python dependencies

Jenkins Pipeline Workflow
Stage 1: Checkout SCM

Jenkins pulls the source code from the GitHub repository.

https://github.com/MaheshBabu-018/Automatedcipipelinetask.git

Stage 2: Install Dependencies

Jenkins sets up a Python virtual environment.

Installs project dependencies from requirements.txt.

Stage 3: Run Tests

Runs automated unit tests using pytest.

Generates a JUnit XML report (reports/results.xml).

Stage 4: Build Artifact

Zips the project files into artifact.zip.

Excludes unnecessary folders like .git, __pycache__, and venv.

Stage 5: Archive Artifact

Jenkins archives the artifact.zip file as a build output.

Post Actions

Publishes test reports.

Displays success or failure messages.

Test Report and Artifacts



   You can find:

 Test Results: under “Test Result” or “Test Result Trend”.

 Artifacts: under “Build Artifacts” (contains artifact.zip).

 Pipeline Stages: under “Pipeline Steps” or “Blue Ocean View”.
