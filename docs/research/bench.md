# Research-bench

## Computational notebooks

Die virtuelle Arbeitsumgebung von NFDI4SD wird mittels computational notebooks geschaffen. Als Relisationen des literate programmings von Donald Knuth wurden seit den 1980er die narrative Beschreibung des Ablaufs von Algorithmen in der Gestalt von Programmen als Gewebe oder Mischung von erklärendem Text und ausführbarem Programm entwickelt. Die heute weit verbreiteten Variante der Jupyter Notebooks haben die Erst-Entwickler Jernando Perez und Brian E. Granger als "An Open Source Framework for Interactive, Collaborative
and Reproducible Scientific Computing and Education" überschrieben und ihre Zielsetzung in den Punkten zusammengefaßt:[^2]


>   * "Individual exploration: a single investigator tests an idea, algorithm or question, likely with a small-scale test data set or simulation.
*  Collaboration: if the initial exploration appears promising, more often than not some kind of collaborative effort ensues.
*    Production-scale execution: large data sets and complex simulations often require the use of clusters, supercomputers or cloud resources in parallel.
*      Publication: whether as a paper or an internal report for discussion with colleagues, results need to be presented to others in a coherent form.
*      Education: ultimately, research results become part of the corpus of a discipline that is shared with students and colleagues, thus seeding the next cycle of research."

Mit Standardtechnologien kann auch der nicht speziell ausgebildete Forscher eine moderne digitale Arbeitsumgebung nutzen. Er wird dabei von der Research workbench in Form von erweiterten computational notebooks unterstützt. Der Wissenschaftler kann die vielfachen Angebote verschiedener IDE und Laufumgebungen von computational notebooks nach eigener Präferenz wählen. Der NFDI folgt der technologischen Entwicklung eng und beabsichtigt, die von den kleinen Fächern genutzten computational notebooks zu unterstützen. Die folgenden Bespiele zeigen die Umsetzung computational notebooks durch Jupyter Notebooks in der Webumgebung von Jupyterlab.[^1]

Die computational Notebooks entwickeln ihre Funktionalität und Bedienungsfreundlichkeit ständig weiter.

- Viele verschiedene vielversprechende Ansätze der kollaborativen Zusammenarbeit von Forschergruppen an einem Dokument sind bereits in fortgeschrittenem Entwicklungsstadium.
- Zukünftige Notebooks kombinieren die Vorzüge aktueller Entwicklungen von Computersprachen und gehen flexibel auf die verschiedenen Kompetenzfelder der Nutzer ein.

[^1]: [Jupyter](https://jupyter.org/), mit [Wiki](https://en.wikipedia.org/wiki/Project_Jupyter) und [Jupyterlab](https://jupyterlab.readthedocs.io/en/stable/).

[^2]: [Perez/Granger](https://ipython.org/_static/sloangrant/sloan-grant.html)

## Computational research objects

Für die Aufgaben der NFDI4SD werden die Anforderungen an open science research data durch eine erhebliche Erweiterung der Funktionalität von Notebooks übernommen. Das NFDI4SD entwickelt dazu ein Paket "Computational Research Objects" an zusätzlichen Funktionalitäten, in deren Zentrum die Einführung einer neuen Objektklasse *CompResearchObject* steht, deren Instanzen alle relevanten Informationen von Forschungsobjekten alle Attribute beschreibt.

# visualizing
