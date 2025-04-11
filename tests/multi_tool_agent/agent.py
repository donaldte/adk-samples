import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    """Récupère le rapport météo actuel pour une ville spécifiée du Cameroun.

    Args:
        city (str): Le nom de la ville.

    Returns:
        dict: statut et résultat ou message d'erreur.
    """
    city = city.lower()
    if city == "yaoundé":
        return {
            "status": "succès",
            "report": "Le temps à Yaoundé est ensoleillé avec une température de 28°C."
        }
    elif city == "douala":
        return {
            "status": "succès",
            "report": "Le temps à Douala est nuageux avec une température de 30°C."
        }
    elif city == "bamenda":
        return {
            "status": "succès",
            "report": "Le temps à Bamenda est pluvieux avec une température de 22°C."
        }
    else:
        return {
            "status": "erreur",
            "error_message": f"Désolé, je n'ai pas d'informations météo pour '{city}'."
        }


def get_current_time(city: str) -> dict:
    """Retourne l'heure actuelle pour une ville spécifiée du Cameroun.

    Args:
        city (str): Le nom de la ville.

    Returns:
        dict: statut et résultat ou message d'erreur.
    """
    city = city.lower()
    if city in ["yaoundé", "douala", "bamenda"]:
        tz = ZoneInfo("Africa/Douala")
        now = datetime.datetime.now(tz)
        report = f"Heure actuelle à {city.capitalize()} : {now.strftime('%d/%m/%Y %H:%M:%S')}"
        return {"status": "succès", "report": report}
    else:
        return {
            "status": "erreur",
            "error_message": f"Désolé, je ne connais pas la ville '{city}'. Veuillez choisir Yaoundé, Douala ou Bamenda."
        }

# Agent adapté uniquement pour les villes camerounaises et en français
root_agent = Agent(
    name="agent_meteo_heure_cameroun",
    model="gemini-2.0-flash-exp",
    description=(
        "Agent qui répond aux questions sur l'heure et la météo dans les villes du Cameroun (Yaoundé, Douala, Bamenda)."
    ),
    instruction=(
        "Je peux répondre à vos questions sur l'heure et la météo à Yaoundé, Douala et Bamenda. Posez-moi votre question en français."
    ),
    tools=[get_weather, get_current_time],
)
