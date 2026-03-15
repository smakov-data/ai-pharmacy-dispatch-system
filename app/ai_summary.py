#from openai import OpenAI
#
#client = OpenAI()
#
#def generate_ai_summary(state, risk, confidence, recommendation_text):
#    prompt = f"""
#You are an operations assistant for a pharmacy delivery dispatch system.
#
#Current system state:
#CEI: {state['CEI']}
#CLI: {state['CLI']}
#NODI: {state['NODI']}
#WBI: {state['WBI']}
#
#Risk:
#{risk}
#
#Confidence:
#{confidence}
#
#Recommendation:
#{recommendation_text}
#
#Write a short operational summary in 3-4 sentences.
#Explain:
#1. the main issue
#2. what is happening operationally
#3. what dispatcher should do now
#
#Keep it concise and professional.
#"""
#
#    response = client.chat.completions.create(
#        model="gpt-4.1-mini",
#        messages=[
#            {"role": "user", "content": prompt}
#        ]
#    )
#
#    return response.choices[0].message.content.strip()

def generate_ai_summary(state, risk, confidence, recommendation):

    cei = state["CEI"]
    cli = state["CLI"]
    nodi = state["NODI"]
    wbi = state["WBI"]

    risk_level = risk["risk_level"]
    confidence_mode = confidence["confidence_mode"]
    decision_mode = recommendation["decision_mode"]

    return (
        f"Operational analysis indicates elevated system stress. "
        f"Courier load index (CEI) is {cei:.2f}, lateness risk (CLI) {cli:.2f}, "
        f"new order pressure (NODI) {nodi:.2f}, and dispatch bandwidth index (WBI) {wbi:.2f}. "
        f"Current system risk level is {risk_level} with {confidence_mode} confidence. "
        f"The system is operating under {decision_mode}. "
        f"Recommended operational action: {recommendation['recommendation']}"
    )