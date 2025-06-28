FEATURE_CONSTANTS = {
    "Lateral Driving": [
        {"id": 1001, "name": "Lane Keeping"},
        {"id": 1002, "name": "Lane Centering / Hands On"},
        {"id": 1003, "name": "Lateral Maneuver"},
        {"id": 1004, "name": "Hands Free"},
        {"id": 1005, "name": "Lane Change"}
    ],
    "Longitudinal Driving": [
        {"id": 2001, "name": "Overtaking support"},
        {"id": 2002, "name": "Set Speed"},
        {"id": 2003, "name": "Stop and Go"},
        {"id": 2004, "name": "Dynamic distance"},
        {"id": 2005, "name": "Set Distance / time gap"},
        {"id": 2006, "name": "Intelligent speed assist"},
        {"id": 2007, "name": "Legal speed"},
        {"id": 2008, "name": "Crowd Speed"},
        {"id": 2009, "name": "Curve speed"}
    ],
    "Urban/Rural": [
        {"id": 3001, "name": "Traffic light following"},
        {"id": 3002, "name": "Intersection following"},
        {"id": 3003, "name": "Right of way"},
        {"id": 3004, "name": "VRU handling"},
        {"id": 3005, "name": "Deadlock mitigation"},
        {"id": 3006, "name": "U turn handling"},
        {"id": 3007, "name": "PUDO management"},
        {"id": 3008, "name": "Remote assistance"},
        {"id": 3009, "name": "Follow route"},
        {"id": 3010, "name": "Re Routing"},
        {"id": 3011, "name": "Special Lanes"},
        {"id": 3012, "name": "Special Objects"},
        {"id": 3013, "name": "Special Zones"},
        {"id": 3014, "name": "Routing"}
    ],
    "System": [
        {"id": 4001, "name": "V2X-Based"},
        {"id": 4002, "name": "MRM"},
        {"id": 4003, "name": "ODD"},
        {"id": 4004, "name": "Guard for Pilot"},
        {"id": 4005, "name": "AV Display"}
    ]
}

def get_next_feature_id(theme):
    existing_ids = [f["id"] for f in FEATURE_CONSTANTS.get(theme, [])]
    if not existing_ids:
        base = {
            "Lateral Driving": 1000,
            "Longitudinal Driving": 2000,
            "Urban/Rural": 3000,
            "System": 4000
        }.get(theme, 5000)
        return base + 1
    return max(existing_ids) + 1