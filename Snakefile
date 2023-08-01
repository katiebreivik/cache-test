rule simulation:
    output:
        "src/data/simulation_1.npy"
    cache:
        True
    script:
        "src/scripts/simulation.py"

rule figure:
    input:
        "src/data/simulation_1.npy"
    output:
        "src/figures/figure.pdf"
    script:
        "src/scripts/fig.py"