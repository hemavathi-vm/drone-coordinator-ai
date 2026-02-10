# import pandas as pd


# # -----------------------------
# # LOAD PILOTS
# # -----------------------------
# def load_pilots():
#     df = pd.read_csv("data/pilot_roster.csv")

#     # convert skills to list
#     df["skills"] = df["skills"].apply(
#         lambda x: [s.strip() for s in str(x).split(",")]
#     )

#     # convert certifications to list
#     df["certifications"] = df["certifications"].apply(
#         lambda x: [c.strip() for c in str(x).split(",")]
#     )

#     return df.to_dict(orient="records")


# # -----------------------------
# # LOAD DRONES
# # -----------------------------
# def load_drones():
#     df = pd.read_csv("data/drone_fleet.csv")

#     # convert capabilities to list
#     df["capabilities"] = df["capabilities"].apply(
#         lambda x: [c.strip() for c in str(x).split(",")]
#     )

#     return df.to_dict(orient="records")


# # -----------------------------
# # LOAD MISSIONS
# # -----------------------------
# def load_missions():
#     df = pd.read_csv("data/missions.csv")
#     return df.to_dict(orient="records")


# # -----------------------------
# # TEST BLOCK
# # -----------------------------
# if __name__ == "__main__":
#     print("Pilots:")
#     print(load_pilots())

#     print("\nDrones:")
#     print(load_drones())

#     print("\nMissions:")
#     print(load_missions())



import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# -----------------------------
# GOOGLE SHEETS CONNECTION
# -----------------------------

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope
)

client = gspread.authorize(creds)

# OPEN YOUR SHEET
#sheet = client.open("Skylark_Drone_Data")
sheet = client.open_by_url(
    "https://docs.google.com/spreadsheets/d/1skxYyjW9aPQqyPImXghPp6KhcdP8WlTnvEBn_4TGOx4/edit?gid=0#gid=0"
)


# -----------------------------
# LOAD PILOTS
# -----------------------------
def load_pilots():
    worksheet = sheet.worksheet("pilot_roster")
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)

    df["skills"] = df["skills"].apply(
        lambda x: [s.strip() for s in str(x).split(",")]
    )

    df["certifications"] = df["certifications"].apply(
        lambda x: [c.strip() for c in str(x).split(",")]
    )

    return df.to_dict(orient="records")


# -----------------------------
# LOAD DRONES
# -----------------------------
def load_drones():
    worksheet = sheet.worksheet("drone_fleet")
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)

    df["capabilities"] = df["capabilities"].apply(
        lambda x: [c.strip() for c in str(x).split(",")]
    )

    return df.to_dict(orient="records")


# -----------------------------
# LOAD MISSIONS
# -----------------------------
def load_missions():
    worksheet = sheet.worksheet("missions")
    data = worksheet.get_all_records()
    return data


# -----------------------------
# UPDATE PILOT STATUS (WRITE BACK)
# -----------------------------
def update_pilot_status(pilot_name, new_status):

    worksheet = sheet.worksheet("pilot_roster")
    records = worksheet.get_all_records()

    for i, row in enumerate(records):
        if row["name"] == pilot_name:
            worksheet.update_cell(i + 2, 6, new_status)
            return True

    return False

if __name__ == "__main__":
    print("Pilots:")
    print(load_pilots())

    print("\nDrones:")
    print(load_drones())

    print("\nMissions:")
    print(load_missions())
