from data_loader import load_pilots, load_drones, load_missions
from logic import suggest_assignment, urgent_reassignment

def handle_query(user_input):

    pilots = load_pilots()
    drones = load_drones()
    missions = load_missions()

    user_input = user_input.lower()

    # ----------------------------
    # URGENT REASSIGNMENT (CHECK FIRST)
    # ----------------------------
    if "urgent" in user_input or "reassign" in user_input:

        for mission in missions:
            if mission["priority"] == "Urgent":
                result = urgent_reassignment(pilots, drones, mission)

                if result["pilot_to_reassign"]:
                    return (
                            f"{result['message']}\n"
                            f"Suggested Pilot: {result['pilot_to_reassign']}"
                           )
                else:
                    return result["message"]


        return "No urgent reassignment needed."

    # ----------------------------
    # ASSIGN MISSION
    # ----------------------------
    if "assign" in user_input:

        for mission in missions:
            if mission["project_id"].lower() in user_input:

                result = suggest_assignment(pilots, drones, mission)

                if "error" in result:
                    return result["error"]

                response = (
                    f"Suggested Assignment:\n"
                    f"Project: {result['project_id']}\n"
                    f"Pilot: {result['pilot']}\n"
                    f"Drone: {result['drone']}"
                )

                if result["warnings"]:
                    response += "\nWarnings:\n"
                    for w in result["warnings"]:
                        response += f"- {w}\n"

                return response

        return "Mission not found."

    return "I did not understand the request."




if __name__ == "__main__":
    while True:
        query = input("You: ")

        if query.lower() in ["exit", "quit", "bye"]:
            print("Agent: Goodbye!")
            break

        print(handle_query(query))
