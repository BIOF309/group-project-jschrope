final-project-template
==============================

The purpose of this project is to load in a network/graph object and 
split the graph into communities using the girvan_newman algorithm (see 'references' folder)

Important Files:

    build_communities_final.py -- master script
        1. Loads in input adjacency matrix found in 'data' folder
        2. Divides the network into communities
        3. Saves .jpg image to current directory of the color-coded communities 
    
    girvan_newman_manual.py -- manually coded girvan_newman algorithm
        -- I had an issue with visualizing the output as it is a "generator" object. 
           I was having trouble accessing the data stores inside what should have been a tuple
           I plan to continue to look into this...
           
    build_graph_scratch.py -- lays out my three different attempts to create the graph object
                               with the correct connectivity (all unsuccessful unfortunately)
          
    slides.md -- markdown file that contains the presentation slides
        make_slides.py -- script that converts .md files into .html slides
        slides.html -- .html version of the slides
        
Project Outcome/Thoughts:

    Issues:     The connectivity of my current graph is messed up. The node positions seem to be correct, but the 
                edges clearly are not. It should look like more of a tesselation of polygon shapes that represent cells.
    
                I cannot for the life of me figure out why... When I create the graph in matlab from the adj_mat it works 
                just fine, so it's not the adjacency matrix itself. What it could be is the process of sacing the adj_mat
                to adj_mat.txt or how I am reading it in... (in matlab im not using the .txt file but the .mat file)
        
    Successes:  I mean I was able to use girvan_newman to split into communities... but thats not all that difficult
                I just type a letter into a pre-defined function. LIke i said I wrote my own version which I am pretty
                damn sure works, but I have trouble actually accessing the output to visualize it...
               
    
    Next Steps: Definitely fix the connectivity, then set up look to run successive time frames (super easy to do)
                and make a cute little color-coded video showing the dyamics of the network communities over time,
                and see how the communities might change over different phenotypes/treatment with drugs 

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <- Input data files used for the project 
    │
    ├── docs               <- Contains documents such as presentation slides pertaining to project
    │
    ├── references         <- References to the algorithms employed
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc. -- currently empty
    │   └── figures        <- Generated graphics and figures to be used in reporting -- currently empty
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data -- currently unmodified
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions -- currently empty
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
