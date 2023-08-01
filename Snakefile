rule simdat:
    output:
        directory("src/data/sim/")
    cache:
        True
    script:
        "src/scripts/simulation.py"

rule figure:
    input:
        "src/data/sim/"
    output:
        "src/figures/figure.pdf"
    script:
        "src/scripts/fig.py"