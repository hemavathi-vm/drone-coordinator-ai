🚁 Drone Operations Coordinator AI Agent
Overview
This project implements an AI-based drone operations coordinator designed to manage pilots, drones, and mission assignments. The system simulates the responsibilities of a real drone operations coordinator by automatically matching pilots and drones to missions based on skills, certifications, availability, and location.

The AI agent also detects operational conflicts and suggests urgent reassignments when high-priority missions arise, helping reduce manual coordination effort.

Features

✅ Pilot roster management
✅ Drone inventory tracking
✅ Mission assignment based on skills and certifications
✅ Conflict detection (availability, certification, maintenance, location mismatch)
✅ Urgent reassignment suggestions for high-priority missions
✅ Conversational AI interface
✅ Web-based interface using Streamlit
✅ Google Sheets integration with data synchronization

How It Works

The system loads pilot, drone, and mission data from Google Sheets.
When a user requests an assignment, the agent:
Identifies eligible pilots based on skills, certifications, availability, and location.
Finds available drones matching required capabilities.
Checks for conflicts such as unavailable pilots, certification mismatches, or maintenance issues.
Suggests the best assignment or explains why assignment is not possible.
For urgent missions, the system evaluates reassignment options and proposes safe alternatives when available.

Running the Project

Install dependencies:
pip install -r requirements.txt

Run the application:
streamlit run app.py

Open the link shown in the terminal (usually http://localhost:8501).

Example Commands
Assign PRJ001
Assign PRJ002
urgent reassignment