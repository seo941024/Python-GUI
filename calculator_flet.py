import flet as ft

class NumberExtractor:
    def extract_numbers(self, inputs):
        pass  # to be overridden


class Calculator(NumberExtractor):
    def __init__(self, inputs):
        self.numbers = []
        self.non_numbers = []
        self.extract_numbers(inputs)

    def extract_numbers(self, inputs):
        for item in inputs:
            if isinstance(item, int):
                self.numbers.append(item)
            elif isinstance(item, (list, tuple)):
                for sub in item:
                    if isinstance(sub, int):
                        self.numbers.append(sub)
                    else:
                        self.non_numbers.append(sub)
            else:
                self.non_numbers.append(item)

        if self.non_numbers:
            print(f"Non-numeric inputs: {self.non_numbers}")

    def add(self):
        return sum(self.numbers)

    def subtract(self):
        result = self.numbers[0]
        for n in self.numbers[1:]:
            result -= n
        return result

    def multiply(self):
        result = 1
        for n in self.numbers:
            result *= n
        return result

    def divide(self):
        result = self.numbers[0]
        for n in self.numbers[1:]:
            if n == 0:
                print("cannot divide by zero.")
                return None
            result /= n
        return result

    def average(self):
        return sum(self.numbers) / len(self.numbers)

    def maximum(self):
        return max(self.numbers)

    def minimum(self):
        return min(self.numbers)


def main(page: ft.Page):
    page.title = "Calculator"

    input_field = ft.TextField(label="정수를 입력하세요. : ")
    result_text = ft.Text()

    def run_calc(e):
        try:
            num_list = list(map(int, input_field.value.split(",")))
            calc = Calculator(num_list)

            question = mode.value

            if question == "1":
                op = op_input.value

                if op == "+":
                    result_text.value = str(calc.add())
                elif op == "-":
                    result_text.value = str(calc.subtract())
                elif op == "*":
                    result_text.value = str(calc.multiply())
                elif op == "/":
                    result_text.value = str(calc.divide())

            elif question == "2":
                result_text.value = (
                    f"Average: {calc.average()}\n"
                    f"Max: {calc.maximum()}\n"
                    f"Min: {calc.minimum()}"
                )

            else:
                result_text.value = "Invalid option"

        except:
            result_text.value = "You must enter an integer."

        page.update()

    mode = ft.TextField(label="1: 연산 / 2: 평균, 최대, 최소")
    op_input = ft.TextField(label="연산자 (+, -, *, /)")
    btn = ft.ElevatedButton("실행", on_click=run_calc)

    page.add(
        input_field,
        mode,
        op_input,
        btn,
        result_text
    )


ft.app(target=main)