from rules import career_rules

def infer_career(student_inputs):

    recommendations = []

    for rule in career_rules:

        matched = all(condition in student_inputs for condition in rule["conditions"])

        if matched:

            result = {
                "career": rule["career"],
                "reason": rule["reason"],
                "conditions": rule["conditions"]
            }

            recommendations.append(result)

    return recommendations