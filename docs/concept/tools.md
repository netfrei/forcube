## Rubik's cube



  - https://github.com/larspetrus/Roofpig)
  - https://lar5.com/cube/
  - http://jsfiddle.net/Lar5/86L4C/

### Anwendung mit der Komponente: Visualisation and navigation durch Filtermengen oder Bäume

  - Trees sind in python als hierarchische dictionaries repräsentiert. Sie können im JSON Format übergeben werden, z.B. per eine REST-api

    - Tree -> Cube
    - Dynamische trees könnten sich als Filter berechnen, wenn eine Abfolge von Filterbedingungen als Und-Verknüpfung aus den Datenbeständen errechnet werden.

    - Element 1) Eine Ebene des tree (horizontaler Schnitt) wird durch die Flächen einer Seite des Cubes abgebildet. Die Ebene können allgemein eine Liste von Filterkritieren sein, z.B. eine Zeitperiode, eine geographische Region, eine bestimmte Eigenschaft der Forschungsobjekte. Der Schnitt durch eine Ebene ergibt eine Menge von Elementen, die den Panels auf einer Seite des Cubes visualisiert werden. Mehr als 8 Elemente werden durch eine Funktion priorisiet (z.B. häufigste zuerst) und im 9ten Feld steht ein Fortsetzungszeichen. Wenn dieses gedrückt wird, werden die übrigen Elemente angezeigt.
      - Ereignisse:
        - Click auf Fläche
          - Animation mit Folge von Drehungen und Änderungen der Flächen
          - Übergang von einer Ebene zur nächsten Schnittebene
    - Element 1a)
        - Wurzelelement erhält eigene Darstellung (z.B. Informations Karte) aus den https://material-ui.com/components/cards/


    - Elemente 2) Der vertikale ancestor jeder Ebene wird als (klickbare) Sequenz visualisiert, z.B. über dem Cube. Diese Liste entspricht einer Liste mit und-Bedingungen eines Auswahlfilters. Die Flächen sind klickbar und aktualisieren die Schnittebene für den aktivierten Sequenzknoten

      - Die Elemente der Flächen enthalten key:values für Attibute:
        - Att1
        - Att2
        - ein dictionary übersetzt Attribute -> Visualisierungsattribute
          - Farbe
          - Text
          - weitere Visualisierungsmerkmale
          -
    - Element 3) Eine Actionkomponente (z.B. choice liste) wählt weitere Aktionen für den Würfel oder den Baum
      - Beispiele für die Action:
        - Auswahl einer Komponente (per Knoten)
        - Zugefügte weitere Filterkomponente

  ### Embedding the cube component

  - Streamlit componente
    - https://docs.streamlit.io/en/stable/develop_streamlit_components.html#create-a-static-component
    - https://docs.streamlit.io/en/stable/publish_streamlit_components.html
    - Bidirektionale Komponente, deren Aktions am Cube zurückgegeben werden als dictionary
  - Markdown component: integrate cube into markdown
    - https://reactjsexample.com/tag/markdown/
    - https://www.learnstorybook.com/intro-to-storybook/

## Material config

  - https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/

https://alinex.gitlab.io/env/mkdocs/ENABLE_PDF_EXPORT=1 mkdocs build

# icons

https://github.com/squidfunk/mkdocs-material/tree/master/material/.icons/fontawesome/regular

https://markdownmonster.west-wind.com/docs/_4ue01xl6q.htm
https://github.com/markdown-it/markdown-it-emoji/blob/master/lib/data/full.json
https://gist.github.com/rxaviers/7360908

### Tricks

actdiag {
  write -> convert -> image

  lane user {
     label = "User"
     write [label = "collect articles"];
     image [label = "Get diagram IMAGE"];
  }
  lane actdiag {
     convert [label = "PDF segmentation->XML"];
  }
}

http://blockdiag.com/en/blockdiag/examples.html#portrait-mode

blockdiag {
   A -> B -> C -> D;
   A -> E -> F -> G;
}

# Foliant

https://foliant-docs.github.io/docs/

Diagram with a caption:

<blockdiag caption="Sample diagram from the official site">
  blockdiag {
    A -> B -> C -> D;
    A -> E -> F -> G;
  }
</blockdiag>

* :material-account-circle:

:smile:

=== "Tab 1"
    Markdown **content**.

    Multiple paragraphs.

=== "Tab 2"
    More Markdown **content**.

    - list item a
    - list item b
