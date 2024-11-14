import pandas as pd
import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, filename):
        self.data = pd.read_csv(filename)
        print("Дані успішно завантажено.")
        
        self.numeric_columns = self.data.select_dtypes(include='number').columns.tolist()
        print(f"Числові стовпці: {', '.join(self.numeric_columns)}")

    def get_extremes(self):
        extremes = self.data[self.numeric_columns].agg(['min', 'max'])
        print("Екстремальні значення по числовим стовпцям:")
        print(extremes)
        return extremes

    def preprocess_data(self):
        print("Обробка даних...")
        self.data = self.data.dropna()
        print("Обробка завершена")

    def visualize_columns(self, chart_type="line", save_png=False):
        for column in self.numeric_columns:
            print(f"Створення графіку для: {column} (Тип: {chart_type})")
            plt.figure(figsize=(10, 5))

            if chart_type == "line":
                plt.plot(self.data[column], label=column)
            elif chart_type == "bar":
                plt.bar(self.data.index, self.data[column], label=column)
            elif chart_type == "scatter":
                plt.scatter(self.data.index, self.data[column], label=column)
            elif chart_type == "hist":
                plt.hist(self.data[column], bins=10, label=column)
            elif chart_type == "pie" and len(self.data[column]) <= 10:
                plt.pie(self.data[column], labels=self.data.index, autopct="%1.1f%%")
                plt.title(f"Секторна діаграма для {column}")
                if save_png:
                    filename = f"{column}_{chart_type}_plot.png"
                    plt.savefig(filename)
                    print(f"Збережено як {filename}")
                plt.show()
                continue 
            else:
                print(f"Непідтримуваний тип графіка: {chart_type}")
                return

            plt.title(f"{chart_type.capitalize()} графік для {column}")
            plt.xlabel("Індекс")
            plt.ylabel(column)
            plt.legend()
            if save_png:
                filename = f"{column}_{chart_type}_plot.png"
                plt.savefig(filename)
                print(f"Збережено як {filename}")
            plt.show()

    def multiple_subplots(self, chart_type="line", save_png=False):
        fig, axes = plt.subplots(len(self.numeric_columns), 1, figsize=(10, len(self.numeric_columns) * 4))
        
        for i, col in enumerate(self.numeric_columns):
            if chart_type == "line":
                axes[i].plot(self.data[col])
            elif chart_type == "bar":
                axes[i].bar(self.data.index, self.data[col])
            elif chart_type == "scatter":
                axes[i].scatter(self.data.index, self.data[col])
            elif chart_type == "hist":
                axes[i].hist(self.data[col], bins=10)
            elif chart_type == "pie" and len(self.data[col]) <= 10:
                plt.figure(figsize=(6, 6))
                plt.pie(self.data[col], labels=self.data.index, autopct="%1.1f%%")
                plt.title(f"Секторна діаграма для {col}")
                if save_png:
                    filename = f"{col}_{chart_type}_plot.png"
                    plt.savefig(filename)
                    print(f"Збережено як {filename}")
                plt.show()
                continue 
            else:
                print(f"Непідтримуваний тип графіка або занадто багато значень для секторної діаграми: {chart_type}")
                return
        
            axes[i].set_title(f"{chart_type.capitalize()} графік для {col}")
        
        plt.tight_layout()
        if save_png and chart_type != "pie":  
            filename = f"multiple_{chart_type}_plots.png"
            plt.savefig(filename)
            print(f"Збережено всі піддіаграми як {filename}")
        plt.show()
