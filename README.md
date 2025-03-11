# Dad-Jokes-API-Access

A Jenkins job to run a Python script that accesses the Dad Jokes API.

### Prerequisites
1. **Jenkins Installed:** Ensure you have Jenkins installed and running on your machine or server.
2. **Python Installed:** Ensure Python is installed on the Jenkins server.
3. **Dad Jokes API Access:** You will be using a public API, so no special authentication is required.

### Step-by-Step Guide

#### Step 1: Install Necessary Jenkins Plugins
1. **Python Plugin:** Install the Python plugin (if necessary) to ensure Jenkins can run Python scripts. Go to `Manage Jenkins` -> `Manage Plugins` -> `Available` and search for "Python Plugin" to install it.

#### Step 2: Prepare Your Python Script
1. **Create a Script:** Write a Python script to access the Dad Jokes API. Save the script in a repository or on your Jenkins server. Below is an example script:

    ```python
    import requests

    def get_dad_joke():
        url = "https://icanhazdadjoke.com/"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            joke = response.json().get("joke")
            print(f"Dad Joke: {joke}")
        else:
            print("Failed to fetch a dad joke.")
    
    if __name__ == "__main__":
        get_dad_joke()
    ```

2. **Dependencies:** If you use external libraries (like `requests`), ensure they are listed in a `requirements.txt` file.

#### Step 3: Set Up Jenkins Job
1. **Create a New Job:**
   - Go to Jenkins Dashboard.
   - Click on `New Item`.
   - Enter an item name (e.g., `DadJokesJob`).
   - Select `Freestyle project`.
   - Click `OK`.

2. **Configure the Job:**
   - **Source Code Management:**
     - If your script is in a version control system (e.g., Git), configure the repository URL and credentials.
   - **Build Environment:**
     - Add a build step to execute a shell command.
     - Use a shell script to set up the environment and run your Python script. Example:
       ```bash
       #!/bin/bash
       # Navigate to the workspace directory
       cd $WORKSPACE
       # Create a virtual environment in the workspace
       python3 -m venv venv
       # Activate virtual environment
       source venv/bin/activate
       # Install dependencies
       pip install -r requirements.txt
       # Run the Python script
       python /path/to/your_script.py
       # Deactivate the virtual environment
       deactivate
       ```
   - **Post-build Actions:**
     - You can add notifications or other post-build actions if desired.

3. **Save and Run:**
   - Click `Save` to save your job configuration.
   - Run the job manually by clicking `Build Now` on the job page.

#### Step 4: Validate the Output
1. **Check Console Output:**
   - After the job runs, click on the build number in the `Build History`.
   - Click `Console Output` to see the results of your Python script execution, including the Dad Joke fetched from the API.

#### Step 5: Automate and Monitor
1. **Automate Builds:**
   - Set up build triggers if you want to automate the execution, such as running the job at regular intervals.
2. **Monitor:**
   - Use Jenkins monitoring tools and notifications to monitor job statuses and receive alerts for failures.

By following these steps, you will have a Jenkins job that can run a Python script to fetch and display a Dad Joke from the API. Adjust paths and configurations according to your specific setup and environment.

## Dependencies: 

External libraries (like requests), are listed in a requirements.txt file.
