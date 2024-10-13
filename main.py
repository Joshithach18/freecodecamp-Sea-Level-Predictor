# main.py

from sea_level_predictor import draw_plot

def main():
    # Generate and display the plot
    fig = draw_plot()
    fig.show()

# Import and run tests from test_module.py
if __name__ == "__main__":
    main()
    import test_module
    test_module.run_tests()
