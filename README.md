# autonomous-system

Sensori:

    Sensori di temperatura e umidità in ogni stanza.

    Sensori di luminosità per regolare l'illuminazione.

    Sensori di qualità dell'aria (CO2, VOC, particolato).

    Sensori di presenza per rilevare l'occupazione delle stanze.

    Sensori di consumo energetico per monitorare l'uso di elettricità.

Effettori:

    Termostati intelligenti per regolare la temperatura.

    Lampadine smart per regolare l'illuminazione.

    Attuatori per aprire/chiudere le finestre o regolare l'oscuramento.

    Ventilatori e sistemi VMC per la qualità dell'aria.
    
Gli obiettivi di adattamento del sistema includono:

    Comfort: Mantenere temperature tra 20-24°C, umidità tra 40-60%, livelli di CO2 sotto 1000 ppm.

    Efficienza energetica: Minimizzare il consumo energetico spegnendo o riducendo l'uso di dispositivi quando non necessari.

    Qualità dell'aria: Mantenere livelli di CO2 e particolato entro limiti accettabili.

    Illuminazione: Regolare l'intensità della luce in base alla luce naturale e alla presenza di persone.

Per la funzione di decisione, utilizzeremo un approccio ibrido:

    Rule-based: Regole predefinite per situazioni comuni (es. "Se la temperatura supera 24°C, accendi il condizionatore").

    AI-based: Un modello di machine learning (es. regressione o reinforcement learning) per ottimizzare le decisioni in base a dati storici e contesto. Ad esempio, il sistema potrebbe imparare quando è più efficiente aprire le finestre invece di usare il condizionatore.

    Search-based: Algoritmi di ottimizzazione per trovare la combinazione migliore di azioni (es. bilanciare comfort e consumo energetico).
