from common import ask_with_openai

ROUTE_NAME = "tokenrt"
QUESTION = """You are a highly knowledgeable assistant with expertise in environmental science and history. Analyze the following passage in terms of its scientific accuracy, coherence, and completeness. Highlight any inconsistencies or outdated information, and suggest more current alternatives where relevant. Also, provide a summary in bullet points for easier understanding:

"Climate change refers to the long-term alteration of temperature and typical weather patterns in a place. While climate change can occur naturally, current trends are heavily influenced by human activities, primarily the burning of fossil fuels such as coal, oil, and gas, which increases levels of greenhouse gases in the Earth's atmosphere. The Intergovernmental Panel on Climate Change (IPCC) has released multiple assessment reports that highlight how anthropogenic activity has resulted in global warming.

During the pre-industrial era, the atmospheric concentration of carbon dioxide (CO₂) was around 280 parts per million (ppm). As of 2023, this figure has surpassed 420 ppm, representing an increase of nearly 50% in less than two centuries. This rise correlates with the dramatic increase in industrial activities, urbanization, deforestation, and the widespread use of motorized transport systems. In addition to CO₂, other greenhouse gases like methane (CH₄), nitrous oxide (N₂O), and fluorinated gases have also contributed to the greenhouse effect.

Despite global agreements such as the Paris Accord, many countries are still falling short of their emissions reduction targets. Innovations in carbon capture and storage (CCS), green hydrogen, and next-generation nuclear reactors are promising, but they are not yet deployed at scale. Individual actions also matter: reducing meat consumption, minimizing air travel, and supporting climate policies can make a difference.

Ultimately, climate change is a multi-faceted challenge requiring coordinated global action, interdisciplinary solutions, and sustained public awareness."

Please provide:

A critique of the passage’s scientific content.

A list of any outdated facts or figures.

A 10-bullet summary highlighting the main points.
"""

HEADERS_WITH_KEY = {
    "Content-Type": "application/json",
    "apikey": "auth-one",
}

if __name__ == "__main__":
    for i in range(3):
        openai_res = ask_with_openai(ROUTE_NAME, QUESTION, HEADERS_WITH_KEY)
        print(openai_res)
