PRIORITY_RANK = {
    "Urgent": 3,
    "High": 2,
    "Standard": 1
}

SKILL_CAPABILITY_MAP = {
    "Mapping": ["RGB", "LiDAR"],
    "Inspection": ["RGB"],
    "Thermal": ["Thermal"]
}


# ----------------------------------------
# FIND ELIGIBLE PILOTS
# ----------------------------------------

def find_eligible_pilots(pilots, mission):

    eligible = []

    required_certs = [c.strip() for c in mission["required_certs"].split(",")]
    location = mission["location"]
    required_skill = mission["required_skills"]

    for pilot in pilots:

        if pilot["status"] != "Available":
            continue

        if not all(cert in pilot["certifications"] for cert in required_certs):
            continue


        if required_skill not in pilot["skills"]:
            continue

        if pilot["location"] != location:
            continue

        eligible.append(pilot)

    return eligible


# ----------------------------------------
# FIND ELIGIBLE DRONES
# ----------------------------------------

def find_eligible_drones(drones, mission):

    eligible = []

    required_skill = mission["required_skills"]
    location = mission["location"]

    required_capabilities = SKILL_CAPABILITY_MAP.get(required_skill, [])

    for drone in drones:

        if drone["status"] != "Available":
            continue

        if drone["location"] != location:
            continue

        # check capability match
        if not any(
            cap in drone["capabilities"]
            for cap in required_capabilities
        ):
            continue

        eligible.append(drone)

    return eligible


# ----------------------------------------
# CONFLICT DETECTION
# ----------------------------------------

def detect_conflicts(pilot, drone):

    warnings = []

    if pilot["status"] != "Available":
        warnings.append("Pilot not available")

    if drone["status"] == "Maintenance":
        warnings.append("Drone under maintenance")

    if pilot["location"] != drone["location"]:
        warnings.append("Pilot and drone in different locations")

    return warnings


# ----------------------------------------
# ASSIGNMENT SUGGESTION
# ----------------------------------------

def suggest_assignment(pilots, drones, mission):

    eligible_pilots = find_eligible_pilots(pilots, mission)
    eligible_drones = find_eligible_drones(drones, mission)

    if not eligible_pilots:
        return {"error": "No eligible pilots found"}

    if not eligible_drones:
        return {"error": "No eligible drones found"}

    pilot = eligible_pilots[0]
    drone = eligible_drones[0]

    warnings = detect_conflicts(pilot, drone)

    return {
        "project_id": mission["project_id"],
        "pilot": pilot["name"],
        "drone": drone["drone_id"],
        "warnings": warnings
    }

def urgent_reassignment(pilots, drones, mission):

    # only trigger for urgent missions
    if mission["priority"] != "Urgent":
        return None

    reassignment_options = []

    required_certs = [c.strip() for c in mission["required_certs"].split(",")]
    required_skill = mission["required_skills"]
    location = mission["location"]

    for pilot in pilots:

        # pilot must have required skill + cert
        if not all(cert in pilot["certifications"] for cert in required_certs):
            continue


        if required_skill not in pilot["skills"]:
            continue

        if pilot["location"] != location:
            continue

        # pilot currently assigned but could be replaced
        if pilot["status"] == "Assigned":
            reassignment_options.append(pilot)

    if not reassignment_options:
        return {
        "message": "No reassignment candidates available",
        "pilot_to_reassign": None
         }

    return {
    "message": "Urgent mission detected. Suggested reassignment.",
    "pilot_to_reassign": reassignment_options[0]["name"]
     }



# ----------------------------------------
# TEST BLOCK
# ----------------------------------------

if __name__ == "__main__":

    from data_loader import load_pilots, load_drones, load_missions

    pilots = load_pilots()
    drones = load_drones()
    missions = load_missions()

    result = suggest_assignment(pilots, drones, missions[0])
    print(result)
   

    urgent_result = urgent_reassignment(pilots, drones, missions[1])
    print(urgent_result)
