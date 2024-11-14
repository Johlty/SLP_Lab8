from Class.DataVisualizer import DataVisualizer
from Interface.user_interface import get_chart_type, ask_save_choice
from Functions.file_operations import load_data

if __name__ == "__main__":
    filename = "E:/SC Python/lab8/your_data.csv"
    data = load_data(filename)
    
    if data is not None:
        visualizer = DataVisualizer(filename)
        visualizer.get_extremes()
        visualizer.preprocess_data()

        chart_type = get_chart_type()
        if chart_type:
            save_png = ask_save_choice()
            visualizer.multiple_subplots(chart_type, save_png)
        else:
            print("Помилка, повторіть спробу")
